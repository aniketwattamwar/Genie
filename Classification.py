import streamlit as st
import data_processing
import load_data
import pandas as pd
import base64
import pickle


class Classification:
    # st.text("Testing")

    def __init__(self):
       
        # file = st.file_uploader('Upload Dataset')
        # if file is not None:
        #     data = load_data.get_data(file)
        #     st.write('Training Data')
        #     training_data = load_data.train_data(data)
        #     st.write(training_data)
        #     st.write('Output Column')
        #     y = load_data.output_col(data)
        #     st.write(y)
            
        st.subheader('Imputation')
        st.text('Fill the missing data using one of the following options')
        if st.checkbox('Mean'):
            training_data = data_processing.Processing.missing_data(training_data)
            st.write(training_data)
    
    
        st.subheader('Encoding of the data')
        st.text('Convert categorical data into numerical data')
        if st.checkbox('Encode') :   
            training_data = data_processing.Processing.encoding(training_data)
            st.write(training_data)
             
       
        st.subheader('Normalize the data')
        
        if st.checkbox('Normalize'):
            training_data = data_processing.Processing.normalisation(training_data)
            st.write(training_data)
            
            
        st.subheader('Upload test data')
        st.text('Note: The above parameters for preprocessing will be automatically\n'+
                'used for the test data')
        test_file = st.file_uploader('Upload')
        if test_file is not None:
            test_data = load_data.load_test_data(test_file)
             
            test_data = data_processing.Processing.missing_data(test_data)
            test_data = data_processing.Processing.encoding(test_data)
            test_data = data_processing.Processing.normalisation(test_data)
#            test_data = normalisation(test_data)
            st.write(test_data)


