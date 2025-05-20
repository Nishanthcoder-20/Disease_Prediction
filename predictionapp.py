import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import streamlit as st
import pickle
from streamlit_option_menu import option_menu

with st.sidebar:
     selected = option_menu('Multiple Disease Prediction System',
                         ['Diabetes Prediction',
                                  'Heart Disease Prediction',
                                  'Parkinsons Prediction'],
                                 icons=['activity', 'heart', 'person'],
                                default_index=0)
if selected == "Diabetes Prediction":
     st.header("Diabetes prediction system")
     st.write("Choose parameters")
     one = st.text_input("Pregnancies")
     two = st.text_input("Glucose")
     three = st.text_input("Bloodpressure")
     four = st.text_input("Skinthickness")
     five = st.text_input("Insulin")
     six = st.text_input("BMI")
     seven = st.text_input("DiabetesPedigreeFunction")
     eight = st.text_input("Age")
     model = pickle.load(open("model.diab.pkl", "rb"))
     features = pd.DataFrame({
         "Pregnancies":one,
         "Glucose":two,
         "BloodPressure":three,
         "SkinThickness":four,
         "Insulin":five,
        "BMI":six,
        "DiabetesPedigreeFunction": seven,
        "Age":eight
     },index=[0])
     diab_diagnosis = ' '
     if st.button("Predict"):
         predictor = model.predict(features)
         if predictor[0] == 1:
             diab_diagnosis = "You have Diabetes. Please consult a doctor. "
         else:
             diab_diagnosis = "You don't have Diabetes. Free to Fly"
     st.success(diab_diagnosis)
