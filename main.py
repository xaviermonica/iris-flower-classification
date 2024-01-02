import streamlit as st
from visualize import visualize_page
from analyze import analyze_page
from predict import predict_page
from about import about_page
from feedback import feedback_page

# Sidebar Navigation
st.sidebar.title("Navigation")
options = st.sidebar.radio("Go to", ["Home", "Visualize", "Analyze", "Predict", "About", "Feedback"])

# Navigation logic
if options == "Home":
    st.title("Welcome to the Iris Species Prediction App!")
    st.write("""
        This app allows you to predict the species of an Iris flower based on its sepal and petal measurements. 
        Use the navigation bar to explore the features of the app.
    """)
elif options == "Visualize":
    visualize_page()
elif options == "Analyze":
    analyze_page()
elif options == "Predict":
    predict_page()
elif options == "About":
    about_page()
elif options == "Feedback":
    feedback_page()
