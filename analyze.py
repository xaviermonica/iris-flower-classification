import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# Load the dataset
@st.cache_data
def load_data():
    # Replace with your actual file path
    file_path = "Iris.csv"
    df = pd.read_csv(file_path)
    return df

def analyze_page():
    st.title("📊 Advanced Data Analysis")
    st.write("Explore and analyze the Iris dataset using a range of advanced statistical techniques and visualizations.")

    # Load the dataset
    df = load_data()

    st.sidebar.header("Analysis Options")
    
    # Select analysis type
    analysis_type = st.sidebar.selectbox("Choose Analysis Type", [
        "Descriptive Statistics",
        "Distribution Analysis",
        "Correlation Analysis",
        "Feature Importance",
        "Pair Plot",
        "Box Plot",
        "Violin Plot"
    ])

    if analysis_type == "Descriptive Statistics":
        st.subheader("Descriptive Statistics")
        st.write(df.describe().T.style.background_gradient(cmap='viridis').highlight_max(axis=0, color='lightpink'))
    
    elif analysis_type == "Distribution Analysis":
        st.subheader("Distribution Analysis")
        column = st.sidebar.selectbox("Select Column", df.columns[:-1])
        
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.histplot(data=df, x=column, kde=True, hue='Species', palette='viridis', ax=ax)
        ax.set_title(f'Distribution of {column}', fontsize=16)
        ax.set_xlabel(column, fontsize=14)
        ax.set_ylabel('Frequency', fontsize=14)
        st.pyplot(fig)
        
    elif analysis_type == "Correlation Analysis":
        st.subheader("Correlation Analysis")
        
        correlation_matrix = df.drop('Species', axis=1).corr()
        fig, ax = plt.subplots(figsize=(12, 10))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', ax=ax, fmt='.2f', linewidths=0.5, vmin=-1, vmax=1)
        ax.set_title('Correlation Heatmap', fontsize=16)
        st.pyplot(fig)

    elif analysis_type == "Feature Importance":
        st.subheader("Feature Importance (Using Random Forest)")
        
        X = df.drop('Species', axis=1)
        y = df['Species']
        
        # Encode categorical target variable
        le = LabelEncoder()
        y_encoded = le.fit_transform(y)
        
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X, y_encoded)
        importances = model.feature_importances_
        
        feature_importances = pd.DataFrame(importances, index=X.columns, columns=['Importance']).sort_values('Importance', ascending=False)
        
        st.write(feature_importances.style.background_gradient(cmap='viridis').highlight_max(axis=0, color='lightpink'))
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.barplot(x=feature_importances.index, y='Importance', data=feature_importances, palette='viridis', ax=ax)
        ax.set_title('Feature Importance', fontsize=16)
        ax.set_xlabel('Feature', fontsize=14)
        ax.set_ylabel('Importance', fontsize=14)
        st.pyplot(fig)

    elif analysis_type == "Pair Plot":
        st.subheader("Pair Plot")
        
        fig = sns.pairplot(df, hue='Species', palette='viridis')
        st.pyplot(fig)
    
    elif analysis_type == "Box Plot":
        st.subheader("Box Plot")
        column = st.sidebar.selectbox("Select Column for Box Plot", df.columns[:-1])
        
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.boxplot(x='Species', y=column, data=df, palette='viridis', ax=ax)
        ax.set_title(f'Box Plot of {column}', fontsize=16)
        ax.set_xlabel('Species', fontsize=14)
        ax.set_ylabel(column, fontsize=14)
        st.pyplot(fig)

    elif analysis_type == "Violin Plot":
        st.subheader("Violin Plot")
        column = st.sidebar.selectbox("Select Column for Violin Plot", df.columns[:-1])
        
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.violinplot(x='Species', y=column, data=df, palette='viridis', ax=ax)
        ax.set_title(f'Violin Plot of {column}', fontsize=16)
        ax.set_xlabel('Species', fontsize=14)
        ax.set_ylabel(column, fontsize=14)
        st.pyplot(fig)
    
    st.write("Explore different analysis options to gain deeper insights into the Iris dataset.")
