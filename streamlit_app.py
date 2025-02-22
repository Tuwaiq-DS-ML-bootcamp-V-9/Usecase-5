import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import arabic_reshaper
from bidi.algorithm import get_display
import time
import random

# Function to fix Arabic labels for correct display
def fix_arabic_labels(labels):
    """
    Fix Arabic labels for correct display in visualizations.

    Parameters:
        labels (list or pd.Index): List of Arabic text labels.

    Returns:
        list: List of fixed Arabic labels.
    """
    return [get_display(arabic_reshaper.reshape(str(label))) for label in labels]

# Set page configuration
st.set_page_config(page_title="دليل الخريجين للوظائف", layout="wide")

# تحسين التصميم العام باستخدام الألوان المحددة
st.markdown(
    """
    <style>
    /* تغيير لون خلفية الصفحة الرئيسية */
    .stApp {
        background-color: #000000;  /* لون خلفية الصفحة */
    }
    body {
        direction: rtl;
        text-align: right;
        font-family: 'Cairo', sans-serif;
        color: #FFFFFF;  /* لون النص الرئيسي */
    }
    .title {
        font-size: 3em;  /* تكبير العنوان الرئيسي */
        font-weight: bold;
        text-align: center;
        color: #FFA500;  /* لون العنوان الرئيسي */
    }
    .highlight {
        color: #FF8C00;  /* لون النصوص المميزة */
        font-weight: bold;
        font-size: 1.2em;  /* تكبير النصوص المميزة */
    }
    .subtitle {
        font-size: 2em;  /* تكبير العناوين الفرعية */
        font-weight: bold;
        color: #FFA500;  /* لون العناوين الفرعية */
    }
    .divider-custom {
        border-top: 3px solid #FF8C00;  /* لون الفواصل */
        margin: 20px 0;
    }
    p {
        font-size: 1.4em;  /* تكبير النصوص العادية */
        color: #FFFFFF;  /* لون النص العادي */
    }
    .container {
        background-color: #1E1E1E;  /* لون خلفية الحاويات */
        padding: 20px;
        border-radius: 10px;
        margin: 20px 0;  /* زيادة المسافة بين الحاويات */
        box-shadow: 0 4px 8px rgba(255, 165, 0, 0.2);  /* إضافة ظل برتقالي للحاويات */
    }
    .notification {
        background-color: #2E2E2E;  /* لون خلفية الإشعارات */
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        border-left: 5px solid #FF8C00;  /* لون الحدود الجانبية */
    }
    .stTable {
        background-color: #1E1E1E;  /* لون خلفية الجداول */
        border-radius: 10px;  /* حواف مستديرة للجداول */
        padding: 10px;
    }
    .stDataFrame {
        background-color: #1E1E1E;  /* لون خلفية الجداول */
        border-radius: 10px;  /* حواف مستديرة للجداول */
        padding: 10px;
    }
    .stButton button {
        background-color: #FFA500;  /* لون خلفية الأزرار */
        color: #000000;  /* لون النص في الأزرار */
        border-radius: 5px;  /* حواف مستديرة للأزرار */
        padding: 10px 20px;
        font-size: 1.2em;
    }
    .stButton button:hover {
        background-color: #FF8C00;  /* لون خلفية الأزرار عند التمرير */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.markdown('<p class="title">🚀 دليل الخريجين للوظائف في المملكة العربية السعودية</p>', unsafe_allow_html=True)

# Load the dataset
@st.cache_data  # Cache the data to improve performance
def load_data():
    try:
        data = pd.read_csv("cleaned_data.csv")
        return data
    except FileNotFoundError:
        st.error("الملف 'cleaned_data.csv' غير موجود. يرجى التأكد من وجود الملف في المسار الصحيح.")
        return pd.DataFrame()  # Return an empty DataFrame if file not found

df = load_data()

# Check if data is loaded successfully
if df.empty:
    st.stop()  # Stop the app if data is not loaded

# Sidebar for filters
st.sidebar.header("الفلاتر")
region_filter = st.sidebar.multiselect(
    "اختر المناطق", 
    df["region"].unique()
)
gender_filter = st.sidebar.multiselect("اختر الجنس", df["gender"].unique())

# Apply filters
if region_filter:
    df = df[df["region"].isin(region_filter)]
if gender_filter:
    df = df[df["gender"].isin(gender_filter)]

# Introduction
with st.container():
    st.markdown("""
        <div style="background-color: #1E1E1E; padding: 20px; border-radius: 10px;">
            <p class="highlight">## 🎓 مرحباً بك في دليل الخريجين للوظائف!</p>
            <p class="highlight">أنت خريج جديد تبحث عن فرصة عمل لبدء مسيرتك المهنية. هذا التطبيق سيساعدك على فهم سوق العمل في المملكة العربية السعودية واتخاذ قرارات مدروسة.</p>
        </div>
    """, unsafe_allow_html=True)

# مسافة بين الفقرات
st.markdown("<br><br>", unsafe_allow_html=True)

# عبارات محفزة داخل حاوية
with st.container():
    st.markdown("""
        <div style="background-color: #2E2E2E; padding: 20px; border-radius: 10px;">
            <p class="highlight">✨ "النجاح يبدأ بخطوة واحدة.. ابدأ الآن!"</p>
            <p class="highlight">💼 "كل وظيفة هي فرصة جديدة لبناء مستقبل مشرق."</p>
            <p class="highlight">🌟 "لا تنتظر الفرصة، اصنعها بنفسك."</p>
        </div>
    """, unsafe_allow_html=True)

# مسافة بين الفقرات
st.markdown("<br><br>", unsafe_allow_html=True)

# مقدمة مشوقة داخل حاوية
with st.container():
    st.markdown("""
        <div style="background-color: #E9EDC9; padding: 20px; border-radius: 10px;">
            ## 🚀 مقدمة مشوقة: لماذا هذا التطبيق؟
            "أنت خريج جديد، تبحث عن فرصتك الأولى في سوق العمل؟ 🤔 تريد معرفة توقعات الرواتب، وأين تتركز الوظائف، وما هي الفرص المتاحة حسب الخبرة؟ 🎯"

            هذا الدليل التفاعلي سيساعدك في اتخاذ قرارات مدروسة حول مستقبلك المهني في السعودية. استعد لاستكشاف بيانات مفيدة حول الرواتب، المناطق، ومتطلبات سوق العمل.

            ### 💰 ما هو نطاق الرواتب المتوقع؟
            هل لديك فضول حول الرواتب التي يمكن أن تتوقعها كخريج جديد؟ 🤓

            - استعرض مخطط الراتب لتفهم التوزيع العام للرواتب.
            - تصفح الإحصائيات لمعرفة الحد الأدنى، المتوسط، والحد الأقصى للأجور.
            - استخدم الفلاتر لتحديد الرواتب بناءً على منطقتك أو مجالك.

            **🔍 المعرفة قوة – وفهم نطاق الرواتب يساعدك في تحديد توقعاتك أثناء البحث عن وظيفة!**

            ### 🎓 هل هناك فرص للخريجين الجدد؟
            أحيانًا يظن الناس أن الوظائف متاحة فقط لأصحاب الخبرة، لكن هل هذا صحيح؟ 🤔

            من خلال هذا التحليل، ستتمكن من معرفة عدد الفرص المتاحة للخريجين الجدد مقارنةً بأصحاب الخبرة. قد تتفاجأ بالنتائج! 😯

            ### 📍 أين تجد أكثر الوظائف؟
            الفرص ليست متساوية في كل مكان، بعض المناطق تزدهر بالوظائف بينما غيرها قد يكون أقل نشاطًا.

            - هل الرياض هي الوجهة المثالية؟
            - ماذا عن جدة أو الدمام؟
            - أين يجب أن تركز بحثك عن الوظائف؟

            اكتشف خريطة توزيع الوظائف في السعودية بناءً على البيانات الحقيقية. 🗺️
        </div>
    """, unsafe_allow_html=True)


# مسافة بين الفقرات
st.markdown("<br><br>", unsafe_allow_html=True)

# Progress Bar for Loading
with st.container():
    with st.spinner("جارٍ تحميل البيانات..."):
        progress_bar = st.progress(0)
        for i in range(100):
            progress_bar.progress(i + 1)
        st.success("تم تحميل البيانات بنجاح!")

# مسافة بين الفقرات
st.markdown("<br><br>", unsafe_allow_html=True)

# Section 1: Salary Range for Fresh Graduates
with st.container():
    st.markdown("""
        <div style="background-color: #1E1E1E; padding: 20px; border-radius: 10px;">
            <h2 style="color: #FFA500;">💰 نطاق الراتب المتوقع للخريجين الجدد</h2>
            <p class="highlight">ما هو نطاق الراتب المتوقع للخريجين الجدد؟ هذا سيساعدك على تحديد التوقعات المالية.</p>
        </div>
    """, unsafe_allow_html=True)

    # Filter data for fresh graduates
    fresh_graduates = df[df['exper'] == '0 Years']

    # Use Columns for Layout
    col1, col2 = st.columns(2)

    with col1:
        # Histogram
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.histplot(fresh_graduates['Salary'], kde=True, color='#FFA500', ax=ax)
        ax.set_xlabel(get_display(arabic_reshaper.reshape("الراتب")))
        ax.set_ylabel(get_display(arabic_reshaper.reshape("التكرار")))
        ax.set_title(get_display(arabic_reshaper.reshape("نطاق الراتب المتوقع لخريجي الجدد")))
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        st.pyplot(fig)

    with col2:
        # Table
        st.markdown("""
            <div style="background-color: #1E1E1E; padding: 20px; border-radius: 10px;">
                <h3 style="color: #FFA500;">جدول نطاق الراتب المتوقع</h3>
            </div>
        """, unsafe_allow_html=True)
        salary_summary = fresh_graduates['Salary'].describe().rename({
            "count": "عدد",
            "mean": "متوسط",
            "std": "انحراف معياري",
            "min": "الحد الأدنى",
            "25%": "25%",
            "50%": "50%",
            "75%": "75%",
            "max": "الحد الأقصى"
        })
        st.table(salary_summary.reset_index().rename(columns={"index": "الإحصائية", "Salary": "القيمة"}))

# مسافة بين الفقرات
st.markdown("<br><br>", unsafe_allow_html=True)

# Section 2: Job Opportunities by Experience Level
with st.container():
    st.markdown("""
        <div style="background-color: #1E1E1E; padding: 20px; border-radius: 10px;">
            <h2 style="color: #FFA500;">🎓 فرص العمل حسب مستوى الخبرة</h2>
            <p class="highlight">هل فرص العمل موجهة أكثر للأفراد ذوي الخبرة أم أن هناك فرصاً للخريجين الجدد؟</p>
        </div>
    """, unsafe_allow_html=True)

    # Calculate experience counts
    experience_counts = df['exper'].value_counts()

    # Use Columns for Layout
    col1, col2 = st.columns(2)

    with col1:
        # Bar Plot
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.barplot(x=experience_counts.values, y=fix_arabic_labels(experience_counts.index), palette="Oranges", ax=ax)
        ax.set_xlabel(get_display(arabic_reshaper.reshape("عدد الوظائف")))
        ax.set_ylabel(get_display(arabic_reshaper.reshape("مستوى الخبرة")))
        ax.set_title(get_display(arabic_reshaper.reshape("فرص العمل حسب مستوى الخبرة")))
        plt.grid(axis='x', linestyle='--', alpha=0.7)
        st.pyplot(fig)

    with col2:
        # Table
        st.markdown("""
            <div style="background-color: #1E1E1E; padding: 20px; border-radius: 10px;">
                <h3 style="color: #FFA500;">جدول فرص العمل حسب مستوى الخبرة</h3>
            </div>
        """, unsafe_allow_html=True)
        st.table(experience_counts.reset_index().rename(columns={"index": "مستوى الخبرة", "exper": "عدد الوظائف"}))

# مسافة بين الفقرات
st.markdown("<br><br>", unsafe_allow_html=True)

# Section 3: Job Postings by Region
with st.container():
    st.markdown("""
        <div style="background-color: #1E1E1E; padding: 20px; border-radius: 10px;">
            <h2 style="color: #FFA500;">📍 توزيع الوظائف حسب المنطقة</h2>
            <p class="highlight">لنبدأ باستكشاف المناطق التي تتركز فيها فرص العمل. هذا سيساعدك على تحديد أفضل المناطق للبحث عن وظيفة.</p>
        </div>
    """, unsafe_allow_html=True)

    # Calculate region counts
    region_counts = df['region'].value_counts()

    # Use Columns for Layout
    col1, col2 = st.columns(2)

    with col1:
        # Bar Plot
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.barplot(x=region_counts.values, y=fix_arabic_labels(region_counts.index), palette="Oranges", ax=ax)
        ax.set_xlabel(get_display(arabic_reshaper.reshape("عدد الوظائف")))
        ax.set_ylabel(get_display(arabic_reshaper.reshape("المنطقة")))
        ax.set_title(get_display(arabic_reshaper.reshape("توزيع الوظائف حسب المنطقة")))
        plt.grid(axis='x', linestyle='--', alpha=0.7)
        st.pyplot(fig)

    with col2:
        # Table
        st.markdown("""
            <div style="background-color: #1E1E1E; padding: 20px; border-radius: 10px;">
                <h3 style="color: #FFA500;">جدول توزيع الوظائف حسب المنطقة</h3>
            </div>
        """, unsafe_allow_html=True)
        st.table(region_counts.reset_index().rename(columns={"index": "المنطقة", "region": "عدد الوظائف"}))

# مسافة بين الفقرات
st.markdown("<br><br>", unsafe_allow_html=True)

# Footer
with st.container():
    st.markdown("---")
    st.markdown("📊 **شكراً لك على استخدام دليل الخريجين للوظائف! نتمنى لك التوفيق في مسيرتك المهنية.**")

# إشعارات تحفيزية كل 30 ثانية
if 'notification_time' not in st.session_state:
    st.session_state.notification_time = time.time()

if time.time() - st.session_state.notification_time > 30:  # كل 30 ثانية
    motivational_messages = [
        "✨ النجاح يبدأ بخطوة واحدة.. ابدأ الآن!",
        "💼 كل وظيفة هي فرصة جديدة لبناء مستقبل مشرق.",
        "🌟 لا تنتظر الفرصة، اصنعها بنفسك.",
        "🚀 المستقبل يبدأ بقرار ذكي.. خذ خطوتك الآن!",
        "📊 البيانات هي مفتاح اتخاذ القرارات الصحيحة.",
        "💡 كل يوم هو فرصة جديدة لتحقيق النجاح.",
        "🌈 النجاح ليس وصولاً، بل رحلة مستمرة.",
    ]
    selected_message = random.choice(motivational_messages)
    st.markdown(f'<div class="notification">{selected_message}</div>', unsafe_allow_html=True)
    st.session_state.notification_time = time.time()  # إعادة ضبط المؤقت