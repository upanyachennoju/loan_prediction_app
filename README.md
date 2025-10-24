# 🏦 Loan Prediction App

A Machine Learning-based web application built with Streamlit that predicts whether a loan application will be approved or not based on applicant details such as income, employment status, CIBIL score, and other financial indicators.

## Live Demo: [Click here to try the app](https://loan-prediction-upanyach.streamlit.app/)

## 📘 Overview

The Loan Prediction App uses a trained Random Forest model to classify loan applications as Approved or Rejected.  
It provides a simple and interactive interface for users to input financial and personal details and receive instant predictions.

## 🧩 Dataset Description

The dataset used is a collection of financial and demographic records related to loan applications.  
The loan approval dataset is a collection of financial records and associated information used to 
determine the eligibility of individuals or organizations for obtaining loans from a lending institution. 
It includes various factors such as cibil score, income, employment status, loan term, loan amount, assets value, and loan status. 
This dataset is commonly used in machine learning and data analysis to develop models and algorithms that predict 
the likelihood of loan approval based on the given features.

## 🚀 How to Run the App

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/Loan-Prediction-App.git
cd Loan-Prediction-App
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Streamlit App
```bash
streamlit run app.py
```

Then open the local URL (usually http://localhost:8501/) in your browser.

## 🧠 Model Details

- Algorithm Used: Random Forest Classifier  
- Framework: Scikit-learn  
- Pipeline: Includes preprocessing (encoding, scaling) and classification steps  
- Output: Binary prediction — Loan Approved or Rejected  

## 📊 Tech Stack

- Python
- Streamlit
- Scikit-learn
- Pandas, NumPy
- Matplotlib, Seaborn
- Joblib

## 🧑‍💻 Author

Upanya Chennoju  
Project: Loan Prediction App – Streamlit  

## 📜 License

This project is open-source and available under the MIT License.
