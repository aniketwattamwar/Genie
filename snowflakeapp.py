# streamlit_app.py

import streamlit as st
import snowflake.connector as snow
import pandas as pd
from snowflake.connector.pandas_tools import write_pandas

# Initialize connection.
# Uses st.cache_resource to only run once.
# @st.experimental_singleton
def init_connection():
    return snow.connect(
        **st.secrets["snowflake"], client_session_keep_alive=True
    )

conn = init_connection()

##Create empty table
table_name = 'TABLEDATA'
schema = 'PUBLIC'
database = 'RDATA'

# q = "USE DATABASE RDATA"
# conn.cursor().execute(q)

# Perform query.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
# @st.cache_data(ttl=600)
def get_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

## Putting the file on snowflake
file = st.file_uploader('Upload Dataset')
if file is not None:
    data = pd.read_csv(file)
    # #Create the SQL statement to create or replace the table
    create_tbl_statement = "CREATE OR REPLACE TABLE " + schema + "." + table_name + " ( "
    q = "USE DATABASE RDATA"
    # Loop through each column finding the datatype and adding it to the statement
    for column in data.columns:
        print(data[column].dtype.name)
        if (data[column].dtype.name == "int" or data[column].dtype.name == "int64"):
            create_tbl_statement = create_tbl_statement + column + " int"
        elif data[column].dtype.name == "object":
            create_tbl_statement = create_tbl_statement + column + " varchar(16777216)"
        elif data[column].dtype.name == "datetime64[ns]":
            create_tbl_statement = create_tbl_statement + column + " datetime"
        elif data[column].dtype.name == "float64":
            create_tbl_statement = create_tbl_statement + column + " float8"
        elif data[column].dtype.name == "bool":
            create_tbl_statement = create_tbl_statement + column + " boolean"
        else:
            create_tbl_statement = create_tbl_statement + column + " varchar(16777216)"

        # # If column is not last column, add comma, else end sql-query
        if data[column].name != data.columns[-1]:
            create_tbl_statement = create_tbl_statement + ", "
        else:
            create_tbl_statement = create_tbl_statement + " )"
        print(create_tbl_statement)
         
    #Execute the SQL statement to create the table
    conn.cursor().execute(q)
    conn.cursor().execute(create_tbl_statement)

    write_pandas(conn, data, "TABLEDATA")
    rows = get_query("SELECT * from TABLEDATA;")

    # Print results.
    st.table(rows)
    



    
    

