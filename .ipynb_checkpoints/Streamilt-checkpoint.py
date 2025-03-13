import streamlit as st
import pandas as pd
import plotly.express as px


st.title("📊 تدور وظيفة؟")


@st.cache_data  
def load_data():
    df = pd.read_excel('output.xlsx')
    return df

df = load_data()


st.markdown("""
<style>
    body, .stApp {
        text-align: right;
        direction: rtl;
    }
    .css-1d391kg, .css-1v3fvcr, .css-1d391kg p, .css-1v3fvcr p {
        text-align: right !important;
        direction: rtl !important;
    }
</style>
""", unsafe_allow_html=True)


st.header("1. مقدمة")
st.write("""
أول منصة ممكن تفيدك هي جدرات، حيث تقدر تستعرض الفرص الوظيفية المتاحة، تقدم على الوظائف بسهولة، وتطور مهاراتك من خلال الدورات التدريبية المتوفرة. انطلق نحو مستقبلك الوظيفي مع جدرات!
""")

st.header("2. الوظائف الأكثر شيوعًا")
st.write("""
انواع الوظايف في جدرات متوعة تقدر تختار على حسبب تخصص الجامعيي 
""")
job_counts = df['job_title'].value_counts().reset_index()
job_counts.columns = ['job_title', 'count']
fig1 = px.bar(job_counts, x='job_title', y='count', title="")
st.plotly_chart(fig1)

st.header("3. المناطق الجغرافية")
st.write("""
في جدارات، يمكنك مشاهدة جميع الوظائف المتاحة في المنطقة التي ترغب فيها.
""")
region_counts = df['region'].value_counts(normalize=True) * 100
region_counts = region_counts.reset_index()
region_counts.columns = ['region', 'percentage']
fig2 = px.pie(region_counts, values='percentage', names='region', title="")
st.plotly_chart(fig2)

st.header("5. توزيع الوظائف حسب الجنس")
st.write("""
طيب، الوظيفة التي أريدها، هل هي متاحة للجنسين؟
""")
gender_counts = df['gender'].value_counts().reset_index()
gender_counts.columns = ['gender', 'count']
fig3 = px.bar(gender_counts, x='gender', y='count')
st.plotly_chart(fig3)

st.header("6. الرواتب المتوقعة للخريجين الجدد")
st.write("""
طيب، هل رواتبها جيدة؟
""")
fresh_grads = df[df['exper'] == '0 Years']
fig4 = px.histogram(fresh_grads, x='benefits', title="")
st.plotly_chart(fig4)

st.header("7. فرص العمل حسب سنوات الخبرة")
st.write("""
هل هناك وظائف لعديمي الخبرة؟
""")
experience_counts = df['exper'].value_counts().reset_index()
experience_counts.columns = ['exper', 'count']
fig5 = px.bar(experience_counts, x='exper', y='count')
st.plotly_chart(fig5)
st.header("خاتمة")
st.write("""
يعد العثور على الوظيفة المناسبة خطوة مهمة نحو بناء مستقبل مهني ناجح. من خلال منصة جدارات، يمكنك استكشاف الفرص الوظيفية المتاحة، ومعرفة المتطلبات والشروط، واتخاذ قرارات مستنيرة بشأن مسارك المهني. لا تتردد في الاستفادة من هذه الموارد للارتقاء بمستقبلك الوظيفي وتحقيق طموحاتك.
""")

