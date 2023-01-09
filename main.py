# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 21:40:33 2020

@author: hp
"""

import streamlit as st
import numpy as np
import pandas as pd
import base64
import csv
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
import pickle
import data_processing
import Regression
import Classification
import details
class Main:
    
    def __init__(self):
    
        selected_box = st.sidebar.selectbox(
        'Choose one of the following',
        ('Welcome','Regression', 'Classification', 'Natural Language Processing')
        )
        
        if selected_box == 'Welcome':
            self.welcome() 
        if selected_box == 'Regression':
            details.Details()
            Regression.Regression()
        if selected_box == 'Classification':
            # details.Details()
            Classification.Classification()
        if selected_box == 'Natural Language Processing':

            NLP()


    def welcome(self):
        
        st.text("Choose which type of problem you would like to solve from the left side bar!")
        st.image('genie.jpg',use_column_width=True)
        st.title('Genie - A webapp to download models & predictions')
        st.header('You can upload datasets and choose your algorithms and obtain a model and a predicted file in minutes')
        
 

def download_model(model):
    output_model = pickle.dumps(model)
    b64 = base64.b64encode(output_model).decode()
    href = f'<a href="data:file/output_model;base64,{b64}" download="myfile.pkl">Download Trained Model .pkl File</a>'
    st.markdown(href, unsafe_allow_html=True)
    
def download_predicted_csv(regressor,test_data):
    ypred =regressor.predict(test_data)
    output = pd.DataFrame(ypred)
    _csv = output.to_csv()
    b64 = base64.b64encode(_csv.encode()).decode()  # some strings <-> bytes conversions necessary here
    href = f'<a href="data:file/csv;base64,{b64}">Download Test Set Predictions CSV File</a> (right-click and save as &lt;some_name&gt;.csv)'
    st.markdown(href, unsafe_allow_html=True)


class NLP():
    def __init__(self):
        st.header("Coming Soon ..!")
        


if __name__ == "__main__":
    Main()
    






