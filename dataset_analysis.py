import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset with caching
@st.cache_data
def load_data():
    data = pd.read_csv(r"C:\Users\Khushi Yadav\Documents\cfd\data.csv")
    return data.sample(10000)

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
                text-align: center;
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
        </style>
        """,
        unsafe_allow_html=True
    )

    # Display title with custom styling
    st.markdown('<div class="title">Dataset Analysis</div>', unsafe_allow_html=True)

    # Load the dataset
    data = load_data()

# Display summary statistics
    st.subheader("Summary Statistics")
    st.write(data.describe())
    
    # Display class distribution plot
    st.markdown('<div class="subheading">Class Distribution</div>', unsafe_allow_html=True)
    with st.container():  # Wrapping the plot in a container for control
        col1, col2 = st.columns([0.6, 0.4])  # Split the width for better control
        with col1:
            fig, ax = plt.subplots(figsize=(6, 4))  # Adjusted figure size
            sns.countplot(x='Class', data=data, ax=ax, palette="viridis")
            ax.set_title("Class Distribution", fontsize=14, color="teal")  # Custom color
            ax.set_xlabel('Class', fontsize=12)
            ax.set_ylabel('Count', fontsize=12)
            st.pyplot(fig)

    

    # Display correlation heatmap plot
    st.markdown('<div class="subheading">Correlation Heatmap</div>', unsafe_allow_html=True)
    with st.container():  # Wrapping the plot in a container for control
        col1, col2 = st.columns([0.6, 0.4])  # Split the width for better control
        with col1:
            correlation_matrix = data.corr()
            fig, ax = plt.subplots(figsize=(8, 6))  # Adjusted figure size
            sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', ax=ax, cbar_kws={'label': 'Correlation Coefficient'})
            ax.set_title('Correlation Heatmap', fontsize=14, color="orange")  # Custom color
            st.pyplot(fig)

    # Display Pairplot for visualizing relationships between features
    st.markdown('<div class="subheading">Pairplot</div>', unsafe_allow_html=True)
    st.write("Pairplot to visualize relationships between features:")
    with st.container():
        col1, col2 = st.columns([0.6, 0.4])  # Split the width for better control
        with col1:
            fig = sns.pairplot(data[['V1', 'V2', 'V3', 'V4', 'V5', 'Class']], hue='Class', palette="coolwarm", height=2)  # Reduced size of pairplot
            fig.fig.suptitle('Pairplot of Features', fontsize=16, color="green")  # Custom color
            st.pyplot(fig)

    # Boxplot for checking outliers in 'Amount'
    st.markdown('<div class="subheading">Boxplot for Amount Distribution</div>', unsafe_allow_html=True)
    with st.container():
        col1, col2 = st.columns([0.6, 0.4])  # Split the width for better control
        with col1:
            fig, ax = plt.subplots(figsize=(6, 4))  # Adjusted size
            sns.boxplot(x='Class', y='Amount', data=data, ax=ax, palette="Set2")
            ax.set_title("Boxplot: Amount Distribution by Class", fontsize=14, color="purple")  # Custom color
            ax.set_xlabel('Class', fontsize=12)
            ax.set_ylabel('Amount', fontsize=12)
            st.pyplot(fig)

    # Distribution plot for 'Amount'
    st.markdown('<div class="subheading">Amount Distribution</div>', unsafe_allow_html=True)
    with st.container():
        col1, col2 = st.columns([0.6, 0.4])  # Split the width for better control
        with col1:
            fig, ax = plt.subplots(figsize=(6, 4))  # Adjusted size
            sns.histplot(data['Amount'], kde=True, ax=ax, color="purple", bins=30)
            ax.set_title("Amount Distribution", fontsize=14, color="brown")  # Custom color
            ax.set_xlabel('Amount', fontsize=12)
            ax.set_ylabel('Frequency', fontsize=12)
            st.pyplot(fig)
