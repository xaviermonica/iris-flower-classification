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

def visualize_page():
 
    
    # Load the dataset
    df = load_data()
    
    st.write("Explore the visualizations for the Iris dataset below.")

    # Sidebar for user input
    st.sidebar.header("Visualization Options")
    
    # Select plot type
    plot_type = st.sidebar.selectbox("Choose Plot Type", [
        "Scatter Plot", "Histogram", "Pair Plot", "Correlation Heatmap", 
        "Box Plot", "Violin Plot", "Strip Plot", "Swarm Plot",
        "Joint Plot", "Ridge Plot", "Hexbin Plot", "Lag Plot",
        "Andrews Curves", "Count Plot", "Facet Grid", "Matrix Plot",
        "Pair Grid", "Heatmap", "ECDF Plot", "KDE Plot"
    ])

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

    # Box Plot
    elif plot_type == "Box Plot":
        st.subheader("Box Plot")
        column = st.sidebar.selectbox("Select Column", df.columns[1:-1])
        
        fig, ax = plt.subplots()
        sns.boxplot(data=df, x='Species', y=column, palette='viridis', ax=ax)
        ax.set_title(f'Box Plot of {column} by Species')
        st.pyplot(fig)
    
    # Violin Plot
    elif plot_type == "Violin Plot":
        st.subheader("Violin Plot")
        column = st.sidebar.selectbox("Select Column", df.columns[1:-1])
        
        fig, ax = plt.subplots()
        sns.violinplot(data=df, x='Species', y=column, palette='viridis', ax=ax)
        ax.set_title(f'Violin Plot of {column} by Species')
        st.pyplot(fig)
    
    # Strip Plot
    elif plot_type == "Strip Plot":
        st.subheader("Strip Plot")
        column = st.sidebar.selectbox("Select Column", df.columns[1:-1])
        
        fig, ax = plt.subplots()
        sns.stripplot(data=df, x='Species', y=column, palette='viridis', ax=ax)
        ax.set_title(f'Strip Plot of {column} by Species')
        st.pyplot(fig)
    
    # Swarm Plot
    elif plot_type == "Swarm Plot":
        st.subheader("Swarm Plot")
        column = st.sidebar.selectbox("Select Column", df.columns[1:-1])
        
        fig, ax = plt.subplots()
        sns.swarmplot(data=df, x='Species', y=column, palette='viridis', ax=ax)
        ax.set_title(f'Swarm Plot of {column} by Species')
        st.pyplot(fig)
    
    # Joint Plot
    elif plot_type == "Joint Plot":
        st.subheader("Joint Plot")
        x_axis = st.sidebar.selectbox("X-axis", df.columns[1:-1])
        y_axis = st.sidebar.selectbox("Y-axis", df.columns[1:-1])
        
        fig = sns.jointplot(data=df, x=x_axis, y=y_axis, hue='Species', palette='viridis', kind='scatter')
        st.pyplot(fig)
    
    # Ridge Plot
    # Ridge Plot
    elif plot_type == "Ridge Plot":
        st.subheader("Ridge Plot")
        column = st.sidebar.selectbox("Select Column", df.columns[1:-1])
        
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Plot KDE for each species
        for species in df['Species'].unique():
            subset = df[df['Species'] == species]
            sns.kdeplot(data=subset, x=column, label=species, shade=True, alpha=0.6, ax=ax, palette='viridis')
        
        ax.set_title(f'Ridge Plot of {column} by Species')
        ax.legend(title='Species')
        st.pyplot(fig)

    # Hexbin Plot
    elif plot_type == "Hexbin Plot":
        st.subheader("Hexbin Plot")
        x_axis = st.sidebar.selectbox("X-axis", df.columns[1:-1])
        y_axis = st.sidebar.selectbox("Y-axis", df.columns[1:-1])
        
        fig, ax = plt.subplots()
        hb = ax.hexbin(df[x_axis], df[y_axis], gridsize=30, cmap='viridis')
        cb = plt.colorbar(hb, ax=ax)
        ax.set_title(f'Hexbin Plot of {x_axis} vs {y_axis}')
        st.pyplot(fig)
    
    # Lag Plot
    # Lag Plot
    elif plot_type == "Lag Plot":
        st.subheader("Lag Plot")
        column = st.sidebar.selectbox("Select Column", df.columns[1:-1])
        
        # Create lagged data
        lag = 1
        df_lag = df[[column]].copy()
        df_lag['Lag'] = df_lag[column].shift(lag)
        df_lag = df_lag.dropna()
        
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.scatter(df_lag[column], df_lag['Lag'], alpha=0.7)
        ax.set_xlabel(f'{column}')
        ax.set_ylabel(f'Lag {lag} of {column}')
        ax.set_title(f'Lag Plot of {column}')
        
        st.pyplot(fig)

    
    # Andrews Curves
    elif plot_type == "Andrews Curves":
        st.subheader("Andrews Curves")
        
        fig = plt.figure(figsize=(10, 6))
        sns.andrews_curves(df, 'Species', palette='viridis')
        plt.title('Andrews Curves')
        st.pyplot(fig)
    
    # Count Plot
    elif plot_type == "Count Plot":
        st.subheader("Count Plot")
        
        fig = plt.figure(figsize=(8, 6))
        sns.countplot(data=df, x='Species', palette='viridis')
        plt.title('Count Plot of Species')
        st.pyplot(fig)
    
    # Facet Grid
    elif plot_type == "Facet Grid":
        st.subheader("Facet Grid")
        column = st.sidebar.selectbox("Select Column", df.columns[1:-1])
        
        g = sns.FacetGrid(df, col='Species', col_wrap=3, height=4)
        g.map(sns.histplot, column, bins=30, kde=True)
        st.pyplot(g)
    
    # Matrix Plot
    elif plot_type == "Matrix Plot":
        st.subheader("Matrix Plot")
        
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(df.corr(), annot=True, cmap='coolwarm', ax=ax, fmt='.2f')
        ax.set_title('Correlation Matrix Plot')
        st.pyplot(fig)
    
    # Pair Grid
    elif plot_type == "Pair Grid":
        st.subheader("Pair Grid")
        
        g = sns.PairGrid(df, hue='Species', palette='viridis')
        g.map_lower(sns.scatterplot)
        g.map_diag(sns.histplot)
        st.pyplot(g)
    
    # Heatmap
    elif plot_type == "Heatmap":
        st.subheader("Heatmap")
        correlation_matrix = df.corr()
        
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', ax=ax, fmt='.2f')
        ax.set_title('Heatmap of Correlation Matrix')
        st.pyplot(fig)
    
    # ECDF Plot
    elif plot_type == "ECDF Plot":
        st.subheader("ECDF Plot")
        column = st.sidebar.selectbox("Select Column", df.columns[1:-1])
        
        fig = plt.figure(figsize=(10, 6))
        sns.ecdfplot(df[column], hue=df['Species'], palette='viridis')
        plt.title(f'ECDF Plot of {column}')
        st.pyplot(fig)
    
    # KDE Plot
    elif plot_type == "KDE Plot":
        st.subheader("KDE Plot")
        column = st.sidebar.selectbox("Select Column", df.columns[1:-1])
        
        fig = plt.figure(figsize=(10, 6))
        sns.kdeplot(df[column], hue=df['Species'], palette='viridis')
        plt.title(f'KDE Plot of {column}')
        st.pyplot(fig)

    # Add a download button for the dataset
    st.sidebar.download_button(
        label="Download Dataset",
        data=df.to_csv(index=False).encode('utf-8'),
        file_name='iris_data.csv',
        mime='text/csv'
    )

    st.write("Feel free to explore different visualizations to gain insights from the Iris dataset.")
