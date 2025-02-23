import streamlit as st

# --- Streamlit App ---

# ضبط اتجاه النص ليكون من اليمين إلى اليسار وتحسين تجربة القراءة
st.markdown(
    """
    <style>
    body {
        direction: rtl;
        text-align: right;
        font-family: 'Cairo', sans-serif;
    }
    .title {
        font-size: 3em;  /* تكبير العنوان الرئيسي */
        font-weight: bold;
        text-align: center;
        color: #007BFF;
    }
    .highlight {
        color: #FF5733;
        font-weight: bold;
        font-size: 1.2em;  /* تكبير النصوص المميزة */
    }
    .subtitle {
        font-size: 2em;  /* تكبير العناوين الفرعية */
        font-weight: bold;
        color: #28A745;
    }
    .divider-custom {
        border-top: 3px solid #007BFF;
        margin: 20px 0;
    }
    p {
        font-size: 1.4em;  /* تكبير النصوص العادية */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# عنوان التطبيق
st.markdown('<h1 class="title">الوظائف في جدارات</h1>', unsafe_allow_html=True)

st.markdown('<hr class="divider-custom">', unsafe_allow_html=True)

# عنوان التطبيق
st.markdown('<h4 class="title"عندك فضول؟</h4>', unsafe_allow_html=True)


st.markdown('<h5 class="title">🔎  هنا كنت ابي اشوف توزيع الوضايف على مناطق المملكة</h5>', unsafe_allow_html=True)
st.image("fig_1.png", caption="")
st.markdown('<hr class="divider-custom">', unsafe_allow_html=True)

st.markdown('<h5 class="title"> بعدها صرت اقول طيب كيف توزيع الفرص 📊</h5>', unsafe_allow_html=True)

st.image("fig_2.png", caption="")
st.markdown('<hr class="divider-custom">', unsafe_allow_html=True)

st.markdown('<h5 class="title">طيب شالوضع مع رواتب حديثي التخرج؟ 📊</h5>', unsafe_allow_html=True
st.image("fig_3.png", caption="")
st.markdown('<hr class="divider-custom">', unsafe_allow_html=True)

st.markdown('<h5 class="title">من عنده فرص اكثر حديث التخرج او الي عنده خبرة؟📊</h5>', unsafe_allow_html=True
st.image("fig_4.png", caption="")
st.markdown('<hr class="divider-custom">', unsafe_allow_html=True)




