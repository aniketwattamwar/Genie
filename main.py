# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 21:40:33 2020

@author: hp
"""

import streamlit as st
import numpy as np
import pandas as pd



class Main:
    
    def __init__(self):
    
        selected_box = st.sidebar.selectbox(
        'Choose one of the following',
        ('Welcome','Regression', 'Classification')
        )
        
        if selected_box == 'Welcome':
            self.welcome() 
        if selected_box == 'Regression':
            Regression()
        if selected_box == 'Classification':
           Classfication()


    def welcome(self):
            
        st.title('Genie- A webapp to download predictions')
        st.header('You can upload datasets and choose your algorithms and obtain a predicted file in minutes')
    


@st.cache
def load_data(file):
    data = pd.read_csv(file)
    
    return data
     
def train_data(data):
    training_data = data.iloc[:,:-1]
    return training_data   

def output_col(data):
    y = data.iloc[:,-1]
    return y

def encoding(training_data):
     
     
    st.write(training_data.describe())
    st.write(training_data.select_dtypes(include = 'object'))
#    data.select_dtypes(include = 'object')
    
    arr = training_data.select_dtypes(include = 'object')
    cols = arr.columns
    print(cols[0])
    for col in cols:
        training_data = pd.get_dummies(training_data, columns=[col]) 
    st.write(training_data) 
        
  
    

#g_data = []
     
 
class Regression:
    
    def __init__(self):
        file = st.file_uploader('Upload Dataset')
        if file is not None:
            data = load_data(file)
            st.write('Training Data')
            training_data = train_data(data)
            st.write(training_data)
            st.write('Output Column')
            y = output_col(data)
            st.write(y)
        
        
        if st.button('Encoding the data'):
#            data = load_data(file)
            encoding(training_data)
            st.write("insdie preprocessed data")
    
        
        

class Classfication:
    def __init__(self):
        file = st.file_uploader('Upload Dataset')



if __name__ == "__main__":
    Main()
    






