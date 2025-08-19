import streamlit as st
import pandas as pd
import pickle

with open('rf_pipeline.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("Loan Predictor App")

st.subheader("Enter the features: ")

# loan_id, no_of_dependents, education, self_employed, income_annum, loan_amount, loan_term, cibil_score, 
# residential_assets_value, commercial_assets_value, luxury_assets_value, bank_asset_value

no_of_dependents = st.number_input("Enter Number of dependents: ", min_value=0, max_value=10)
education = st.selectbox("Select educational qualification: ", [' Graduate', ' Not Graduate'])
self_employed = st.selectbox("Employment: ", [' Yes', ' No'])
income_annum = st.number_input("Enter your annual income: ", min_value=0, max_value=100000000)
loan_amount = st.number_input("Enter the loan amount: ", min_value=0, max_value=100000000)
loan_term = st.slider("Choose a loan term: ", min_value=1, max_value=20, value=5)
cibil_score = st.number_input("Enter your cibil score: ", min_value=0, max_value=900)
residential_assets_value = st.number_input("Enter your residential assets value: ", min_value=0, max_value=100000000)
commercial_assets_value = st.number_input("Enter your commercial assets value: ", min_value=0, max_value=100000000)
luxury_assets_value = st.number_input("Enter your luxury assets value: ", min_value=0, max_value=100000000)
bank_asset_value = st.number_input("Enter your bank asset value: ", min_value=0, max_value=100000000)

input_df = pd.DataFrame([[no_of_dependents, education, self_employed, income_annum, loan_amount, loan_term, cibil_score, 
                          residential_assets_value, commercial_assets_value, luxury_assets_value, bank_asset_value]], 
                          columns=['no_of_dependents', 'education', 'self_employed', 'income_annum',
                                'loan_amount', 'loan_term', 'cibil_score', 'residential_assets_value',
                                'commercial_assets_value', 'luxury_assets_value', 'bank_asset_value'])

if st.button("Predict"):
    prediction = model.predict(input_df)
    if prediction[0]==1:
        st.error("Loan is Rejected")
    else:
        st.success("Loan is Approved")


#1,00,00,000