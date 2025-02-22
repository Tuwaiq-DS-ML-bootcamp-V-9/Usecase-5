import streamlit as st
import pandas as pd
import plotly.express as px

# App title
st.set_page_config(page_title="Jobs in Saudi Arabia", layout="wide")

# Load data
jops = pd.read_csv("Data/cleaned_data.csv")

# Add job-related images
st.image("images/jobs_banner.jpg", use_column_width=True)  # Change to a relevant image
st.title("📊 Jobs in Saudi Arabia")

# Sidebar Filters
st.sidebar.header("🔍 Filter Jobs")
selected_region = st.sidebar.selectbox("Select Region", ["All"] + list(jops["region"].unique()))
selected_category = st.sidebar.selectbox("Select Job Category", ["All"] + list(jops["job_title"].unique()))

# Apply filters
filtered_data = jops.copy()
if selected_region != "All":
    filtered_data = filtered_data[filtered_data["region"] == selected_region]
if selected_category != "All":
    filtered_data = filtered_data[filtered_data["job_title"] == selected_category]

# Display Job Count
st.subheader("📈 Job Distribution by Region")
fig = px.bar(
    jops, x="region", color="region",
    title="Number of Jobs by Region",
    color_discrete_sequence=px.colors.qualitative.Pastel
)
st.plotly_chart(fig, use_container_width=True)

# Display Job Table
st.subheader("📋 Available Jobs")
st.dataframe(filtered_data[["job_title", "comp_name", "region", "job_date"]].reset_index(drop=True))

# Footer Image
st.image("images/jobs_footer.jpg", use_column_width=True)  # Another relevant job-related image