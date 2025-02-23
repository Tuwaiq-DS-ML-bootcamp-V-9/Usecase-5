import streamlit as st

# --- Streamlit App ---
st.title("Jadarat Data Visualization")
fig_1 = st.file_uploader('fig_1',type = 'png')
fig_2 = st.file_uploader('fig_2',type = 'png')
fig_3 = st.file_uploader('fig_3',type = 'png')
fig_4 = st.file_uploader('fig_4',type = 'png')

if fig_1 is not None:
    try:
        image = Image.open(fig_1) # Open the uploaded file using PIL
        st.image(fig_1, caption="Uploaded Image", use_column_width=True)
        image = Image.open(fig_2)
        st.image(fig_2, caption="Uploaded Image", use_column_width=True)
        image = Image.open(fig_3)
        st.image(fig_3, caption="Uploaded Image", use_column_width=True)
        image = Image.open(fig_4)
        st.image(fig_4, caption="Uploaded Image", use_column_width=True)
    except Exception as e:
        st.error(f"Error processing uploaded image: {e}")
