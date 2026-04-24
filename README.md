# 🩺 Diabetes Risk Prediction App

## 📌 Overview
This project predicts whether a person is diabetic based on medical attributes using Machine Learning.  
It includes EDA, model building, evaluation, and a deployed Streamlit app.

---

## 📑 Table of Contents
- [📸 App Preview](#app-preview)
- [📊 Key Insights](#key-insights)
- [🤖 Model Performance](#model-performance)
- [🎯 Features](#features)
- [⚙️ Tech Stack](#tech-stack)
- [▶️ How to Run](#how-to-run)
- [🌐 Live App](#live-app)
- [📁 Project Structure](#project-structure)
- [⚠️ Disclaimer](#disclaimer)
- [🙌 Author](#author)

---

## 📸 App Preview

![App Result](images/app_result.png)

Insight:  
The application takes user input and predicts diabetes probability along with classification output.

---

## 📊 Key Insights

### 🔥 Glucose vs Outcome
![Glucose vs Outcome](images/glucose_vs_outcome.png)

Insight:  
Diabetic patients have significantly higher glucose levels, making glucose the strongest predictor.

---

### 📈 Correlation Heatmap
![Correlation Heatmap](images/correlation_heatmap.png)

Insight:  
Glucose shows the highest correlation with outcome, followed by BMI and Age.

---

## 🤖 Model Performance

Metric | Value  
-------|--------
Accuracy | ~0.75  
ROC-AUC | ~0.82  
Recall | ~0.72  

Insight:  
Model shows strong class separation and improved recall to reduce missed diabetic cases.

---

## 🎯 Features

- Exploratory Data Analysis (EDA)
- Multiple model comparison
- ROC-AUC evaluation
- Threshold tuning
- Streamlit web app

---

## ⚙️ Tech Stack

- Python  
- Pandas, NumPy  
- Scikit-learn  
- Matplotlib, Seaborn  
- Streamlit  

---

## ▶️ How to Run

git clone https://github.com/your-username/diabetes-risk-prediction-app.git  
cd diabetes-risk-prediction-app  

pip install -r requirements.txt  
streamlit run app.py  

---

## 🌐 Live App

👉 https://your-streamlit-link.streamlit.app

---

## 📁 Project Structure

Diabetes-Prediction/  
│  
├── images/  
│   ├── app_result.png  
│   ├── correlation_heatmap.png  
│   ├── glucose_vs_outcome.png  
│  
├── models/  
│   ├── model.pkl  
│   ├── scaler.pkl  
│  
├── app.py  
├── notebook.ipynb  
├── requirements.txt  
└── README.md  

---

## ⚠️ Disclaimer

This project is for educational purposes only and not a medical diagnosis tool.

---

## 🙌 Author

Your Name
