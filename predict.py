# predict.py

import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("Iris_RF.pkl")

def predict_page():
    # Set the page title and layout
    st.title("🌺 **Iris Species Prediction** 🌺")

    # Sidebar header
    st.sidebar.header("🔧 **Input Features**")

    def user_input_features():
        # Slider inputs for feature selection with custom styling
        SepalLengthCm = st.sidebar.slider("Sepal Length (cm)", 4.0, 8.0, 5.1, format="%.1f")
        SepalWidthCm = st.sidebar.slider("Sepal Width (cm)", 2.0, 5.0, 3.5, format="%.1f")
        PetalLengthCm = st.sidebar.slider("Petal Length (cm)", 1.0, 7.0, 1.4, format="%.1f")
        PetalWidthCm = st.sidebar.slider("Petal Width (cm)", 0.1, 2.5, 0.2, format="%.1f")

        # Create a DataFrame with the input features
        data = {
            'SepalLengthCm': SepalLengthCm,
            'SepalWidthCm': SepalWidthCm,
            'PetalLengthCm': PetalLengthCm,
            'PetalWidthCm': PetalWidthCm
        }

        features = pd.DataFrame(data, index=[0])
        return features

    # Get user input
    input_df = user_input_features()

    # Display user input with refined styling
    st.subheader('🔢 **User Input Features**')
    st.write(input_df)

    # Make prediction
    prediction = model.predict(input_df)
    prediction_proba = model.predict_proba(input_df)

    # Display the prediction and classes
    st.subheader('🌟 **Prediction**')
    st.markdown(f'**Predicted Species:** _{prediction[0]}_')
    st.write(f'**Classes:** {model.classes_}')

    # Map predictions to class names
    species_map = {0: 'Iris-setosa', 1: 'Iris-versicolor', 2: 'Iris-virginica'}

    # Display prediction probabilities with formatted styling
    st.subheader('🔍 **Prediction Probabilities**')
    # Create a DataFrame for probabilities
    prob_df = pd.DataFrame(prediction_proba, columns=species_map.values())

    # Style DataFrame
    st.write(
        prob_df.style
        .background_gradient(cmap='coolwarm')  # Updated color map
        .highlight_max(axis=1, color='lightgreen')  # Highlight max values in light green
        .set_properties(**{'border': '1px solid black'})  # Add border to DataFrame
    )
    # Add a visual flair with a closing message
    st.markdown(
        """
        <div style="font-size:18px; color:#4682B4; padding:10px; border:2px solid #4682B4; border-radius:8px;">
        🌟 **Thank you for using our Iris Species Prediction tool!** 🌟<br>
        Explore different features using the sidebar to enhance your experience.
        </div>
        """,
        unsafe_allow_html=True
    )
