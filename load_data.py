
import streamlit as st
import pandas as pd
import snowflake.connector as snow
from snowflake.connector.pandas_tools import write_pandas

# @st.experimental_singleton
def init_connection():
    return snow.connect(
        **st.secrets["snowflake"], client_session_keep_alive=True
    )

conn = init_connection()

# @st.cache_data(ttl=600)
def get_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetch_pandas_all()


@st.experimental_memo
def get_data(file):
    data = pd.read_csv(file)
    
    ##Create empty table
    table_name = (file.name).split(".")[0].upper()
    schema = 'PUBLIC'
    database = 'RDATA'
    qu = "CREATE DATABASE IF NOT EXISTS RDATA"
    conn.cursor().execute(qu)
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

    write_pandas(conn, data, table_name)
 
    rows = get_query("SELECT * from " + table_name)
    
    return rows
     
def train_data(data):
    training_data = data.iloc[:,:-1]
    return training_data   

def output_col(data):
    y = data.iloc[:,-1]
    return y

def output_col_classification(data):
    cols = data.columns.tolist()
    col = cols[-1]
    st.write(col)
    y = pd.get_dummies(data,columns=[col],drop_first=True)
    y = y.iloc[:,-1]
    # st.write(y)

    # col = y.columns.tolist()
    # print(col)
    # y = pd.get_dummies(y,columns=[col[0]],drop_first=True)
    
    return y

@st.experimental_memo
def load_test_data(test_file):
    test_data = pd.read_csv(test_file)
    test_data = test_data.iloc[:,:]
    return test_data

