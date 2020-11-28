# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 21:40:33 2020

@author: hp
"""

import streamlit as st
import numpy as np
import pandas as pd
 
from sklearn.preprocessing import StandardScaler

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


def missing_data(training_data):
     
    training_data = training_data.fillna(training_data.mean())
    return training_data 
        

def encoding(training_data):
    
#    for i in len(training_data): 
#        training_data['ID'] = training_data['ID'].replace()
    training_data=training_data.drop(['ID'],axis =1)
#    st.write(training_data.describe())
#    st.write(training_data.select_dtypes(include = 'object'))
#    data.select_dtypes(include = 'object')
    
    arr = training_data.select_dtypes(include = 'object')
    cols = arr.columns
    print(cols) 
    for i in range(len(cols)):
#        training_data = pd.get_dummies(training_data, columns=[col]) 
#        print(training_data[col].value_counts())
#        print(training_data[col].isna().sum())
        print(cols[i])
        training_data = pd.get_dummies(training_data, columns=[cols[i]]) 
         
#    print(training_data['Outlet_Size'].isna().sum())
#    st.write(training_data)
    return training_data
     
        
 
def normalisation(training_data):
        
    sc_X = StandardScaler()
#    st.write(training_data)
    training_data = sc_X.fit_transform(training_data)
    return training_data

#g_data = []
     
 
class Regression:
    
    
    file = st.file_uploader('Upload Dataset')
    if file is not None:
        data = load_data(file)
        st.write('Training Data')
        training_data = train_data(data)
        st.write(training_data)
        st.write('Output Column')
        y = output_col(data)
        st.write(y)
        
    st.subheader('Imputation')
    st.text('Fill the missing data using one of the following options')
    training_data = missing_data(training_data)
    if st.button('Mean'):
        st.write(training_data)


    st.subheader('Encoding of the data')
    st.text('Convert categorical data into numerical data')
#    st.write(training_data)
    training_data = encoding(training_data)
    if st.button('Encode'):
        st.write(training_data)
 
 
        
    st.subheader('Normalize the data')
    training_data = normalisation(training_data)
    if st.button('Normalize'):
        st.write(training_data)
        
    
 
class Classfication:
    def __init__(self):
        file = st.file_uploader('Upload Dataset')



if __name__ == "__main__":
    Main()
    






