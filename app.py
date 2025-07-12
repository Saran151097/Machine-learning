import streamlit as st
import pickle
import numpy as np

# Load model
with open('linear_reg.pkl', 'rb') as file:
    model = pickle.load(file)

# UI
st.title("💼 Salary Predictor")
experience = st.number_input("Years of Experience", 0.0, 50.0, step=0.1)

if st.button("Predict Salary"):
    salary = model.predict(np.array([[experience]]))
    st.success(f"Predicted Salary: ₹{salary[0]:.2f} Lakhs/year")

