import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import arabic_reshaper
from bidi.algorithm import get_display
from datetime import datetime

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("clean_data.csv")
df = load_data()
# Custom CSS for background color

def load_css():
    with open("css/main.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Apply CSS
load_css()

st.markdown(
    """
    <style>

        .stApp {
            background-color: #eae2d9; /* Light gray */
        }
        [data-testid="stSidebar"] {
            background-color: #464d70; /* Dark Blue-Gray */
        
    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit App
#st.title("📊 Jobs Employment Landscape Dashboard")

st.image("imgs/titel.png",  use_column_width=True)
st.markdown(
    """
    
    <div class="head-div"">
    <h3> حديث تخرج او حتى تبحث عن وظائف وحاب تعرف عن سوق العمل في المملكة</h3>
    <h5>         في البداية انا حمد حديث تخرج وابحث عن وظيفة مناسبة لي ولكن مااعرف كيف ابدا ماعرف ايش المهارات الي احتاج اطورها؟ او حتى اللغات الي لازم اتقنها ف قررت اجمع البيانات وابدا احللها عشان احصل إجابات وافيه وكافيه</h5>
    </div>


    <div class="head-div">

    <h4> تعال معي خلني اوريك اكثر الوظائف المطروحه على المنصه الوطنية جدارات حسب مناطق المملكة</h4>
    </div>

        """,

        unsafe_allow_html=True

)
st.markdown(
    """
    
    <div class="head-div"">
    </div>
    """,unsafe_allow_html=True)
# Sidebar Filters
st.sidebar.header("الفرز حسب المنطقة")
selected_region = st.sidebar.selectbox("حدد منطقتك", df["region"].unique())
filtered_df = df[df["region"] == selected_region]


st.subheader("اكثر المناطق طرحاً للوظائف")
top_jobs = df['region'].value_counts().head(10)  
fig, ax = plt.subplots(figsize=(10, 6))


sns.barplot(y=[get_display(arabic_reshaper.reshape(x)) for x in top_jobs.index], x=top_jobs.values, palette="coolwarm", ax=ax)
fig.patch.set_facecolor("#eae2d9")  # Light gray background
ax.set_facecolor("#D1E7DD")  # Light green for the plot background

ax.set_xlabel(get_display(arabic_reshaper.reshape("عدد الوظائف")))
st.pyplot(fig)
st.markdown(
    """
<h5> هنا نشوف وش هي اكثر المناطق فيها طرح كثير للوظائف ونقدر نحدد وش المنطقه الي حاب تركز عليها </h5>
<h5> > من خلال القائمة الجانبية ابيك تختار منطقتك من المناطق الموجودة </h5>

 <div class="head-div"">
    </div>

    """
,unsafe_allow_html=True)

#Most Common Job Titles
st.subheader(f"اكثر الوظائف طرحاً في {selected_region}")
top_jobs = filtered_df['job_title'].value_counts().head(10)
fig, ax = plt.subplots(figsize=(10, 6))


sns.barplot(y=[get_display(arabic_reshaper.reshape(x)) for x in top_jobs.index], x=top_jobs.values, palette="coolwarm", ax=ax)
fig.patch.set_facecolor("#eae2d9")  # Light gray background
ax.set_facecolor("#D1E7DD")  # Light green for the plot background

ax.set_xlabel(get_display(arabic_reshaper.reshape("عدد الوظائف")))
st.pyplot(fig)
st.markdown(
    """
<h5> هاذي هي اكثر الوظائف المطروحة في منطقتك ومن خلالها تقدر تعرف تركز على اي وظيفة انت حاب تتوظفها</h5>
 <div class="head-div"">
    </div>

    """
,unsafe_allow_html=True)
#Salary Distribution
st.subheader(f"  توزيع الرواتب في  {selected_region}")
fig, ax = plt.subplots(figsize=(10, 6))
sns.histplot(filtered_df['Salary'].dropna(), bins=20, kde=True, color="blue", ax=ax)
ax.set_xlabel(get_display(arabic_reshaper.reshape("الراتب")))
ax.set_ylabel(get_display(arabic_reshaper.reshape("العدد")))
fig.patch.set_facecolor("#eae2d9")  # Light gray background
ax.set_facecolor("#D1E7DD")  # Light green for the plot background
st.pyplot(fig)
st.markdown(
    """
    
<h5>  ومن هنا تقدر تشوف معدل توزيع الرواتب في منطقتك وتقدر تستنتج اذا حصلت وظيفه هل راتبها يعتبر مناسب حسب المنطقة او لا </h5>
<div class="head-div"">
    </div>

    """
,unsafe_allow_html=True)

# Language Requirements
st.subheader(f" اكثر اللغات المطلوبة في {selected_region}")
language_counts = filtered_df['required_languages'].explode().value_counts().head(3)
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(y=[get_display(arabic_reshaper.reshape(x)) for x in language_counts.index[1:]], x=language_counts.values[1:], palette="viridis", ax=ax)
ax.set_xlabel(get_display(arabic_reshaper.reshape("عدد الوظائف")))
fig.patch.set_facecolor("#eae2d9")  
ax.set_facecolor("#D1E7DD") 
st.pyplot(fig)
st.markdown(
    """
    
<h5>   ومن هنا تقدر تشوف اكثر اللغات المطلوبه في الوظائف وتركز على تطويرها ولو نلاحظ ان اللغة الانجليزية من اهم اللغات المطلوبة في التوظيف عندنا       </h5>
<div class="head-div"">
    </div>

    """
,unsafe_allow_html=True)





st.subheader(f" اكثر المهارات المطلوبة في {selected_region}")
language_counts = filtered_df['Skills'].explode().value_counts().head(5)
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(y=[get_display(arabic_reshaper.reshape(x)) for x in language_counts.index[1:]], x=language_counts.values[1:], palette="viridis", ax=ax)
ax.set_xlabel(get_display(arabic_reshaper.reshape("عدد الوظائف")))
fig.patch.set_facecolor("#eae2d9")  
ax.set_facecolor("#D1E7DD") 
st.pyplot(fig)
st.markdown(
    """

<h5>       بعد ماشفت اهم المهارات المطلوبه في منطقتك تقدر تعمل على تطويرها وانا اشوف ان من اهمها الحاسب     </h5>



<div class="result-card">
            <h2>والحين بعد ماخذت نظره كافيه عن اكثر منطقة فيها وظائف ووش هي الوظائف المطروحة</h2>
            <ul>
            <li> بما ان الرياض هي اكثر منطقة طرحاً للوظائف انا اشوف انها مكان مناسب للبحث عن وظيفه</li>
            <li> واكيد اللغة الانجليزية هي اهم لغة بشتغل على تطويرها </li>
            <li> وبرضو بشتغل على مهارة الحاسب الالي والتعامل مع البرامج</li>
            </ul>



        </div>

    """
,unsafe_allow_html=True)




#st.write("🚀 **Explore employment trends with interactive visualizations!**")
