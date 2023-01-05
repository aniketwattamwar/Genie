
import streamlit as st
import load_data

class Details:
    def __init__(self):
        st.subheader("Please read the instructions below")
        st.text("1.) Choose all the options in the way they are given. Skipping anyone will throw an error")
        st.text("2.) After uploading the dataset if you get parsing error, reupload the dataset.")
        st.text("3.) The preprocessing options chosen for training data will be automatically used\n" + "for testing data as well")
        st.text("4.) While downloading the csv file, make sure to rename it with .csv extension")
        
        



