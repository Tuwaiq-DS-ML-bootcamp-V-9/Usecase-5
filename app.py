import pandas as pd
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# Set page configuration
st.set_page_config(layout="wide", page_title="تحليل بيانات الوظائف في المملكة العربية السعودية")

# Load data
jadarat_data = pd.read_csv("cleaned_Jadarat_data.csv")

# Data Cleaning
jadarat_data['job_title'] = jadarat_data['job_title'].str.lower().str.strip().fillna('Unknown')
jadarat_data['gender'] = jadarat_data['gender'].str.lower().str.strip().fillna('Unknown')
jadarat_data['exper'] = pd.to_numeric(jadarat_data['exper'], errors='coerce').fillna(0).astype(int)
jadarat_data['region'] = jadarat_data['region'].fillna('Unknown')
jadarat_data['Salary'] = pd.to_numeric(jadarat_data['Salary'], errors='coerce').fillna(0)

# Custom CSS for improved styling
def load_css():
    custom_css = """
    <style>
        .stApp {
            background: #fdf6e3;
            text-align: right;
            direction: rtl;
            font-family: 'Tajawal', sans-serif;
        }
        h1, h2, h3 {
            color: #657b83;
        }
        .chart-container {
            background: #fff;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

# Load CSS
load_css()

# Hero Section
def hero_section():
    st.markdown("""
    <div style="text-align: center; padding: 2rem; background: #268bd2; border-radius: 15px; color: white;">
        <h1>📊 تحليل بيانات الوظائف في المملكة العربية السعودية</h1>
        <h3>اكتشف التوجهات الوظيفية في المملكة</h3>
    </div>
    """, unsafe_allow_html=True)

# Charts Section
def charts_section():
    st.header("🔎 تحليلات الوظائف")
    
    # Job Postings by Region
    st.subheader("🌍 توزيع الإعلانات الوظيفية حسب المناطق")
    region_distribution = jadarat_data['region'].value_counts().reset_index()
    region_distribution.columns = ['region', 'count']
    fig1 = px.bar(region_distribution, x='region', y='count', title='توزيع الإعلانات حسب المناطق',
                  color='count', color_continuous_scale='blues')
    st.plotly_chart(fig1, use_container_width=True)
    st.markdown("""📌 **تحليل:** يوضح هذا المخطط أن بعض المناطق تحتوي على فرص وظيفية أكثر من غيرها، مما يعكس تركيز الأنشطة الاقتصادية في مناطق معينة. يمكن أن يكون هذا مؤشرًا على الحاجة إلى تعزيز فرص العمل في المناطق الأقل تمثيلًا.""")
    
    # Job Postings by Gender
    st.subheader("👨‍💻 توزيع الإعلانات حسب الجنس")
    gender_distribution = jadarat_data['gender'].value_counts().reset_index()
    gender_distribution.columns = ['gender', 'count']
    fig2 = px.pie(gender_distribution, values='count', names='gender', title='توزيع الإعلانات حسب الجنس',
                  color_discrete_sequence=px.colors.sequential.RdBu)
    st.plotly_chart(fig2, use_container_width=True)
    st.markdown("""📌 **تحليل:** يكشف هذا الرسم البياني عن الفروق في إعلانات التوظيف بين الجنسين. إذا كانت هناك فجوة كبيرة، فقد يشير ذلك إلى فرص متاحة بشكل غير متساوٍ بين الجنسين في بعض القطاعات.""")
    
    # Average Salary by Job Title
    st.subheader("💼 متوسط الرواتب حسب العناوين الوظيفية")
    avg_salary_by_job = jadarat_data.groupby('job_title')['Salary'].mean().reset_index()
    avg_salary_by_job = avg_salary_by_job.sort_values(by='Salary', ascending=False).head(10)
    fig3 = px.bar(avg_salary_by_job, x='job_title', y='Salary', title='متوسط الرواتب حسب العناوين الوظيفية',
                  color='Salary', color_continuous_scale='Viridis')
    st.plotly_chart(fig3, use_container_width=True)
    st.markdown("""📌 **تحليل:** يوضح هذا المخطط الوظائف التي تتمتع بمتوسط رواتب مرتفع، مما يمكن الباحثين عن عمل من تحديد المسارات المهنية الأكثر ربحية بناءً على البيانات الحالية.""")

# Main Function
def main():
    hero_section()
    charts_section()
    st.markdown("""
    <div style="text-align: center; padding: 1rem; background: #fdf6e3; border-radius: 10px;">
        <p>تم التحليل بواسطة مشعل الشقحاء | جميع الحقوق محفوظة 2025</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
