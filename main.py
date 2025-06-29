import streamlit as st
import joblib
model = joblib.load("ml_model.pkl")

st.set_page_config(page_title="Subscription Prediction App", page_icon=":chart_with_upwards_trend:", layout="centered")
st.title("Subscription Prediction App")
st.write("This app predicts whether a user will subscribe to a product or not on the basis of gender, age and estimated salary.")
col1, col2 = st.columns(2)
with col1:
    st.write("Please enter the following details:")
with col2:
    st.write("Model accuracy: **93.75%**")
    st.write("This app is built by [**Uttam Kumar**](https://www.linkedin.com/in/uttam-kumar-88b7a9288/)")
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.number_input("Age", min_value=18, max_value=100)
estimated_salary = st.number_input("Estimated Salary", min_value=0)

if st.button("Predict"):
    with st.spinner("Predicting..."):
        features = [[1 if gender == "Male" else 0, age, estimated_salary]]
        prediction = model.predict(features)
        if prediction[0] == 1 : st.success("Yes, the user will subscribe.") 
        else: st.error("No, the user will not subscribe.")