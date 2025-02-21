import pandas as pd
import streamlit as st
import plotly.express as px

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

def load_css(theme):
    """Load futuristic CSS with glassmorphism and neon effects."""
    custom_css = f"""
    <style>
        /* Global App Styling */
        .stApp {{
            background: {theme['background']};
            text-align: right;
            direction: rtl;
            color: {theme['text_color']};
            font-family: 'Tajawal', sans-serif;
            overflow-x: hidden;
        }}
        h1, h2, h3 {{
            font-family: {theme['header_font']};
            color: {theme['text_color']};
            font-weight: 700;
            letter-spacing: 1px;
        }}
        /* Hero Section with Glassmorphism */
        .hero {{
            background: linear-gradient(135deg, rgba(255,255,255,0.1), rgba(255,255,255,0.05)),
                        url('https://images.unsplash.com/photo-1496171367470-9ed9a91ea931') center/cover no-repeat;
            backdrop-filter: blur(10px);
            padding: 4rem 2rem;
            border-radius: 20px;
            margin: 2rem 1rem;
            text-align: center;
            border: 1px solid rgba(255,255,255,0.2);
            box-shadow: 0 15px 30px rgba(0,0,0,0.4);
            transition: all 0.4s ease;
        }}
        .hero:hover {{
            transform: scale(1.02);
            box-shadow: 0 20px 40px rgba(0,0,0,0.5);
        }}
        .hero h1 {{
            color: {theme['accent1']};
            text-shadow: 0 0 10px {theme['accent1']}, 0 0 20px {theme['accent2']};
            font-size: 3.2rem;
            margin-bottom: 1rem;
        }}
        .hero h3 {{
            color: {theme['text_color']};
            font-size: 1.6rem;
            opacity: 0.9;
        }}
        /* Filter Inputs with Neon Glow */
        .stSelectbox, .stNumberInput {{
            background: rgba(255,255,255,0.1);
            border-radius: 12px;
            padding: 0.8rem;
            border: 1px solid {theme['accent3']};
            box-shadow: 0 0 10px {theme['accent3']};
            transition: all 0.3s ease;
            color: {theme['text_color']};
        }}
        .stSelectbox:hover, .stNumberInput:hover {{
            box-shadow: 0 0 15px {theme['accent3']}, 0 0 25px {theme['accent2']};
            border-color: {theme['accent2']};
        }}
        /* Filter Result Box with Glass Effect */
        .filter-result-box {{
            background: linear-gradient(135deg, rgba(255,255,255,0.1), rgba(255,255,255,0.05));
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255,255,255,0.2);
            color: {theme['text_color']};
            padding: 2.5rem;
            border-radius: 20px;
            margin: 2rem 1rem;
            box-shadow: 0 15px 30px rgba(0,0,0,0.4), inset 0 0 10px rgba(255,255,255,0.1);
            transition: all 0.4s ease;
        }}
        .filter-result-box:hover {{
            transform: scale(1.03);
            box-shadow: 0 20px 40px rgba(0,0,0,0.5), inset 0 0 15px rgba(255,255,255,0.2);
        }}
        .filter-result-box h3 {{
            font-size: 2.6rem;
            margin-bottom: 1.5rem;
            color: {theme['accent1']};
            text-shadow: 0 0 8px {theme['accent1']};
        }}
        .filter-result-box p {{
            font-size: 1.7rem;
            margin: 0.8rem 0;
            font-weight: 400;
            color: {theme['text_color']};
        }}
        .filter-result-box p strong {{
            color: {theme['accent2']};
        }}
        /* Chart Containers */
        .plotly-chart {{
            border-radius: 15px;
            overflow: hidden;
            box-shadow: 0 8px 16px rgba(0,0,0,0.3);
            background: rgba(255,255,255,0.05);
            border: 1px solid rgba(255,255,255,0.1);
        }}
        /* Footer */
        .footer {{
            text-align: center;
            padding: 2rem;
            background: linear-gradient(to top, {theme['background']}, rgba(0,0,0,0.2));
            color: {theme['text_color']};
            font-size: 1.3rem;
            margin-top: 3rem;
            border-top: 1px solid {theme['accent3']};
            box-shadow: 0 -5px 15px rgba(0,0,0,0.2);
        }}
        /* Smooth Transitions */
        * {{
            transition: all 0.2s ease-out;
        }}
        html {{
            scroll-behavior: smooth;
        }}
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap" rel="stylesheet">
    """
    st.markdown(custom_css, unsafe_allow_html=True)

def hero_section(theme):
    """Display a futuristic hero section."""
    hero_html = f"""
    <div class="hero">
        <h1>📊 تحليل بيانات الوظائف في المملكة العربية السعودية</h1>
        <h3>استكشف المستقبل الوظيفي بأسلوب مبتكر</h3>
    </div>
    """
    st.markdown(hero_html, unsafe_allow_html=True)

def info_sections():
    """Show information sections with styled interactive graphs."""
    st.title('تحليل بيانات الوظائف في المملكة العربية السعودية')

    st.markdown('''<div>
                    <h3>تحليل متقدم لإعلانات الوظائف في السعودية مع رؤى حول الرواتب، التوزيع الجغرافي،
                    مستويات الخبرة، وأنماط العقود.</h3>
                </div>''', unsafe_allow_html=True)

    # Job Postings by Region
    st.markdown('''<h3>🌍 توزيع الإعلانات الوظيفية حسب المناطق</h3>''', unsafe_allow_html=True)
    region_distribution = jadarat_data['region'].value_counts().reset_index()
    region_distribution.columns = ['region', 'count']
    fig1 = px.bar(region_distribution, x='region', y='count', title='توزيع الإعلانات حسب المناطق',
                  color='count', color_continuous_scale='Plasma')
    st.plotly_chart(fig1, use_container_width=True)

    # Job Postings by Gender
    st.markdown('''<h3>👨‍💻 توزيع الإعلانات حسب الجنس</h3>''', unsafe_allow_html=True)
    gender_distribution = jadarat_data['gender'].value_counts().reset_index()
    gender_distribution.columns = ['gender', 'count']
    fig2 = px.pie(gender_distribution, values='count', names='gender', title='توزيع الإعلانات حسب الجنس',
                  color_discrete_sequence=px.colors.sequential.Magma)
    st.plotly_chart(fig2, use_container_width=True)

    # Average Salary by Job Title
    st.markdown('''<h3>💼 متوسط الرواتب حسب العناوين الوظيفية</h3>''', unsafe_allow_html=True)
    avg_salary_by_job = jadarat_data.groupby('job_title')['Salary'].mean().reset_index()
    avg_salary_by_job = avg_salary_by_job.sort_values(by='Salary', ascending=False).head(10)
    fig3 = px.bar(avg_salary_by_job, x='job_title', y='Salary', title='متوسط الرواتب حسب العناوين الوظيفية',
                  color='Salary', color_continuous_scale='Inferno')
    st.plotly_chart(fig3, use_container_width=True)

def main():
    # Futuristic theme configuration
    futuristic_theme = {
        "background": "#1a1a2e",   # Deep dark blue
        "text_color": "#e0e0e0",   # Light gray for contrast
        "accent1": "#00d4ff",      # Neon cyan
        "accent2": "#ff007a",      # Neon pink
        "accent3": "#39ff14",      # Neon green
        "hero_overlay": "rgba(0, 212, 255, 0.5)",
        "header_font": "'Tajawal', sans-serif",
        "recommendation_bg": "#16213e",
    }
    theme = futuristic_theme

    load_css(theme)
    hero_section(theme)
    info_sections()

    # Filters Section
    st.header('تصفية البيانات')
    
    col1, col2, col3 = st.columns([1.2, 1, 1])  # Slightly wider first column for job titles
    with col1:
        job_titles = jadarat_data['job_title'].unique()
        job_title = st.selectbox('اختر عنوان الوظيفة', job_titles, key='job_title')
    with col2:
        years_of_experience = st.number_input('عدد سنوات الخبرة', min_value=0, max_value=50, step=1, value=0, key='exper')
    with col3:
        unique_genders = jadarat_data['gender'].unique()
        gender = st.selectbox('اختر الجنس', unique_genders, key='gender')

    # Filter data
    filtered_data = jadarat_data[
        (jadarat_data['job_title'] == job_title) &
        (jadarat_data['exper'] == int(years_of_experience)) &
        (jadarat_data['gender'] == gender)
    ]

    # Display filtered results
    if not filtered_data.empty:
        st.markdown(f'''
        <div class="filter-result-box">
            <h3>معلومات الوظيفة المختارة</h3>
            <p><strong>عنوان الوظيفة:</strong> {job_title}</p>
            <p><strong>سنوات الخبرة:</strong> {years_of_experience}</p>
            <p><strong>الجنس:</strong> {gender}</p>
            <p><strong>المنطقة:</strong> {filtered_data['region'].values[0]}</p>
            <p><strong>الراتب:</strong> {filtered_data['Salary'].values[0]}</p>
            <p><strong>عدد النتائج المطابقة:</strong> {len(filtered_data)}</p>
        </div>
        ''', unsafe_allow_html=True)
    else:
        st.markdown('''
        <div class="filter-result-box">
            <h3>لا توجد نتائج مطابقة</h3>
            <p>لم يتم العثور على وظائف تطابق المعايير المحددة. يرجى التحقق من الفلاتر وإعادة المحاولة.</p>
        </div>
        ''', unsafe_allow_html=True)

    # Footer
    st.markdown(f'''<div class="footer">تم التحليل بواسطة مشعل الشقحاء | جميع الحقوق محفوظة 2025</div>''', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
