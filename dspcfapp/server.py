"""
   Server side components for your app
   Srivatsan Ramanujam <vatsan.cs@utexas.edu>, 28-May-2015
"""

import os
import json
from flask import Flask, render_template, jsonify, request
from flask.ext.assets import Bundle, Environment
import logging
from dbconnector import DBConnect, DEFAULT_PORT
from sql.queries import *

#init app
app = Flask(__name__)

#init logger
logging.basicConfig(level= logging.DEBUG if not os.getenv('PORT') \
        else logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

#init flask assets
bundles = {
    'user_js': Bundle(
            #all your javascript files in static folder, go here
            'js/heatmap.js',
            filters='jsmin' if os.getenv('PORT') else None, #minify if deploying on CF
            output='gen/user.js',
        ),
    'user_css': Bundle(
            #all your css files in the static folder, go here
           'css/custom.css',
            filters='jsmin' if os.getenv('PORT') else None, #minify if deploying on CF
            output='gen/user.css'
        )   
}
assets = Environment(app)
assets.register(bundles)

#Initialize database connection objects
conn = DBConnect(logger)

def index():
    """
       Render homepage
    """
    return render_template('index.html', title='dspcfboilerplate')

@app.route('/')
@app.route('/home')
def home():
    """
       Homepage
    """
    logger.debug('In home()')
    return render_template('home.html')

@app.route('/about')
def about():
    """
       About page, listing background information about the app
    """
    logger.debug('In about()')
    return render_template('about.html')

@app.route('/contact')
def contact():
    """
       Contact page
    """
    logger.debug('In contact()')
    return render_template('contact.html')
    
@app.route('/settings')
def settings():
    """
       Settings page (for model building)
    """
    logger.debug('In settings()')
    return render_template('settings.html')    

@app.route('/<path:path>')
def static_proxy(path):
    """
       Serving static files
    """
    logger.debug('In static_proxy()')
    return app.send_static_file(path)

@app.route('/_hmap')    
def sample_heatmap():
    """
        Populate a sample heatmap
    """
    global conn
    INPUT_SCHEMA = 'public'
    INPUT_TABLE = 'sample_heatmap'
    sql = fetch_sample_data_for_heatmap(INPUT_SCHEMA, INPUT_TABLE)
    logger.info(sql)
    df = conn.fetchDataFrame(sql)
    logger.info('sample_heatmap: {0} rows'.format(len(df)))
    return jsonify(hmap=[{'machine_id':r['id'], 'hour':r['hour'], 'prob':r['prob']} for indx, r in df.iterrows()])    

def main():
    """
       Start the application
    """
    app_port = int(os.environ.get('PORT',33512))
    app.run(host='0.0.0.0',  port = app_port)

if __name__ == '__main__':
    main()
