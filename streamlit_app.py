import streamlit as st
import requests

st.set_page_config(page_title="Bank Churn Predictor", page_icon="🏦", layout="centered")
st.title("Bank Customer Churn Predictor")
st.markdown("Enter customer details to predict if they will leave the bank.")
st.divider()

col1, col2 = st.columns(2)

with col1:
    credit_score = st.number_input("Credit Score", min_value=300, max_value=850, value=600)
    age = st.number_input("Age", min_value=18, max_value=100, value=45)
    tenure = st.number_input("Tenure (years)", min_value=0, max_value=10, value=3)
    balance = st.number_input("Balance ($)", min_value=0.0, max_value=300000.0, value=120000.0)
    num_products = st.selectbox("Number of Products", options=[1, 2, 3, 4])

with col2:
    has_cr_card = st.selectbox("Has Credit Card", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
    is_active = st.selectbox("Is Active Member", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
    salary = st.number_input("Estimated Salary ($)", min_value=0.0, max_value=300000.0, value=80000.0)
    geography = st.selectbox("Geography", options=["France", "Germany", "Spain"])
    gender = st.selectbox("Gender", options=["Female", "Male"])

st.divider()

# Convert geography and gender to encoded values
geo_germany = 1 if geography == "Germany" else 0
geo_spain = 1 if geography == "Spain" else 0
gender_male = 1 if gender == "Male" else 0

if st.button("🔍 Predict Churn", use_container_width=True, type="primary"):
    payload = {
        "CreditScore": credit_score,
        "Age": age,
        "Tenure": tenure,
        "Balance": balance,
        "NumOfProducts": num_products,
        "HasCrCard": has_cr_card,
        "IsActiveMember": is_active,
        "EstimatedSalary": salary,
        "Geography_Germany": geo_germany,
        "Geography_Spain": geo_spain,
        "Gender_Male": gender_male
    }

    try:
        response = requests.post("http://127.0.0.1:8002/predict", json=payload)
        result = response.json()

        if result["prediction"] == 1:
            st.error(f"**{result['result']}**")
        else:
            st.success(f"**{result['result']}**")

        st.metric(label="Churn Probability", value=f"{result['churn_probability']}%")
        st.caption("⚠️ This tool is for educational purposes only.")

    except Exception as e:
        st.error(f"Could not connect to API. Make sure uvicorn is running!\n\n{e}")