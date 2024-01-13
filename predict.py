# predict.py

import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("Iris_RF.pkl")

def predict_page():
    # Set page title and layout
    st.title("🌸 Iris Species Prediction 🌸")

    # Sidebar header
    st.sidebar.header("🔍 Input Features")

    def user_input_features():
        # Slider inputs for feature selection
        SepalLengthCm = st.sidebar.slider("Sepal Length (cm)", 4.0, 8.0, 5.1)
        SepalWidthCm = st.sidebar.slider("Sepal Width (cm)", 2.0, 5.0, 3.5)
        PetalLengthCm = st.sidebar.slider("Petal Length (cm)", 1.0, 7.0, 1.4)
        PetalWidthCm = st.sidebar.slider("Petal Width (cm)", 0.1, 2.5, 0.2)

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

    # Display user input
    st.subheader('🔢 User Input Features')
    st.write(input_df)

    # Make prediction
    prediction = model.predict(input_df)
    prediction_proba = model.predict_proba(input_df)

    # Display the prediction and classes
    st.subheader('🌟 Prediction')
    st.write(f'**Predicted Species:** {prediction[0]}')
    st.write(f'**Classes:** {model.classes_}')

    # Map predictions to class names
    species_map = {0: 'Iris-setosa', 1: 'Iris-versicolor', 2: 'Iris-virginica'}

    # Display prediction probabilities
    st.subheader('🔍 Prediction Probabilities')
    prob_df = pd.DataFrame(prediction_proba, columns=species_map.values())
    st.write(prob_df)

    # Add a little more flair with a closing message
    st.markdown(
        """
        <div style="font-size:16px; color:#4682B4;">
        Thank you for using our Iris Species Prediction tool! 🌷
        </div>
        """,
        unsafe_allow_html=True
    )
