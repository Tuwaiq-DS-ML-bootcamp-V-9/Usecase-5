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
    """Load enhanced custom CSS with modern styling."""
    custom_css = f"""
    <style>
        /* Global App Styling */
        .stApp {{
            background: {theme['background']};
            text-align: right;
            direction: rtl;
            color: {theme['text_color']};
            font-family: 'Tajawal', sans-serif;
            margin: 0;
            padding: 0;
        }}
        h1, h2, h3 {{
            font-family: {theme['header_font']};
            color: {theme['text_color']};
            font-weight: 700;
        }}
        /* Hero Section */
        .hero {{
            background: linear-gradient(135deg, {theme['hero_overlay']} 0%, rgba(0,0,0,0.5) 100%), 
                        url('https://images.unsplash.com/photo-1496171367470-9ed9a91ea931') center/cover no-repeat;
            padding: 5rem 2rem;
            border-radius: 20px;
            margin: 2rem 1rem;
            text-align: center;
            box-shadow: 0 10px 20px rgba(0,0,0,0.3);
            transition: transform 0.3s ease;
        }}
        .hero:hover {{
            transform: translateY(-5px);
        }}
        .hero h1 {{
            color: white;
            text-shadow: 3px 3px 6px rgba(0,0,0,0.5);
            font-size: 3rem;
            margin-bottom: 1rem;
        }}
        .hero h3 {{
            color: #e0e0e0;
            font-size: 1.5rem;
        }}
        /* Filter Section */
        .stSelectbox, .stNumberInput {{
            background: white;
            border-radius: 15px;
            padding: 0.5rem;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            transition: box-shadow 0.3s ease;
        }}
        .stSelectbox:hover, .stNumberInput:hover {{
            box-shadow: 0 6px 12px rgba(0,0,0,0.15);
        }}
        /* Filter Result Box */
        .filter-result-box {{
            background: linear-gradient(135deg, {theme['accent1']} 0%, {theme['accent2']} 70%, {theme['accent3']} 100%);
            color: white;
            padding: 2.5rem;
            border-radius: 25px;
            margin: 2rem 1rem;
            box-shadow: 0 10px 20px rgba(0,0,0,0.25);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }}
        .filter-result-box:hover {{
            transform: translateY(-5px);
            box-shadow: 0 12px 24px rgba(0,0,0,0.3);
        }}
        .filter-result-box h3 {{
            font-size: 2.5rem;
            margin-bottom: 1.5rem;
            text-shadow: 1px 1px 3px rgba(0,0,0,0.2);
        }}
        .filter-result-box p {{
            font-size: 1.6rem;
            margin: 0.8rem 0;
            font-weight: 400;
        }}
        /* Chart Containers */
        .plotly-chart {{
            border-radius: 15px;
            overflow: hidden;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }}
        /* Footer */
        .footer {{
            text-align: center;
            padding: 2rem;
            background: {theme['background']};
            color: {theme['text_color']};
            font-size: 1.2rem;
            border-top: 1px solid {theme['accent3']};
            margin-top: 2rem;
        }}
        /* Smooth Scroll */
        html {{
            scroll-behavior: smooth;
        }}
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap" rel="stylesheet">
    """
    st.markdown(custom_css, unsafe_allow_html=True)

def hero_section(theme):
    """Display an enhanced hero section."""
    hero_html = f"""
    <div class="hero">
        <h1>📊 تحليل بيانات الوظائف في المملكة العربية السعودية</h1>
        <h3>اكتشف التوجهات الوظيفية في المملكة بأسلوب حديث</h3>
    </div>
    """
    st.markdown(hero_html, unsafe_allow_html=True)

def info_sections():
    """Show information sections with styled interactive graphs."""
    st.title('تحليل بيانات الوظائف في المملكة العربية السعودية')

    st.markdown('''<div>
                    <h3>نقدم تحليلًا شاملًا لإعلانات الوظائف في السعودية، مع التركيز على الرواتب،
                    توزيع الوظائف حسب المناطق ومستويات الخبرة، وأنواع عقود العمل.</h3>
                </div>''', unsafe_allow_html=True)

    # Job Postings by Region
    st.markdown('''<h3>🌍 توزيع الإعلانات الوظيفية حسب المناطق</h3>''', unsafe_allow_html=True)
    region_distribution = jadarat_data['region'].value_counts().reset_index()
    region_distribution.columns = ['region', 'count']
    fig1 = px.bar(region_distribution, x='region', y='count', title='توزيع الإعلانات حسب المناطق',
                  color='count', color_continuous_scale='Blues')
    st.plotly_chart(fig1, use_container_width=True)

    # Job Postings by Gender
    st.markdown('''<h3>👨‍💻 توزيع الإعلانات حسب الجنس</h3>''', unsafe_allow_html=True)
    gender_distribution = jadarat_data['gender'].value_counts().reset_index()
    gender_distribution.columns = ['gender', 'count']
    fig2 = px.pie(gender_distribution, values='count', names='gender', title='توزيع الإعلانات حسب الجنس',
                  color_discrete_sequence=px.colors.sequential.Teal)
    st.plotly_chart(fig2, use_container_width=True)

    # Average Salary by Job Title
    st.markdown('''<h3>💼 متوسط الرواتب حسب العناوين الوظيفية</h3>''', unsafe_allow_html=True)
    avg_salary_by_job = jadarat_data.groupby('job_title')['Salary'].mean().reset_index()
    avg_salary_by_job = avg_salary_by_job.sort_values(by='Salary', ascending=False).head(10)
    fig3 = px.bar(avg_salary_by_job, x='job_title', y='Salary', title='متوسط الرواتب حسب العناوين الوظيفية',
                  color='Salary', color_continuous_scale='Viridis')
    st.plotly_chart(fig3, use_container_width=True)

def main():
    # Enhanced theme configuration
    modern_theme = {
        "background": "#f4f7fa",  # Softer light gray-blue
        "text_color": "#2c3e50",  # Darker slate for contrast
        "accent1": "#3498db",    # Vibrant blue
        "accent2": "#e67e22",    # Warm orange
        "accent3": "#2ecc71",    # Fresh green
        "hero_overlay": "rgba(52, 152, 219, 0.7)",
        "header_font": "'Tajawal', sans-serif",
        "recommendation_bg": "#34495e",
    }
    theme = modern_theme

    load_css(theme)
    hero_section(theme)
    info_sections()

    # Filters Section
    st.header('تصفية البيانات')
    
    col1, col2, col3 = st.columns(3)
    with col1:
        job_titles = jadarat_data['job_title'].unique()
        job_title = st.selectbox('اختر عنوان الوظيفة', job_titles)
    with col2:
        years_of_experience = st.number_input('عدد سنوات الخبرة', min_value=0, max_value=50, step=1, value=0)
    with col3:
        unique_genders = jadarat_data['gender'].unique()
        gender = st.selectbox('اختر الجنس', unique_genders)

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
