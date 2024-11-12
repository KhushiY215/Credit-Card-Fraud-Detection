import streamlit as st

def show():
    # Set up custom CSS styling with Google Fonts
    st.markdown(
        """
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;700&display=swap" rel="stylesheet">
        <style>
            /* Apply Poppins font to the entire page */
            * {
                font-family: 'Poppins', sans-serif;
                background-color:black;
            }

            /* Center-align and style the title */
            .title {
                text-align: center;
                font-size: 3.5em;  /* Larger font size for title */
                font-weight: bold;
                color: #4866fa;
                margin-top: 30px;
                margin-bottom:70px;
            }

            /* Center-align and increase font size for description */
            .description {
                text-align: left;
                font-size: 2rem;  /* Adjusted font size for description */
                color: #e7e9f7;
                margin: 20px auto;
                line-height: 1.8;
                max-width: 1000px;
                background-color: rgba(0, 0, 0, 0.6);  /* Semi-transparent background for readability */
                padding: 20px;
                border-radius: 10px;
            }

            /* Add height to image container */
            .image-container {
                height: 50vh;  /* 100% viewport height */
                overflow: hidden;
                display: flex;
                justify-content: center;
                align-items: center;
            }

            /* Apply styling to the image to ensure it covers the container height */
            .image-container img {
                height: 100%;
                object-fit: cover;  /* Ensures the image covers the container */
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Display title with the custom class for styling
    st.markdown('<div class="title">Credit Card Fraud Detection</div>', unsafe_allow_html=True)

    # Set up layout with columns for description and image
    col1, col2 = st.columns([1.3, 1])  # Wider column for text, narrower for the image

    # Add description in the left column
    with col2:
        st.markdown(
            """
            <div class="description">
                <p style="font-size: 2rem">
                Welcome to the <b style="color:#4866fa"> Web App</b>! </p>
               <p style="font-size: 1.2rem"> This application leverages a powerful machine learning 
                model to help identify potential fraudulent credit card transactions in real time. Designed with user accessibility 
                in mind, it assists users, analysts, and developers in detecting fraudulent activity effectively.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Add an image in the right column, wrapped in a custom container
    with col1:
        st.markdown(
            """
            <div class="image-container">
                <img src="https://wallpapercave.com/wp/wp2691560.jpg" alt="Fraud Detection Image">
            </div>
            """,
            unsafe_allow_html=True
        )

show()
