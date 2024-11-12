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
                background-color: black;
            }

            /* Center-align and style the title */
            .title {
                text-align: center;
                font-size: 3.5em;  /* Larger font size for title */
                font-weight: bold;
                color: #4866fa;
                margin-top: 30px;
                margin-bottom: 70px;
            }

            /* Center-align and increase font size for description */
            .description {
                text-align: left;
                color: #e7e9f7;
                margin: 20px auto;
                line-height: 1.5;
                max-width: 900px;
                background-color: rgba(0, 0, 0, 0.6);  /* Semi-transparent background for readability */
                padding: 20px;
                border-radius: 10px;
            }

            /* Increase font size for items under Key Features */
            .description p {
                font-size: 1.2rem;
            }
            .description ul, .description ul li {
                font-size: 1.2rem;  /* Increase font size of list items */
            }

            /* Add height to image container */
            .image-container {
                height: 50vh;
                overflow: hidden;
                display: flex;
                justify-content: center;
                align-items: center;
            }

            /* Apply styling to the image to ensure it covers the container height */
            .image-container img {
                height: 60vh;
                object-fit: cover;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Display title with the custom class for styling
    st.markdown('<div class="title">About the platform </div>', unsafe_allow_html=True)

    # Set up layout with columns for description and image
    col1, col2 = st.columns([1.3, 1])

    # Add description in the left column
    with col1:
        st.markdown(
            """
            <div class="description">
                <p style="font-size: 2rem">Key features</p>
                <ul>
                    <li><b style="color:#4866fa">Dataset Analysis</b>: Gain insights into class distributions and dataset characteristics.</li>
                    <li><b style="color:#4866fa">Classification</b>: Use a Random Forest classifier to detect potential fraud transactions.</li>
                    <li><b style="color:#4866fa">Manual Input</b>: Enter transaction details to check fraud predictions in real-time.</li>
                </ul>
                <p>
                    The dataset undergoes preprocessing using SMOTE for balanced class distribution, and all features are standardized for optimized model performance.
                </p>
                
            </div>
            """,
            unsafe_allow_html=True
        )

    # Add an image in the right column, wrapped in a custom container
    with col2:
        st.markdown(
            """
            <div class="image-container">
                <img src="https://chargebacks911.com/wp-content/uploads/2023/04/Detecting-Credit-Card-Fraud-blog.jpg" alt="Fraud Detection Image">
            </div>
            """,
            unsafe_allow_html=True
        )

show()
