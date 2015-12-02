"""
   Wrapper on psycopg2's connection pool class. Pandas will call this 
   class to obtain a connection and then work with it to query the database
   Srivatsan Ramanujam <vatsan.cs@utexas.edu>, June 2015
"""

import psycopg2
from psycopg2 import pool
import pandas.io.sql as psql
import os
import json
import ConfigParser

DEFAULT_PORT = 9090

class DBConnect(object):
    def __init__(self, logger, conn_str=None):
        """Constructor"""
        self.logger = logger
        host, port, user, database, password, app_port = None, None, None, None, None, None
        if(not conn_str):
            if(os.getenv("PORT")):
                app_port = int(os.getenv("PORT"))
                vcap_services = json.loads(os.environ['VCAP_SERVICES'])
                creds = vcap_services['user-provided'][0]['credentials']
                host = creds['host']
                user = creds['user']
                database = creds['database']
                password = creds['password']
                port = creds['port']
            else:
                #default port
                app_port = DEFAULT_PORT
                #Read database credentials from user supplied file
                basepath = os.path.dirname(__file__)
                conf = ConfigParser.ConfigParser()
                conf.read(os.path.join(basepath,'user.cred'))
                self.logger.debug('Config sections:'+','.join(conf.sections()))
                #host, port, user, database, password
                host = conf.get('database_creds','host')
                port = conf.get('database_creds','port')
                user = conf.get('database_creds','user')
                database = conf.get('database_creds','database')
                password = conf.get('database_creds','password')

            #Initialize connection string
            conn_str =  """dbname='{database}' user='{user}' host='{host}' port='{port}' password='{password}'""".format(                       
                                database=database,
                                host=host,
                                port=port,
                                user=user,
                                password=password
                        )
        self.conn_str = conn_str
        self.__initConnectionPool__()

    def __initConnectionPool__(self):
        """
           Initialize a connection pool
        """
        self.pool = psycopg2.pool.SimpleConnectionPool(1, 5, self.conn_str)

    def __is_dbconn_alive__(self):
        """ 
           Ping the DB and check if the connection is alive - it seems like conn.closed doesn't work all the time 
        """
        ping_cmd = """select 1;"""
        conn_alive = True
        isQuery = True
	conn_from_pool = self.pool.getconn()
        try:
            df = psql.read_sql(ping_cmd, conn_from_pool)
        except psycopg2.Error, e:
            self.logger.error('Database connection is not alive: '+str(e))
            conn_alive = False
        finally:
	    self.pool.putconn(conn_from_pool)
        return conn_alive

    def __reconnect_if_closed__(self, conn_str=None):
        """
           Reconnect if the connection has failed/timed-out or has been closed down
        """
        if(self.pool.closed or not self.__is_dbconn_alive__()):
            self.pool.closeall()
            self.logger.warn('Detected closed connections. Reconnecting...')
            self.__initConnectionPool__()

    def fetchDataFrame(self, query):
        """
           Execute query
        """
        self.__reconnect_if_closed__()
	conn_from_pool = self.pool.getconn()
	df = psql.read_sql(query, conn_from_pool)
	self.pool.putconn(conn_from_pool)
        return df
