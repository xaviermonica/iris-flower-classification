import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
@st.cache_data
def load_data():
    # Replace with your actual file path
    file_path = "iris.csv"
    df = pd.read_csv(file_path)
    return df

def visualize_page():
    st.title("📊 Data Visualization")
    
    # Load the dataset
    df = load_data()
    
    st.write("Explore the visualizations for the Iris dataset below.")

    # Sidebar for user input
    st.sidebar.header("Visualization Options")
    
    # Select plot type
    plot_type = st.sidebar.selectbox("Choose Plot Type", ["Scatter Plot", "Histogram", "Pair Plot", "Correlation Heatmap"])

    # Scatter Plot
    if plot_type == "Scatter Plot":
        st.subheader("Scatter Plot")
        x_axis = st.sidebar.selectbox("X-axis", df.columns[1:-1])
        y_axis = st.sidebar.selectbox("Y-axis", df.columns[1:-1])
        
        fig, ax = plt.subplots()
        sns.scatterplot(data=df, x=x_axis, y=y_axis, hue='Species', palette='viridis', ax=ax)
        ax.set_title(f'Scatter Plot of {x_axis} vs {y_axis}')
        st.pyplot(fig)
    
    # Histogram
    elif plot_type == "Histogram":
        st.subheader("Histogram")
        column = st.sidebar.selectbox("Select Column", df.columns[1:-1])
        
        fig, ax = plt.subplots()
        sns.histplot(df[column], bins=30, kde=True, hue=df['Species'], palette='viridis', ax=ax)
        ax.set_title(f'Histogram of {column}')
        st.pyplot(fig)
    
    # Pair Plot
    elif plot_type == "Pair Plot":
        st.subheader("Pair Plot")
        
        fig = sns.pairplot(df, hue='Species', palette='viridis')
        st.pyplot(fig)
    
    # Correlation Heatmap
    elif plot_type == "Correlation Heatmap":
        st.subheader("Correlation Heatmap")
        
        correlation_matrix = df.iloc[:, 1:-1].corr()
        fig, ax = plt.subplots()
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', ax=ax, fmt='.2f', linewidths=0.5)
        ax.set_title('Correlation Heatmap')
        st.pyplot(fig)

    # Add a download button for the dataset
    st.sidebar.download_button(
        label="Download Dataset",
        data=df.to_csv(index=False).encode('utf-8'),
        file_name='iris_data.csv',
        mime='text/csv'
    )

    st.write("Feel free to explore different visualizations to gain insights from the Iris dataset.")
