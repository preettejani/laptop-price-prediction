import streamlit as st
import joblib
import pandas as pd

df = pd.read_csv("cleaned_croma_laptops.csv")


st.title(" Laptop Price Prediction App")


models = {

    "Linear Regression": "linear_model.joblib",
    "Ridge Regression": "ridge_model.joblib",
    "Lasso Regression": "lasso_model.joblib",
    "Random Forest": "random_forest_model.joblib",
    "Decision Tree": "decision_model.joblib"

}

model_choice = st.selectbox("Choose a model", list(models.keys()))
model = joblib.load(models[model_choice])

brand = st.selectbox("Brand", df["Brand"].dropna().unique())
ram = st.selectbox("RAM (GB)", df["RAM"].dropna().unique())
storage = st.number_input("Storage (GB)", min_value=128, max_value=2000, step=128, value=512)
cpu = st.selectbox("CPU", ["Apple","Intel i3", "Intel i5", "Intel i7", "Intel i9", "Ryzen 3", "Ryzen 5", "Ryzen 7", "Other"])
gpu = st.selectbox("GPU", ["Integrated", "NVIDIA", "AMD", "Other"])
color = st.selectbox("Color", df["Color"].dropna().unique())
screen_size = st.selectbox("Screen Size (inches)", df["Screen Size"].dropna().unique())

input_data = pd.DataFrame([{

    "Brand": brand,
    "Screen Size": screen_size,
    "RAM": ram,
    "Storage": storage,
    "Color": color,
    "CPU": cpu,
    "GPU": gpu

}])


if st.button("Pridict price"):
    predicted_price = model.predict(input_data)[0]
    st.success(f"Laptop Price: ₹{predicted_price:,.2f}")