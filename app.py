import pandas as pd
import streamlit as st
import plotly.express as px

# Load data
jadarat_data = pd.read_csv("cleaned_Jadarat_data.csv")

# Normalize data: trim whitespace and convert to consistent case
jadarat_data['job_title'] = jadarat_data['job_title'].str.strip().str.lower()
jadarat_data['gender'] = jadarat_data['gender'].str.strip().str.lower()
jadarat_data['exper'] = pd.to_numeric(jadarat_data['exper'], errors='coerce')  # Ensure 'exper' is numeric

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
        /* Hero Section Styling */
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
        /* Price Card Styling */
        .price-card {{
            background: white;
            border-radius: 15px;
            padding: 1.5rem;
            margin: 1rem 0;
            border-right: 5px solid;
            color: {theme['text_color']};
            transition: transform 0.3s;
        }}
        .price-card:hover {{
            transform: scale(1.05);
        }}
        .price-card.apartment {{ border-color: {theme['accent1']}; }}
        .price-card.villa {{ border-color: {theme['accent2']}; }}
        .price-card.land {{ border-color: {theme['accent3']}; }}
        /* Comparison Box Styling */
        .comparison-box {{
            background: linear-gradient(135deg, #ffffff 0%, {theme['background']} 100%);
            border-radius: 20px;
            padding: 2rem;
            margin: 2rem 0;
            border: 1px solid #e9ecef;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }}
        /* Recommendation Box Styling */
        .recommendation-box {{
            background: {theme['recommendation_bg']};
            color: white;
            padding: 2rem;
            border-radius: 20px;
            margin: 2rem 0;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }}
        /* Example Section Styling */
        .example-section {{
            margin-top: 3rem;
            font-size: 1.8rem;
            line-height: 1.7;
        }}
        .example-section h2 {{
            font-size: 2.4rem;
            margin-bottom: 1rem;
            color: {theme['text_color']};
        }}
        .highlight {{
            font-weight: bold;
            color: {theme['accent1']};
            font-size: 1.9rem;
        }}
        /* Footer Styling */
        .footer {{
            text-align: center;
            padding: 2rem;
            background: {theme['background']};
            color: {theme['text_color']};
            font-size: 1.2rem;
        }}
        /* Filter Box Styling */
        .filter-box {{
            background: {theme['recommendation_bg']};
            color: white;
            padding: 2rem;
            border-radius: 20px;
            margin: 2rem 0;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }}
        /* Amazing Filter Result Styling */
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
    """Show information sections explaining the choices and add interactive graphs."""
    st.title('تحليل بيانات الوظائف في المملكة العربية السعودية')

    st.markdown('''<div class="content-container animate-content">
                    <h3>قمنا بتحليل البيانات المتعلقة بالإعلانات الوظيفية في السعودية،
                    وهدفنا هو تقديم نظرة شاملة على الوضع الوظيفي في المملكة من خلال تحليلات تتعلق بالرواتب، توزيع الوظائف حسب المناطق،
                    توزيع الوظائف حسب الخبرات المطلوبة، بالإضافة إلى توزيع عقود العمل.</h3>
                </div>''', unsafe_allow_html=True)

    # Proportion of Job Postings by Region
    st.markdown('''<h3 class="animate-content">🌍 توزيع الإعلانات الوظيفية حسب المناطق</h3>''', unsafe_allow_html=True)
    st.markdown('''<div class="content-container animate-content">
                    <h4>من خلال تحليل بيانات الوظائف، نلاحظ أن معظم الإعلانات الوظيفية تأتي من منطقة الرياض،
                    تليها مكة المكرمة والمنطقة الشرقية. بينما تكون المناطق الأخرى مثل عسير وتبوك وغيرها تساهم بنسب أقل بكثير في الإعلانات.</h4>
                </div>''', unsafe_allow_html=True)
    region_distribution = jadarat_data['region'].value_counts().reset_index()
    region_distribution.columns = ['region', 'count']
    fig1 = px.bar(region_distribution, x='region', y='count', title='توزيع الإعلانات الوظيفية حسب المناطق')
    st.plotly_chart(fig1, use_container_width=True)

    # Gender Preference in Job Postings
    st.markdown('''<h3 class="animate-content">👨‍💻 توزيع الإعلانات الوظيفية حسب الجنس</h3>''', unsafe_allow_html=True)
    st.markdown('''<div class="content-container animate-content">
                    <h4>هناك تفضيل واضح في بعض الإعلانات الوظيفية لاستقطاب جميع الأجناس (كلا الجنسين)،
                    بينما هناك بعض الوظائف المخصصة فقط للذكور أو الإناث. لكن بشكل عام، تهيمن الإعلانات التي تقبل كلا الجنسين.</h4>
                </div>''', unsafe_allow_html=True)
    gender_distribution = jadarat_data['gender'].value_counts().reset_index()
    gender_distribution.columns = ['gender', 'count']
    fig2 = px.pie(gender_distribution, values='count', names='gender', title='توزيع الإعلانات الوظيفية حسب الجنس')
    st.plotly_chart(fig2, use_container_width=True)

    # Average Salary by Job Title
    st.markdown('''<h3 class="animate-content">💼 متوسط الرواتب حسب العناوين الوظيفية</h3>''', unsafe_allow_html=True)
    st.markdown('''<div class="content-container animate-content">
                    <h4>نقوم هنا بعرض متوسط الرواتب لكل عنوان وظيفي في المملكة العربية السعودية.</h4>
                </div>''', unsafe_allow_html=True)

    avg_salary_by_job = jadarat_data.groupby('job_title')['Salary'].mean().reset_index()
    avg_salary_by_job = avg_salary_by_job.sort_values(by='Salary', ascending=False).head(10)  # Show top 10 job titles
    fig3 = px.bar(avg_salary_by_job, x='job_title', y='Salary', title='متوسط الرواتب حسب العناوين الوظيفية')
    st.plotly_chart(fig3, use_container_width=True)

    # Proportion of Job Postings for Fresh Graduates vs Experienced Candidates
    st.markdown('''<h3 class="animate-content">👩‍🎓 الإعلانات الوظيفية للخريجين الجدد مقابل الخبرات المطلوبة</h3>''', unsafe_allow_html=True)
    st.markdown('''<div class="content-container animate-content">
                    <h4>الوظائف الموجهة للخريجين الجدد هي الأكثر انتشارًا، حيث تشكل أكثر من نصف الإعلانات الوظيفية،
                    مقارنة بالإعلانات التي تطلب خبرات متعددة التي تشكل نسبة أقل بكثير.</h4>
                </div>''', unsafe_allow_html=True)
    experience_distribution = jadarat_data['exper'].value_counts().reset_index()
    experience_distribution.columns = ['experience', 'count']
    fig4 = px.bar(experience_distribution, x='experience', y='count', title='الإعلانات الوظيفية للخريجين الجدد مقابل الخبرات المطلوبة')
    st.plotly_chart(fig4, use_container_width=True)

    # Contract Type Distribution
    st.markdown('''<h3 class="animate-content">📝 توزيع نوع العقد في الإعلانات الوظيفية</h3>''', unsafe_allow_html=True)
    st.markdown('''<div class="content-container animate-content">
                    <h4>فيما يتعلق بنوع العقد، نجد أن غالبية الوظائف المعروضة هي بعقود دوام كامل،
                    بينما هناك عدد قليل من الوظائف التي تقدم عقودًا للعمل عن بعد.</h4>
                </div>''', unsafe_allow_html=True)
    contract_distribution = jadarat_data['contract'].value_counts().reset_index()
    contract_distribution.columns = ['contract_type', 'count']
    fig5 = px.pie(contract_distribution, values='count', names='contract_type', title='توزيع نوع العقد في الإعلانات الوظيفية')
    st.plotly_chart(fig5, use_container_width=True)

    # Conclusion
    st.markdown('''<h3 class="animate-content">💬 الخاتمة</h3>''', unsafe_allow_html=True)
    st.markdown('''<div class="content-container animate-content">
                    <h4>باستخدام هذا التحليل، يمكننا ملاحظة توجهات مهمة مثل التوزيع غير المتكافئ للإعلانات
                    الوظيفية بين المناطق في المملكة، بالإضافة إلى الرواتب التي تهيمن عليها الرواتب الأقل للخريجين الجدد.
                    كما أن تحليل الخبرات المطلوبة يبرز التحديات التي يواجهها الباحثون عن وظائف ذوي الخبرة. هذه الرؤية توفر لنا معطيات تساعدنا
                    في اتخاذ قرارات أكثر استراتيجية حول مستقبلنا المهني أو نوع الوظائف التي نرغب في التقديم لها.</h4>
                </div>''', unsafe_allow_html=True)

    # Prompt to check for specific job details
    st.markdown('''<h3 class="animate-content">🔍 تحقق من تفاصيل وظيفتك</h3>''', unsafe_allow_html=True)
    st.markdown('''<div class="content-container animate-content">
                    <h4>بعد مراجعة الرسوم البيانية، يمكنك الآن التحقق من تفاصيل وظيفتك المحددة. استخدم الفلاتر أدناه لاختيار عنوان الوظيفة، سنوات الخبرة، والجنس لعرض المعلومات المتعلقة بالوظيفة التي تهمك.</h4>
                </div>''', unsafe_allow_html=True)

def main():
    st.set_page_config(layout="wide", page_title="تحليل بيانات الوظائف في المملكة العربية السعودية")

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

    # Filters
    st.header('تصفية البيانات')
    job_titles = jadarat_data['job_title'].unique()
    job_title = st.selectbox('اختر عنوان الوظيفة', job_titles)
    years_of_experience = st.number_input('ادخل عدد سنوات الخبرة', min_value=0, max_value=50, step=1)
    gender = st.selectbox('اختر الجنس', ['كلا الجنسين', 'ذكر', 'أنثى'])

    # Normalize filter inputs
    job_title = job_title.strip().lower()
    gender = gender.strip().lower()

    # Filter data based on user input
    filtered_data = jadarat_data[
        (jadarat_data['job_title'].str.strip().str.lower() == job_title) &
        (jadarat_data['exper'] == years_of_experience) &
        (jadarat_data['gender'].str.strip().str.lower() == gender)
    ]

    # Debugging: Print filtered data and conditions
    st.write("Filtered Data:", filtered_data)
    st.write("Filter Conditions:", {
        "job_title": job_title,
        "years_of_experience": years_of_experience,
        "gender": gender
    })

    # Display filtered information in an amazing style if there is a match
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

    # Footer
    st.markdown('''<div class="footer">تم التحليل بواسطة مشعل الشقحاء | جميع الحقوق محفوظة 2025</div>''', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
