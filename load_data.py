
import streamlit as st
import pandas as pd

@st.cache
def get_data(file):
    data = pd.read_csv(file)
    
    return data
     
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

@st.cache
def load_test_data(test_file):
    test_data = pd.read_csv(test_file)
    test_data = test_data.iloc[:,:]
    return test_data

