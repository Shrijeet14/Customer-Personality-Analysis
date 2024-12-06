import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load the trained model and scaler
loaded_model = pickle.load(open('Output_Model/best_model.pkl', 'rb'))
scaler = pickle.load(open('Output_Model/scaler.pkl', 'rb'))

# Define a function to display predictions and insights
def display_prediction(prediction):
    if prediction == 0:
        st.write("### Prediction: High-income group")
        st.write("""
        - **Average Income**: $69,000
        - **Average Age**: 46 years
        - **Education Level**: Mostly graduates
        - **Family Composition**: Families with offspring; mostly couples and single people
        - **Purchase Behavior**: Higher purchase frequency and volume
        - **Campaign Response**: Responds to campaigns
        - **Average Transaction Time**: 18 days
        """)
    else:
        st.write("### Prediction: Low-income group")
        st.write("""
        - **Average Income**: $37,000 (lower than cluster 0)
        - **Average Age**: 42 years
        - **Education Level**: Graduates, Masters, PhD
        - **Purchase Behavior**: Lower frequency of purchases and lower expenditure
        - **Average Transaction Time**: 42 days (longer time between purchases)
        - **Loyalty**: Not as loyal or profitable for the company
        """)

# Streamlit interface
st.set_page_config(page_title="Customer Segmentation Prediction", page_icon="💼")
st.title("Customer Segmentation Prediction")
st.markdown("""
Welcome to the **Customer Segmentation Prediction** tool! 
This app predicts customer groups based on certain features like income, education, and purchase behavior.
""")

# Input form for new data on the main page
st.header("Input New Data")

age = st.number_input("Age", min_value=18, max_value=100, value=25)
education = st.selectbox("Education Level", options=["High School", "Undergraduate", "Graduate", "Postgraduate", "PhD"], index=2)
members = st.number_input("Family Members", min_value=1, max_value=10, value=2)
income = st.number_input("Income ($)", min_value=1000, max_value=200000, value=56000)
last_purchase = st.number_input("Last Purchase Amount ($)", min_value=1, max_value=10000, value=300)
enrollment_duration = st.number_input("Enrollment Duration (days)", min_value=1, max_value=365, value=30)
campaign_acceptance = st.selectbox("Campaign Acceptance", options=["Accepted", "Not Accepted"], index=0)
average_days = st.number_input("Average Days Between Purchases", min_value=1, max_value=100, value=20)
average_expenditure = st.number_input("Average Expenditure ($)", min_value=1, max_value=500, value=15)
num_transactions = st.number_input("Number of Transactions", min_value=1, max_value=100, value=15)
total_expenditure = st.number_input("Total Expenditure ($)", min_value=1, max_value=5000, value=350)
complain = st.selectbox("Complaint Status", options=["No", "Yes"], index=0)

# Convert input data to DataFrame
new_data = pd.DataFrame({
    "Age": [age],
    "Education": [["High School", "Undergraduate", "Graduate", "Postgraduate", "PhD"].index(education)],
    "Members": [members],
    "Income": [income],
    "Last_Purchase": [last_purchase],
    "Enrollment_Duration": [enrollment_duration],
    "Campaign_Acceptance": [1 if campaign_acceptance == "Accepted" else 0],
    "Average_Days": [average_days],
    "Average_Expenditure": [average_expenditure],
    "Num_of_Transactions": [num_transactions],
    "Total_Expenditure": [total_expenditure],
    "Complain": [1 if complain == "Yes" else 0]
})

# Normalize the new data using the scaler
new_data = scaler.transform(new_data)

# Prediction button
if st.button("Predict Customer Segment"):
    # Prediction
    new_prediction = loaded_model.predict(new_data)

    # Display the result
    st.subheader("Prediction Result")
    display_prediction(new_prediction[0])

# Additional design elements
st.markdown("""
<div style="background-color:#f4f4f4;padding:20px;margin-top:30px;text-align:center;">
    <p style="font-size:14px;color:gray;">Customer Segmentation Prediction App</p>
</div>
""", unsafe_allow_html=True)
