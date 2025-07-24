import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import streamlit as st
import pickle
from streamlit_option_menu import option_menu

with st.sidebar:
     selected = option_menu('Disease Prediction System',
                             ['Diabetes Prediction','Heart Disease Prediction'],
                             icons=['activity'],
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

if selected == "Heart Disease Prediction":
     st.header("Heart Disease Prediction system")
     st.write("Choose parameters")
     one = st.text_input("age")
     two = st.text_input("sex")
     three = st.text_input("Chest Pain types [0 = Typical angina, 1 = Atypical angina, 2 = Non-anginal pain, 3 = Asymptomatic]")
     four = st.text_input("Resting Blood Pressure in mmHg")
     five = st.text_input("Serum Cholesterol in mg/dl")
     six = st.text_input("Fasting Blood Sugar > 120 mg/dl [1 = True, 0 = False]")
     seven = st.text_input('Resting Electrocardiographic results [0 = Normal, 1 = ST-T wave abnormality, 2 = Left ventricular hypertrophy]')
     eight = st.text_input("Maximum Heart Rate achieved")
     nine = st.text_input("Exercise Induced Angina [1 = Yes, 0 = No]")
     ten = st.text_input("ST depression induced by exercise")
     eleven = st.text_input("Slope of the peak exercise ST segment [0 = Upsloping, 1 = Flat, 2 = Downsloping]")
     twelve = st.text_input("Major vessels colored by flourosopy")
     thirteen = st.text_input("thal: 0 = normal; 1 = fixed defect; 2 = reversable defect")
     model = pickle.load(open("model.heart.pkl", "rb"))
     features = pd.DataFrame({
         "age": one,
         "sex": two,
         "cp": three,
         "trestbps": four,
         "chol": five,
         "fbs": six,
         "restecg": seven,
         "thalach" :eight,
         "exang": nine,
         "oldpeak": ten,
         "slope": eleven,
         "ca": twelve,
         "thal": thirteen
     },index=[0])
     heart_diagnosis = ''
     if st.button("predict"):
         predictor = model.predict(features)
         if predictor [0]==1:
            heart_diagnosis = 'The person is having heart disease!'
         else:
            heart_diagnosis = 'The person does not have any heart disease'
     st.success(heart_diagnosis)
