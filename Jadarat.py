import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import arabic_reshaper
from bidi.algorithm import get_display

Jadarat_data = pd.read_csv("cleaned_Jadarat_data")  # Example: loading from CSV


# --- Streamlit App ---
st.title("Jadarat Data Visualization")
unique_regions = Jadarat_data['region'].unique()
region_counts = Jadarat_data['region'].value_counts()

# Reshape Arabic text
reshaped_regions = []  # Initialize an empty list
for item in unique_regions:
     reshaped_item = get_display(arabic_reshaper.reshape(item))
     reshaped_regions.append(reshaped_item)
         
# Create Plotly chart
fig = go.Figure(data=[go.Bar(x=reshaped_regions, y=region_counts)])
# Update layout
fig.update_layout(
    xaxis_title=get_display(arabic_reshaper.reshape("المناطق")),
    yaxis_title=get_display(arabic_reshaper.reshape("عدد الوظائف المتاحة")),
    title=get_display(arabic_reshaper.reshape("الوظائف المعروضة حسب المناطق")),
    font=dict(family='Arial', size=12),
    xaxis=dict(tickangle=45),
    title_x=0.5
    )

# Show the Plotly chart in Streamlit
st.plotly_chart(fig)


