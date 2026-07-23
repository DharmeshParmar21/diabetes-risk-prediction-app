import streamlit as st
import numpy as np
import pickle
import os

# -----------------------
# Page Configuration
# -----------------------
st.set_page_config(
    page_title="Diabetes Prediction App",
    page_icon="🩺",
    layout="centered"
)

# -----------------------
# File Paths
# -----------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "models", "model.pkl")
SCALER_PATH = os.path.join(BASE_DIR, "models", "scaler.pkl")

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

with open(SCALER_PATH, "rb") as f:
    scaler = pickle.load(f)

# -----------------------
# App UI
# -----------------------
st.title("🩺 Diabetes Prediction App")
st.write("Enter patient details below")

preg = st.number_input("Pregnancies", 0, 20, 1)
glucose = st.number_input("Glucose", 0, 250, 120)
bp = st.number_input("Blood Pressure", 0, 150, 70)
skin = st.number_input("Skin Thickness", 0, 100, 20)
insulin = st.number_input("Insulin", 0, 900, 80)
bmi = st.number_input("BMI", 0.0, 70.0, 25.0)
dpf = st.number_input("Diabetes Pedigree Function", 0.0, 3.0, 0.50)
age = st.number_input("Age", 1, 120, 30)

if st.button("Predict"):

    data = np.array([
        [preg, glucose, bp, skin, insulin, bmi, dpf, age]
    ])

    data = scaler.transform(data)

    probability = model.predict_proba(data)[0][1]

    st.subheader("Prediction Result")

    st.write(f"Diabetes Probability: **{probability:.2%}**")

    if probability >= 0.5:
        st.error("⚠️ High Risk of Diabetes")
    else:
        st.success("✅ Low Risk of Diabetes")