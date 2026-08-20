import joblib
import streamlit as st
import numpy as np

# load the dataset
mod=joblib.load('Linear Regression_model.pkl')

st.title('Salary Prediction App')
st.write('Enter your years of experience to predict salary')

# input fields
YearsExperience=st.number_input('Years of Experience',min_value=1.0,max_value=50.0,value=2.0)

if st.button("Predict Salary"):
    prediction=mod.predict([[YearsExperience]])
    st.success(f"Predicted Salary: {prediction[0]:,.2f}")