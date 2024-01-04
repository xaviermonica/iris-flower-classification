import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("Iris_RF.pkl")

def predict_page():
    st.title("Iris Species Prediction")

    st.sidebar.header("Input Features")

    def user_input_features():
        SepalLengthCm = st.sidebar.slider("Sepal Length (cm)", 4.0, 8.0, 5.1)
        SepalWidthCm = st.sidebar.slider("Sepal Width (cm)", 2.0, 5.0, 3.5)
        PetalLengthCm = st.sidebar.slider("Petal Length (cm)", 1.0, 7.0, 1.4)
        PetalWidthCm = st.sidebar.slider("Petal Width (cm)", 0.1, 2.5, 0.2)

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
    st.subheader('User Input Features')
    st.write(input_df)

    # Make prediction
    prediction = model.predict(input_df)
    prediction_proba = model.predict_proba(input_df)

    st.write(f'Prediction: {prediction}')
    st.write(f'Classes: {model.classes_}')

    species_map = {0: 'Iris-setosa', 1: 'Iris-versicolor', 2: 'Iris-virginica'}

    # Display prediction probabilities
    st.subheader('Prediction Probabilities')
    prob_df = pd.DataFrame(prediction_proba, columns=species_map.values())
    st.write(prob_df)
