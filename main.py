import streamlit as st
from visualize import visualize_page
from analyze import analyze_page
from predict import predict_page
from about import about_page
from feedback import feedback_page

# Set app theme color using markdown styling
st.markdown("""
    <style>
    .sidebar .sidebar-content {
        background-color: #FFEBF0;
    }
    .main {
        background-color: #FFF3E0;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar Navigation with emojis 🌸
st.sidebar.title("🌼 Navigation")
options = st.sidebar.radio("Go to", ["🏠 Home", "📊 Visualize", "🔍 Analyze", "🤖 Predict", "📚 About", "💬 Feedback"])

# Navigation logic
if options == "🏠 Home":
    st.title("🌸 Welcome to the Iris Species Prediction App! 🌸")
    st.markdown("""
        <div style="font-size:18px;">
        🌷 This app allows you to predict the species of an Iris flower based on its sepal and petal measurements.<br>
        🏵️ Use the navigation bar on the left to explore different features of the app.
        </div>
    """, unsafe_allow_html=True)

elif options == "📊 Visualize":
    st.markdown("<h1 style='color:#ff6347;'>📊 Visualization</h1>", unsafe_allow_html=True)
    visualize_page()

elif options == "🔍 Analyze":
    st.markdown("<h1 style='color:#4682B4;'>🔍 Data Analysis</h1>", unsafe_allow_html=True)
    analyze_page()

elif options == "🤖 Predict":
    st.markdown("<h1 style='color:#32CD32;'>🤖 Iris Species Prediction</h1>", unsafe_allow_html=True)
    predict_page()

elif options == "📚 About":
    st.markdown("<h1 style='color:#FF8C00;'>📚 About the App</h1>", unsafe_allow_html=True)
    about_page()

elif options == "💬 Feedback":
    st.markdown("<h1 style='color:#DA70D6;'>💬 Feedback</h1>", unsafe_allow_html=True)
    feedback_page()
