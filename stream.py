import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static

# Sample data
data = {'latitude': [24.7136, 21.3891], 'longitude': [46.6753, 39.8579]}  # Riyadh & Mecca
df = pd.DataFrame(data)

# Create a map centered at the first location
m = folium.Map(location=[df['latitude'][0], df['longitude'][0]], zoom_start=6)

# Add markers
for _, row in df.iterrows():
    folium.Marker([row['latitude'], row['longitude']], popup=f"Lat: {row['latitude']}, Lon: {row['longitude']}").add_to(m)

# Render the map
folium_static(m)
