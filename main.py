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
    

#def load_data(nrows):
#    data = pd.read_csv()


class Regression:
    
    def __init__(self):
        file = st.file_uploader('Upload Dataset')
        if file is not None:
            data = pd.read_csv(file)
            st.write(data)
         
        
        

class Classfication:
    def __init__(self):
        file = st.file_uploader('Upload Dataset')



if __name__ == "__main__":
    Main()
    






