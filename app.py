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
    """Load custom CSS with colors defined by the chosen theme."""
    custom_css = f"""
    <style>
        .stApp {{
            background: {theme['background']};
            text-align: right;
            direction: rtl;
            color: {theme['text_color']};
            font-family: 'Tajawal', sans-serif;
        }}
        h1, h2, h3 {{
            font-family: {theme['header_font']};
            color: {theme['text_color']};
        }}
        .hero {{
            background: linear-gradient({theme['hero_overlay']}, {theme['hero_overlay']}),
                        url('https://images.unsplash.com/photo-1496171367470-9ed9a91ea931') center/cover;
            padding: 4rem 2rem;
            border-radius: 30px;
            margin: 2rem 0;
            text-align: center;
            animation: fadeIn 2s;
        }}
        @keyframes fadeIn {{
            from {{ opacity: 0; }}
            to {{ opacity: 1; }}
        }}
        .hero h1, .hero h3 {{
            animation: fadeIn 2s;
        }}
        .filter-result-box {{
            background: linear-gradient(135deg, {theme['accent1']} 0%, {theme['accent2']} 100%);
            color: white;
            padding: 2rem;
            border-radius: 20px;
            margin: 2rem 0;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
            text-align: center;
        }}
        .filter-result-box h3 {{
            font-size: 2.4rem;
            margin-bottom: 1rem;
        }}
        .filter-result-box p {{
            font-size: 1.8rem;
            margin: 0.5rem 0;
        }}
        .footer {{
            text-align: center;
            padding: 2rem;
            background: {theme['background']};
            color: {theme['text_color']};
            font-size: 1.2rem;
        }}
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap" rel="stylesheet">
    """
    st.markdown(custom_css, unsafe_allow_html=True)

def hero_section(theme):
    """Display the hero section with background image and title."""
    hero_html = f"""
    <div class="hero">
        <h1 style="color: white; text-shadow: 2px 2px 4px rgba(0,0,0,0.5);">
            📊 تحليل بيانات الوظائف في المملكة العربية السعودية
        </h1>
        <h3 style="color: white;">اكتشف التوجهات الوظيفية في المملكة</h3>
    </div>
    """
    st.markdown(hero_html, unsafe_allow_html=True)

def info_sections():
    """Show information sections with interactive graphs."""
    st.title('تحليل بيانات الوظائف في المملكة العربية السعودية')

    st.markdown('''<div>
                    <h3>قمنا بتحليل البيانات المتعلقة بالإعلانات الوظيفية في السعودية،
                    وهدفنا هو تقديم نظرة شاملة على الوضع الوظيفي من خلال تحليلات تتعلق بالرواتب،
                    توزيع الوظائف حسب المناطق ومستويات الخبرة، بالإضافة إلى توزيع عقود العمل.</h3>
                </div>''', unsafe_allow_html=True)

    # Job Postings by Region
    st.markdown('''<h3>🌍 توزيع الإعلانات الوظيفية حسب المناطق</h3>''', unsafe_allow_html=True)
    region_distribution = jadarat_data['region'].value_counts().reset_index()
    region_distribution.columns = ['region', 'count']
    fig1 = px.bar(region_distribution, x='region', y='count', title='توزيع الإعلانات حسب المناطق')
    st.plotly_chart(fig1, use_container_width=True)

    # Job Postings by Gender
    st.markdown('''<h3>👨‍💻 توزيع الإعلانات حسب الجنس</h3>''', unsafe_allow_html=True)
    gender_distribution = jadarat_data['gender'].value_counts().reset_index()
    gender_distribution.columns = ['gender', 'count']
    fig2 = px.pie(gender_distribution, values='count', names='gender', title='توزيع الإعلانات حسب الجنس')
    st.plotly_chart(fig2, use_container_width=True)

    # Average Salary by Job Title
    st.markdown('''<h3>💼 متوسط الرواتب حسب العناوين الوظيفية</h3>''', unsafe_allow_html=True)
    avg_salary_by_job = jadarat_data.groupby('job_title')['Salary'].mean().reset_index()
    avg_salary_by_job = avg_salary_by_job.sort_values(by='Salary', ascending=False).head(10)
    fig3 = px.bar(avg_salary_by_job, x='job_title', y='Salary', title='متوسط الرواتب حسب العناوين الوظيفية')
    st.plotly_chart(fig3, use_container_width=True)

def main():
    # Pastel theme configuration
    pastel_theme = {
        "background": "#fdf6e3",
        "text_color": "#657b83",
        "accent1": "#b58900",
        "accent2": "#cb4b16",
        "accent3": "#268bd2",
        "hero_overlay": "rgba(38, 139, 210, 0.4)",
        "header_font": "'Tajawal', sans-serif",
        "recommendation_bg": "#657b83",
    }
    theme = pastel_theme

    load_css(theme)
    hero_section(theme)
    info_sections()

    # Filters Section
    st.header('تصفية البيانات')
    
    job_titles = jadarat_data['job_title'].unique()
    job_title = st.selectbox('اختر عنوان الوظيفة', job_titles)
    
    years_of_experience = st.number_input('ادخل عدد سنوات الخبرة', min_value=0, max_value=50, step=1, value=0)
    
    unique_genders = jadarat_data['gender'].unique()
    gender = st.selectbox('اختر الجنس', unique_genders)

    # Filter data
    filtered_data = jadarat_data[
        (jadarat_data['job_title'] == job_title) &
        (jadarat_data['exper'] == int(years_of_experience)) &
        (jadarat_data['gender'] == gender)
    ]

    # Debugging Output
    st.write("### معلومات التصحيح")
    st.write(f"عنوان الوظيفة المختار: '{job_title}'")
    st.write(f"سنوات الخبرة المختارة: {years_of_experience}")
    st.write(f"الجنس المختار: '{gender}'")
    st.write("عدد النتائج المطابقة:", len(filtered_data))

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
        </div>
        ''', unsafe_allow_html=True)
    else:
        st.markdown('''
        <div class="filter-result-box">
            <h3>لا توجد نتائج مطابقة</h3>
            <p>لم يتم العثور على وظائف تطابق المعايير المحددة. يرجى التحقق من الفلاتر وإعادة المحاولة.</p>
        </div>
        ''', unsafe_allow_html=True)
        st.write("البيانات المصفاة (للتصحيح):", filtered_data)

    # Footer
    st.markdown('''<div class="footer">تم التحليل بواسطة مشعل الشقحاء | جميع الحقوق محفوظة 2025</div>''', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
