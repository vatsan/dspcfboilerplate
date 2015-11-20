
"""
Your SQL code goes here (model building, scoring, visualization)
Srivatsan Ramanujam <vatsan.cs@utexas.edu>, June-2015
"""
def fetch_sample_data_for_heatmap(input_schema, input_table):
    """
        Inputs:
        =======
        input_schema (str): The schema containing the input table
        input_table (str): The table in the input_schema containing data from the wells
        Outputs:
        ========
        A sql code block        
    """
    #You can write a query to fetch data from input_table, in input_schema
    sql = """
        select
            machine - 1 as id,
            hod-1 as hour,
            random() as prob
        from
            generate_series(1, 15) as machine,
            generate_series(1, 24) as hod;
    """
    return sql