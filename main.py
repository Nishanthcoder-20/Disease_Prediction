from email.policy import default
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import streamlit as st
import pickle
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu("Diabetes Prediction",

                           ['Diabetes prediction'],
                           icons=['Activity'],
                           default_index=0)
if selected =="Diabetes Prediction":
    st.header("Diabetes prediction system")
    st.write("Choose parameters")
    one = st.text_input("Pregnancies")
    two = st.text_input("Glucose")
    three = st.text_input("Blood pressure")
    four = st.text_input("Skin thickness")
    five = st.text_input("Insulin")
    six = st.text_input("BMI")
    seven = st.text_input("Diabetes Pedigree Function")
    eight = st.text_input("Age")
    model = pickle.load(open("model_db.pkl","rb"))
    features = pd.DataFrame({
        "Pregnancies":one,
        "Glucose": two,
        "Blood Pressure": three,
        "SkinThickness": four,
        "Insulin": five,
        "BMI": six,
        "DiabetesPedigreeFunction": seven,
        "Age":eight
    }, index = [0])
    diab_diagnosis = ''
    if st.button("predict"):
        predictor = model.predict(features)
    if predictor[0]==1:
        diab_diagnosis = 'The person is diabetic'
    else:
        diab_diagnosis = 'The person is not diabetic'
    st.success(diab_diagnosis)