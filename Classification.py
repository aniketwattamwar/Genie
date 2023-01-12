import streamlit as st
import data_processing
import load_data
import pandas as pd
import base64
import pickle

from sklearn.linear_model import LogisticRegression
from xgboost import XGBClassifier

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


class Classification:
    # st.text("Testing")

    def __init__(self):
       
        file = st.file_uploader('Upload Dataset')
        if file is not None:
            data = load_data.get_data(file)
            st.write('Training Data')
            training_data = load_data.train_data(data)
            st.write(training_data)
            st.write('Output Column')
            y = load_data.output_col_classification(data)
            st.write(y)
            
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
            st.write(test_data)

        st.subheader('Choose one of the algorithms to train your data')
        st.text('You can also download the .pkl file and the prediction file post\nchoosing an algorithm')
        algo = st.radio("",
                        ('Disabled','Logistic Regression','XGBoost'))

        if algo == "Logistic Regression":
            lg = LogisticRegression()
            logit = lg.fit(training_data, y)
            st.write('Model Trained Successfully')
            download_model(logit)
            ypred =logit.predict(test_data)
            st.write(ypred)
            download_predicted_csv(logit,test_data)
            
        if algo == "XGBoost":
            xgb = XGBClassifier(learning_rate = 0.01,n_estimators=1000)
            xgb.fit(training_data, y)
            ypred =xgb.predict(test_data)
            print(ypred)
            download_model(xgb)
            st.write(ypred)
            download_predicted_csv(xgb,test_data)

