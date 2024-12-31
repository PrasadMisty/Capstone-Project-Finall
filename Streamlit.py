#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import joblib
import pandas as pd
import os
import requests

# Load the model
#model_path = os.path.join(os.getcwd(), 'Saved Model\\fraud_detection_model.joblib')
model_url = 'https://raw.githubusercontent.com/PrasadMisty/Capstone-Project-Finall/master/Saved Model/fraud_detection_model.joblib'
response = requests.get(model_url)
mfile = BytesIO(response.content)
model = joblib.load(mfile)

# Streamlit app
st.title("Fraud Detection Prediction")

st.sidebar.header("Input Features")
time = st.sidebar.number_input("Time", value=0.0, step=0.1)
v2 = st.sidebar.number_input("V2", value=0.0, step=0.1)
v4 = st.sidebar.number_input("V4", value=0.0, step=0.1)
v5 = st.sidebar.number_input("V5", value=0.0, step=0.1)
v7 = st.sidebar.number_input("V7", value=0.0, step=0.1)
v10 = st.sidebar.number_input("V10", value=0.0, step=0.1)
v14 = st.sidebar.number_input("V14", value=0.0, step=0.1)
v17 = st.sidebar.number_input("V17", value=0.0, step=0.1)
v19 = st.sidebar.number_input("V19", value=0.0, step=0.1)
v23 = st.sidebar.number_input("V23", value=0.0, step=0.1)

if st.button("Predict"):
    # Prepare input features as a DataFrame
    features = pd.DataFrame([[time, v2, v4, v5, v7, v10, v14, v17, v19, v23]],
                            columns=["Time", "V2", "V4", "V5", "V7", "V10", "V14", "V17", "V19", "V23"])
    
    # Make prediction
    prediction = model.predict(features)[0]
    
    # Display the result
    result = "Fraudulent Transaction" if prediction == 1 else "Legitimate Transaction"
    st.success(f"Prediction: {result}")


# In[ ]:




