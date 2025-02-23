import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import arabic_reshaper
from bidi.algorithm import get_display

Jadarat_data = pd.read_csv("cleaned_Jadarat_data")  # Example: loading from CSV


# --- Streamlit App ---
st.title("Jadarat Data Visualization")
fig_1 = st.file_uploader('fig_1',type = 'png')

if fig_1 is not None:
    try:
        image = Image.open(uploaded_file) # Open the uploaded file using PIL
        st.image(image, caption="Uploaded Image", use_column_width=True)
    except Exception as e:
        st.error(f"Error processing uploaded image: {e}")
