import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def main():
    st.title("Fresh Graduate CSV Data Explorer")
    st.write(
        """
        Welcome! This app is tailored for fresh graduates to easily explore and analyze CSV data.
        It will try to load a default CSV file (`cleaned_jadarat.csv`) if available.
        Otherwise, you can upload your own CSV file.
        """
    )
    
    # Define the default CSV file path
    default_file = '/mnt/data/cleaned_jadarat.csv'
    
    # Attempt to load the default file if it exists
    if os.path.exists(default_file):
        st.info("Loading default CSV file: cleaned_jadarat.csv")
        try:
            df = pd.read_csv(default_file)
        except Exception as e:
            st.error(f"Error loading default CSV file: {e}")
            return
    else:
        # Provide a file uploader if default file is not found
        uploaded_file = st.file_uploader("Upload your CSV file", type="csv")
        if uploaded_file is not None:
            try:
                df = pd.read_csv(uploaded_file)
                st.success("File loaded successfully!")
            except Exception as e:
                st.error(f"An error occurred while processing the CSV file: {e}")
                return
        else:
            st.warning("Please upload a CSV file to get started.")
            return

    # Display a preview of the data
    st.subheader("Data Preview")
    st.dataframe(df.head())

    # Display summary statistics
    st.subheader("Data Summary")
    st.write(df.describe())

    # Check for numerical columns for visualization
    num_columns = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
    if num_columns:
        selected_col = st.selectbox("Select a numerical column for histogram", num_columns)
        st.subheader(f"Histogram of {selected_col}")
        fig, ax = plt.subplots()
        ax.hist(df[selected_col].dropna(), bins=20, color='skyblue', edgecolor='black')
        st.pyplot(fig)
        
        # Display a correlation heatmap if more than one numerical column exists
        if len(num_columns) > 1:
            st.subheader("Correlation Matrix")
            corr = df[num_columns].corr()
            st.write(corr)
            fig2, ax2 = plt.subplots()
            sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax2)
            st.pyplot(fig2)
    else:
        st.info("No numerical columns found for visualization.")

if __name__ == '__main__':
    main()
