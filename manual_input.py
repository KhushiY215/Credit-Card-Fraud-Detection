import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from imblearn.over_sampling import SMOTE
from joblib import dump, load
import os
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

# Load data with caching
@st.cache_data
def load_data():
    data = pd.read_csv(r"C:\Users\Khushi Yadav\Documents\cfd\data.csv")
    return data.sample(10000)  # Load a sample of 10,000 rows

# Load or Train the Model
MODEL_PATH = "fraud_model.joblib"
SCALER_PATH = "scaler.joblib"

# Check if model and scaler are already saved, otherwise train and save them
if os.path.exists(MODEL_PATH) and os.path.exists(SCALER_PATH):
    model = load(MODEL_PATH)
    scaler = load(SCALER_PATH)
else:
    data = load_data()
    X = data.drop('Class', axis=1)
    y = data['Class']

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

    # Scale the data
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Handle class imbalance with SMOTE
    smote = SMOTE(random_state=42)
    X_train, y_train = smote.fit_resample(X_train, y_train)

    # Train the model
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    # Save the model and scaler
    dump(model, MODEL_PATH)
    dump(scaler, SCALER_PATH)

def show():
    # Custom styling using HTML and CSS
    st.markdown(
        """
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;700&display=swap" rel="stylesheet">
        <style>
            * {
                font-family: 'Poppins', sans-serif;
                background-color: #0e1117;
                color: #e7e9f7;
            }
             .title {
                text-align: center;
                font-size: 3.2em;  /* Larger font size for title */
                font-weight: bold;
                color: #4866fa;
                margin-top: 30px;
                margin-bottom:40px;
            }
            .section-title {
                font-size: 1.5em;
                font-weight: bold;
                color: #5a67f2;
                margin-top: 40px;
                margin-bottom: 15px;
            }
            .metrics {
                color: #d1d4e0;
                background-color: rgba(0, 0, 0, 0.65);
                padding: 15px;
                border-radius: 10px;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
                margin-bottom: 30px;
            }
            .prediction-result {
                font-size: 1.2em;
                font-weight: bold;
                color: #e7e9f7;
                background-color: rgba(0, 0, 0, 0.65);
                padding: 20px;
                border-radius: 10px;
                margin-top: 20px;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Display Model Evaluation
    st.markdown('<div class="title">Model Evaluation</div>', unsafe_allow_html=True)

    # Load data and evaluate model
    data = load_data()
    X = data.drop('Class', axis=1)
    y = data['Class']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
    X_test = scaler.transform(X_test)

    y_pred = model.predict(X_test)

    st.markdown('<div class="section-title">Confusion Matrix</div>', unsafe_allow_html=True)
    st.write(f"<div class='metrics'>{confusion_matrix(y_test, y_pred)}</div>", unsafe_allow_html=True)

    st.markdown('<div class="section-title">Classification Report</div>', unsafe_allow_html=True)
    st.write(f"<div class='metrics'>{classification_report(y_test, y_pred)}</div>", unsafe_allow_html=True)

    # Move to the manual input form for predictions
    st.markdown('<div class="section-title">Predict Fraud</div>', unsafe_allow_html=True)

    # User input for prediction
    time = st.number_input("Time", min_value=float(X['Time'].min()), max_value=float(X['Time'].max()))
    amount = st.number_input("Amount", min_value=0.0, max_value=10000.0, value=100.0)
    
    # Collect user input for other features (V1, V2, ..., V28)
    features = [time, amount] + [st.number_input(f"V{i}", value=0.0) for i in range(1, 29)]
    
    # Add a button for making the prediction
    if st.button("Predict"):
        # Standardize user input
        input_data = scaler.transform([features])
        prediction = model.predict(input_data)
        
        # Display result based on the prediction
        if prediction[0] == 1:
            st.markdown('<div class="prediction-result">The transaction is <span style="color:#ff4b4b;">fraudulent</span>.</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="prediction-result">The transaction is <span style="color:#4caf50;">not fraudulent</span>.</div>', unsafe_allow_html=True)

show()
