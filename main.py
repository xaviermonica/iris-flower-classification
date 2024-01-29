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
        background-color: #000000;
    }
    </style>
    """, unsafe_allow_html=True)

import streamlit as st

# Set the page title and icon using HTML
st.markdown("""
    <title>Iris Species Prediction App</title>
    <link rel="icon" href="iris1.jpg" type="image/jpg">
""", unsafe_allow_html=True)


st.sidebar.image("iris4.jpg", use_column_width=True)

# Sidebar Navigation with emojis 🌸 using Selectbox
st.sidebar.title("🌼 Navigation")

# Define the options for the selectbox
selectbox_options = ["🏠 Home", "📊 Visualize", "🔍 Analyze", "🤖 Predict", "📚 About", "💬 Feedback"]

# Sidebar selectbox for navigation (scrollable)
options = st.sidebar.selectbox(
    "Navigate to:",
    options=selectbox_options
)

# Navigation logic based on selectbox value
if options == "🏠 Home":
    # Professional Title with Gradient and Center Alignment
    st.markdown(
        """
        <h1 style='text-align: center;
        background: linear-gradient(90deg, #ff69b4, #8a2be2);
        -webkit-background-clip: text;
        color: transparent;
        font-size: 3rem;
        font-weight: bold;'>
        🌸 Welcome to the Iris Species Prediction App! 🌸
        </h1>
        """, 
        unsafe_allow_html=True
    )
    
    # Container for the introductory text
    st.markdown(
        """
        <div style="
        background-color: #eddada; 
        padding: 40px;
        border-radius: 15px;
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
        font-size: 1.2rem;
        line-height: 1.6;
        color: #2c3e50;
        text-align: justify;">
        
        <p style="text-indent: 40px; margin-bottom: 20px;">
            🌷 <strong>Iris Species Prediction App</strong> is designed to help you predict the species of an Iris flower 
            by entering its sepal and petal measurements. With a simple and intuitive interface, this app leverages 
            machine learning to provide accurate predictions.
        </p>
        
        <p style="text-indent: 40px; margin-bottom: 20px;">
            🏵️ Use the <strong>navigation menu</strong> on the left to explore various features. You can visualize key 
            insights from the dataset, analyze important data trends, predict the species of an Iris flower, and learn 
            more about how the app works.
        </p>
        
        <p style="text-indent: 40px; margin-bottom: 20px;">
            📊 The app offers interactive charts, professional analysis tools, and a smooth experience for exploring data 
            with modern design elements.
        </p>

        <div style="text-align: center; margin-top: 30px;">
            <a href="https://www.linkedin.com/in/devanik/" target="_blank"
            style="background-color: #8a2be2; color: white; padding: 10px 20px;
            text-decoration: none; border-radius: 5px;
            font-weight: bold;">Connect with Devanik on LinkedIn</a>
        </div>

        </div>
        """, 
        unsafe_allow_html=True
    )

    # Footer Section with Subtle Styling
    st.markdown(
        """
        <div style="text-align: center; margin-top: 40px;">
            <p style="font-size: 1rem; color: #95a5a6;">
                Built with passion by <strong>Devanik</strong> and powered by <strong>Streamlit</strong>.<br>
                🌐 <a href="https://github.com/devanik21" style="color: #8a2be2;" target="_blank">Explore More Projects on GitHub</a>
            </p>
        </div>
        """, 
        unsafe_allow_html=True
    )


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



st.image("iris3.jpg", use_column_width=True)
st.image("iris2.jpg", use_column_width=True)
st.sidebar.image("iris1.jpg",use_column_width=True)
 
