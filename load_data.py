
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

@st.cache
def load_test_data(test_file):
    test_data = pd.read_csv(test_file)
    test_data = test_data.iloc[:,:]
    return test_data

