import streamlit as st
#from streamlit_card import card
import pandas as pd
import os

# Detect theme preference
theme = st.get_option("theme.base")
if theme == "dark":
    bg_color = "#1e1b29"
    primary_color = "#6c6780"
else:
    bg_color = "#d9d4e7"
    primary_color = "#9692a1"

css = f"""
<style>
    /* Set right-to-left direction and custom font */
    html, body {{
        background-color: {bg_color};
        direction: rtl;
        text-align: right;
        font-family: 'Tajawal', sans-serif;
    }}
    [data-testid="stAppViewContainer"] {{
       background-color: {bg_color};
      
    }}
[data-testid="stHeader"] {{
       background-color: {bg_color};

    }}
    .stSelectbox select:focus {{
        border-color: {primary_color} ;  /* Change border color on focus */
        outline: none !important;  /* Remove default outline */
    }}

    /* Style for Streamlit buttons */
    .stButton>button {{
        background-color: {primary_color};
        color: white;
    }}

    /* Custom paragraph styles */
    .custom-paragraph {{
        font-size: 18px !important;
        line-height: 1.6;
        color: #3e3c40;
    }}

    /* Header colors */
    h1, h2, h3, h4, h5, h6 {{
        background-color: rgba(230, 230, 230, 0.3);
        color: #3e3c40;
    }}

    /* Custom hover effect for dropdown options */
    div[data-baseweb="select"] ul li:hover {{
        background-color: #f7b2a5 !important;  /* Hover background color */
        color: white;                        /* Hover text color */
    }}
</style>
"""


jadarat = pd.read_csv('jadarat_cleaned.csv')

st.markdown(css, unsafe_allow_html=True)

st.title("من الجامعة إلى العالم الحقيقي: الخريجون والبحث عن الوظائف👩🏻‍🎓👨🏻‍🎓")

col1, col2 = st.columns([7, 5])

with col1:
    img = os.path.join('imgs', 'grads-removebg-preview.png')
    st.image(img)
    

with col2:
    # Apply custom styling to the paragraph using the 'custom-paragraph' class
    st.markdown('<p class="custom-paragraph">منذ نعومة أظافرنا ونحن نخطو خطواتٌ مدروسة ممن هم أكبر منا ونتعلم من خبرات من سبقونا. نتعلم في مجموعاتٍ تشبهنا وندرس معًا المواد الدراسية نفسها، ثم ننتقل إلى الجامعة، حيث يقل تشابهننا، وتختلف تخصصاتنا، فنلتقي يمن يختلف عنا. وبعد الجامعة، تنفكُّ أيدينا عن أيدي من أرشدونا طيلة الثلاثة والعشرين عامًا الماضية، ونبدأ أولى خطواتنا في العالم الحقيقي، بين من هم أكثر منا خبرة، ومن هم أقل، ومن يشبهوننا. ورغم كل هذه الاختلافات، نشترك جميعًا في مهمة شاقة واحدة: البحث عن وظيفة. في هذا العالم الواسع، قد تجد نفسك وحيدًا تبحث عمّن يرشدك، وهنا نحن مع بيانات منصة جدارات حللناها لنرشدك.</p>', unsafe_allow_html=True)
 


st.markdown('<h2> سوق العمل يطلب حديثي التخرج و الأشخاص بلا خبرة!</h2>', unsafe_allow_html=True)
st.image(os.path.join('imgs','st1.png'))
st.markdown('<p class="custom-paragraph">الخبرة من المشاكل المؤرقة أثناء البحث عن العمل لكن بيانات منصة جدارات تبين أن السوق يطلب حديثي التخرج والأشخاص بلا خبرة في عدة مجالات منها: بائع، موظف استقبال، مندوب مبيعات، وغيرها لكن ماذا عن الوظائف التي تتطلب شهادات جامعية؟</p>', unsafe_allow_html=True)

st.markdown('<h3>وظائف حديثي التخرج في سوق العمل: يتربع على عرشها الوظائف الإدارية</h3>', unsafe_allow_html=True)
st.image(os.path.join('imgs','st2.png'))
st.markdown('<p class="custom-paragraph">على ما يبدو أن التخصصات الإدارية تدير الأعمال وسوق العمل بنفسه! فنلاحظ أن  المحاسبين واخصائي التسويق هم الأكثر طلبًا في عامي 2022-2023</p>', unsafe_allow_html=True)

st.markdown('<h2> لا تحيزات في سوق العمل!</h2>', unsafe_allow_html=True)
st.image(os.path.join('imgs','jobposting2.png'))
st.markdown('<p class="custom-paragraph">قد يتبادر لأذهان البعض أسئلة عما إذا كان جنسه سيؤثر في حصوله على الوظيفة. ماذا إن كان إحدى التخصصات يفضل جنسٌ على آخر؟ ماذا لو أن البعض يرى أن الجنس المعاكس يسرق فرصه في العمل؟ <b>الحقيقة</b> البيانات تظهر عكس هذه المخاوف! توجد اختلافات بسيطة لا تذكر والنتيجة هي لا توجد تحيزات لجنسٍ على آخر في سوق العمل</p>', unsafe_allow_html=True)

st.markdown("<h2>الربع الأخير من السنة: منجم الفرص الوظيفية!</h2>" , unsafe_allow_html=True)
st.image(os.path.join('imgs', 'last_quarter.png'))
st.markdown('<p class="custom-paragraph">تنتهي سنة 2022 مع نوفمبر وديسمبر ونرى ذروة إعلانات التوظيف فيهما وتقدمهما على الشهر الأول من الربع الأول لسنة 2023!</p>', unsafe_allow_html=True)

st.markdown("""
    <h2 style="font-family: 'Arial', sans-serif; text-align: center;">
        والآن أيها الخريج، سمِّ بربِّ البداياتِ، وابحث عن وظيفتك، واشحذ سيف مهاراتك، واسعَ إليها.
    </h2>
""", unsafe_allow_html=True)

degree_required_jobs = [
    'محاسب', 'أخصائي عمليات موارد بشرية', 'مدير مكتب', 'أخصائي إدارة مشاريع', 'مصمم جرافيك', 
    'مدير حساب عميل', 'مطور برامج', 'أخصائي إدارة اداء', 'كيميائي', 'مهندس زراعي', 'مدير عام', 
    'كاتب علاقات حكومية', 'مهندس كهربائي', 'مهندس ميكانيكي', 'أخصائي تسويق',
    'صيدلي', 'مدير رقابة ادارية', 'مدير تسويق', 'مدير تدريب', 'محلل نظم المعلومات',
    'أخصائي توظيف', 'أخصائي تغذية', 'مهندس مواد', 'طبيب أسنان عام', 'أخصائي مختبرات طبية', 
    'محامي', 'أخصائي سمعيات', 'مهندس معماري', 'أخصائي قانوني', 'أخصائي شؤون قانونية',
    'أخصائي تقنية إشعاعية', 'مدير برمجيات', 'أخصائي علوم حشرات', 'أخصائي إعلامي', 'أخصائي مبيعات مستلزمات طبية', 
    'أخصائي بصريات', 'مراجع داخلي', 'مدير موارد بشرية أمن سيبراني', 'مبرمج تطبيقات', 'مهندس صناعي', 
    'أخصائي علاقات عامة', 'مدير بحث وتطوير', 'مهندس كيميائي', 'مهندس بيئي', 'مهندس تقنية معلومات', 
    'مهندس إدارة مشاريع', 'أخصائي تأمين', 'رئيس منظمة غير ربحية', 'أخصائي أمراض نطق وسمع', 
    'مدير إدارة مشاريع'
]

# Filter the dataframe to only include jobs in the degree_required_jobs list
filtered_df = jadarat[jadarat['job_title'].isin(degree_required_jobs)]

# Get unique job titles from the filtered dataframe
unique_jobs = filtered_df['job_title'].unique()

# Dropdown list (selectbox) for unique jobs based on the filtered dataframe
selected_job = st.selectbox("اختر وظيفتك", unique_jobs)

experience_label = st.radio("اختر الخبرة المطلوبة:", ('لا تتطلب خبرة', 'تتطلب خبرة'))
experience_value = 0 if experience_label == 'لا تتطلب خبرة' else 1


# Search button
if st.button('جد وظيفتي', key='search_button'):
    # Filter jobs based on the user's input
    if experience_value == 0:
        result = jadarat[(jadarat['job_title'] == selected_job) & (jadarat['experience (Years)'] == 0)]
    else:
        result = jadarat[(jadarat['job_title'] == selected_job) & (jadarat['experience (Years)'] != 0)]

    # Display results
    if result.empty:
        st.warning("لا توجد وظيفة مطابقة للمتطلبات المختارة")
    else:
        st.success(f"عُثِر على {len(result)} وظيفة")
        # Create dynamic job cards
        for i, row in result.iterrows():
            gender_label = 'إناث' if row['gender'] == 'F' else 'ذكور' if row['gender'] == 'M' else 'الاثنان'
            with st.container():
                st.markdown(
                    f"""
                    <div style="background-color: #eee; padding: 20px; border-radius: 15px; margin-bottom: 15px;">
                        <h3 style="color: #9692a1;">{row['job_title']}</h3>
                        <p><b>الشركة:</b> {row['comp_name']}</p>
                        <p><b>الوصف الوظيفي:</b> {row['job_desc']}</p>
                        <p><b>المؤهلات:</b> {row['qualifications_corrected']}</p>
                        <p><b>الخبرة المطلوبة:</b> {'لا تتطلب خبرة' if row['experience (Years)'] == 0 else row['experience (Years)']}</p>
                        <p><b>الجنس:</b> {gender_label}</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

