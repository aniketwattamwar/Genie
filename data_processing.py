import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
import pickle
import numpy as np
import pandas as pd
import base64
import streamlit as st

class Processing:

    def missing_data(training_data):
        for col in training_data.columns:
            count_unique = training_data[col].nunique()
            if count_unique == training_data.shape[0]:
                training_data=training_data.drop([col],axis =1)
                # st.text(training_data)
        training_data = training_data.fillna(training_data.mean())
        return training_data 

    def encoding(training_data):
        
    #    for i in len(training_data): 
    #        training_data['ID'] = training_data['ID'].replace()
        st.write(training_data.info())
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

    
     
        
