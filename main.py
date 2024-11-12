
import streamlit as st

# Set the page configuration (must be the first Streamlit command)
st.set_page_config(page_title="Credit Card Fraud Detection", layout="wide", initial_sidebar_state="collapsed")

# Custom HTML for Top Navbar
st.markdown("""
    <style>
        .css-18e3th9 {display: none;}  /* Hide default Streamlit sidebar */
        .css-1d391kg {margin-top: -20px;}  /* Remove default spacing */
        .top-nav { 
            display: flex; 
            justify-content: space-evenly; 
            background-color: black; 
            padding: 10px; 
            border-bottom: 1px solid #ccc; 
            position: sticky;
            top: 0;
            z-index: 10;
        }
        .top-nav a {
            text-decoration: none;
            font-weight: bold;
            color: #333;
        }
        .css-1d391kg {margin-top: -10px;}
    </style>
    
""", unsafe_allow_html=True)

# Import other pages after the set_page_config cal
import home
import about
import dataset_analysis
import classification
import manual_input 


# Custom sidebar navigation (remove sidebar by using 'radio' in top navbar)
st.sidebar.title("Navigation")
page = st.selectbox("", ["Home","About", "Dataset Analysis", "Classification", "Manual Input"])

# Display the selected page content
if page == "Home":
    home.show()
elif page == "About":
    about.show()
elif page == "Dataset Analysis":
    dataset_analysis.show()
elif page == "Classification":
    classification.show()
elif page == "Manual Input":
    manual_input.show()  # Correctly call the 'show' function from manual_input.py
