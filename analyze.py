import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
@st.cache_data
def load_data():
    # Replace with your actual file path
    file_path = "Iris.csv"
    df = pd.read_csv(file_path)
    return df

def analyze_page():
    st.title("📊 Data Analysis")
    st.write("Explore and analyze the Iris dataset using various statistical techniques and visualizations.")

    # Load the dataset
    df = load_data()
    
    st.sidebar.header("Analysis Options")
    
    # Select analysis type
    analysis_type = st.sidebar.selectbox("Choose Analysis Type", ["Descriptive Statistics", "Distribution Analysis", "Correlation Analysis", "Feature Importance"])

    if analysis_type == "Descriptive Statistics":
        st.subheader("Descriptive Statistics")
        st.write(df.describe().T.style.background_gradient(cmap='viridis').highlight_max(axis=0, color='lightpink'))
    
    elif analysis_type == "Distribution Analysis":
        st.subheader("Distribution Analysis")
        column = st.sidebar.selectbox("Select Column", df.columns[1:-1])
        
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.histplot(df[column], kde=True, hue='Species', palette='viridis', ax=ax)
        ax.set_title(f'Distribution of {column}')
        st.pyplot(fig)
        
    elif analysis_type == "Correlation Analysis":
        st.subheader("Correlation Analysis")
        
        correlation_matrix = df.iloc[:, 1:-1].corr()
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', ax=ax, fmt='.2f', linewidths=0.5)
        ax.set_title('Correlation Heatmap')
        st.pyplot(fig)
    
    elif analysis_type == "Feature Importance":
        st.subheader("Feature Importance (Using Random Forest)")
        from sklearn.ensemble import RandomForestClassifier
        
        X = df.iloc[:, 1:-1]
        y = df['Species']
        
        model = RandomForestClassifier()
        model.fit(X, y)
        importances = model.feature_importances_
        
        feature_importances = pd.DataFrame(importances, index=X.columns, columns=['Importance']).sort_values('Importance', ascending=False)
        
        st.write(feature_importances.style.background_gradient(cmap='viridis').highlight_max(axis=0, color='lightpink'))
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.barplot(x=feature_importances.index, y='Importance', data=feature_importances, palette='viridis', ax=ax)
        ax.set_title('Feature Importance')
        ax.set_xlabel('Feature')
        ax.set_ylabel('Importance')
        st.pyplot(fig)
    
    st.write("Feel free to select different options to gain insights into the Iris dataset.")

