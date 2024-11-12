import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from imblearn.over_sampling import SMOTE
from joblib import dump, load
import os

@st.cache_data
def load_data():
    data = pd.read_csv(r"C:\Users\Khushi Yadav\Documents\cfd\data.csv")
    return data.sample(10000)

@st.cache_resource
def train_model():
    data = load_data()
    X = data.drop('Class', axis=1)
    y = data['Class']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
    
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    smote = SMOTE(random_state=42)
    X_train, y_train = smote.fit_resample(X_train, y_train)

    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    
    # Save the model and scaler
    dump(model, 'fraud_detection_model.joblib')
    dump(scaler, 'scaler.joblib')
    
    return model, scaler

model, scaler = train_model()

def show():
    # Custom CSS styling with Google Fonts and background
    st.markdown(
        """
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;700&display=swap" rel="stylesheet">
        <style>
            * {
                font-family: 'Poppins', sans-serif;
            }

            /* Center-align and style the title */
            .title {
                text-align: center;
                font-size: 3.5em;
                font-weight: bold;
                color: #4866fa;
                margin-top: 30px;
                margin-bottom:50px;
            }

            /* Styling for subheadings (changing color to blue like the title) */
            .subheading {
                font-size: 1.75em;
                font-weight: bold;
                color: #4866fa;  /* Blue color like the title */
                margin-top: 20px;
                text-align: left;
                margin-bottom: 30px;
            }

            /* Styling for section descriptions */
            .section {
                text-align: center;
                font-size: 1.25em;
                color: #e7e9f7;
                margin: 20px auto;
                line-height: 1.8;
                max-width: 1000px;
                background-color: rgba(0, 0, 0, 0.6);  /* Semi-transparent background */
                padding: 20px;
                border-radius: 10px;
            }

            /* Styling for the page layout */
            .plot-container {
                display: flex;
                justify-content: center;
                align-items: center;
                max-width: 60%;  /* Make the plot container take up 60% width */
                margin: 0 auto;  /* Center the plot */
                margin-bottom: 40px;
            }

            /* Styling for buttons */
            .button {
                background-color: #4866fa;
                color: white;
                padding: 10px 20px;
                font-size: 16px;
                border-radius: 5px;
                cursor: pointer;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Display title with custom styling
    st.markdown('<div class="title">Fraud Detection Prediction</div>', unsafe_allow_html=True)

    st.write("Enter details of the transaction to check if it's fraudulent.")

    # Load data and balance it for display
    data = load_data()
    fraud_data = data[data['Class'] == 1]
    non_fraud_data = data[data['Class'] == 0]
    balanced_data = pd.concat([fraud_data, non_fraud_data.sample(len(fraud_data), random_state=42)])

    # Display a select box for sample transactions
    selected_transaction = st.selectbox("Select a transaction:", balanced_data.index)
    transaction_data = balanced_data.loc[selected_transaction].drop("Class")

    # Display the transaction details
    st.markdown('<div class="subheading">Transaction Details</div>', unsafe_allow_html=True)
    st.write(transaction_data)

    # Predict button with custom styling
    if st.button("Predict", key="predict"):
        input_data = scaler.transform([transaction_data])
        prediction = model.predict(input_data)

        # Display prediction result
        st.markdown('<div class="subheading">Prediction Result</div>', unsafe_allow_html=True)
        if prediction[0] == 1:
            st.write("The transaction is **likely fraudulent**.")
        else:
            st.write("The transaction is **likely not fraudulent**.")
