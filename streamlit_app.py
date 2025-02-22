import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import arabic_reshaper
from bidi.algorithm import get_display
import matplotlib.patches as mpatches


# ✅ تحميل البيانات مباشرة والتحقق من وجود الملف
try:
    Jadarat = pd.read_excel("Cleaned_Jadarat.xlsx")
except FileNotFoundError:
    st.error("❌ لم يتم العثور على ملف 'Cleaned_Jadarat.xlsx'! تأكد من وجود الملف في نفس المجلد.")
    st.stop()


st.set_page_config(layout="wide")


import streamlit as st

# ✅ Apply the custom CSS for styling
st.markdown(
    """
    <style>
    .styled-text {
        font-family: 'Arial', sans-serif; /* Match the font style */
        font-size: 24px; /* Adjusted size */
        color: #5A6B6E; /* Extracted text color */
        font-weight: bold;
        text-align: center; /* Right align for Arabic */
        direction: rtl;
        padding: 15px;
        border-radius: 10px; /* Smooth rounded edges */
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    .styled-text1 {
        font-family: 'Arial', sans-serif; /* Match the font style */
        font-size: 24px; /* Adjusted size */
        color: #5A6B6E; /* Extracted text color */
        font-weight: bold;
        text-align: right; /* Right align for Arabic */
        direction: rtl;
        padding: 15px;
        border-radius: 10px; /* Smooth rounded edges */
    }
    </style>
    """,
    unsafe_allow_html=True
)




st.markdown("<h1 style='text-align: center; direction: rtl;'> من التخرج إلى النجاح المهني 🚀 !</h1>", unsafe_allow_html=True)

# ✅ تعديل تغيير لون الخلفية بشكل صحيح
st.markdown(
    """
    <style>
    .stApp {
        background-color: #F5E8D8; /* لون بيج فاتح */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ✅ وضع الصورة كهيدر كامل
st.markdown(
    """
    <style>
        .header-img {
            width: 100%;
            height: auto;
        }
    </style>
    <img class='header-img' src='https://carterwellington.com/wp-content/uploads/2024/05/ksa-page-1024x256.jpg'>
    """,
    unsafe_allow_html=True
)

# ✅ توسيط النص وتحسين التنسيق



st.markdown(
    """
    <div class="styled-text">

إذا كنت **حديث تخرج** وتبحث عن فرصة عمل في السعودية، فـ **جدارات** هي بوابتك الأولى للانطلاق! 🎓💼 

هنا ستجد كل التفاصيل اللي تحتاجها لبداية مسارك المهني بثقة وراحة بال.

✅ 🔍 **أكثر الوظائف طلبًا لحديثي التخرج في مختلف مناطق السعودية**
✅ 💰 **متوسط الرواتب لكل قطاع وظيفي عبر منصة جدارات**
🔥 باستخدام **البيانات والتحليل**، تقدر تختار الوظيفة الأنسب لك وتبدأ مشوارك المهني بأفضل طريقة! 💡
    </div>
    """,
    unsafe_allow_html=True
)



# first chart
# ✅ التأكد من وجود عمود الوظائف
if "job_title" in Jadarat.columns:
    # 🔄 إصلاح النصوص العربية
    Jadarat["job_title_fixed"] = Jadarat["job_title"].astype(str).apply(lambda x: get_display(arabic_reshaper.reshape(x)))

    # 📊 حساب أكثر الوظائف طلبًا
    job_counts_fixed = Jadarat["job_title_fixed"].value_counts().head(10)

    # 🎨 إعداد النصوص العربية
    title_text = get_display(arabic_reshaper.reshape("📊 أكثر الوظائف طلبًا في مختلف مناطق السعودية"))
    xlabel_text = get_display(arabic_reshaper.reshape("عدد الوظائف"))
    ylabel_text = get_display(arabic_reshaper.reshape("المسمى الوظيفي"))

    # 🎨 رسم المخطط البياني مع دعم الخط العربي
    fig, ax = plt.subplots(figsize=(10, 5))
    bars = ax.barh(job_counts_fixed.index, job_counts_fixed.values, color="steelblue")

    # إضافة الأرقام على أشرطة البيانات
    for bar in bars:
        ax.text(bar.get_width(), bar.get_y() + bar.get_height()/2, str(int(bar.get_width())), va='center', ha='left', fontsize=12, fontweight="bold")

    ax.set_xlabel(xlabel_text, fontsize=12, fontweight="bold")
    ax.set_ylabel(ylabel_text, fontsize=12, fontweight="bold")
    ax.set_title(title_text, fontsize=14, fontweight="bold")
    ax.invert_yaxis()  # جعل أكثر الوظائف طلبًا في الأعلى

    # 🚀 عرض المخطط البياني في Streamlit
    st.pyplot(fig)
else:
    st.error("❌ لم يتم العثور على عمود 'job_title' في الملف.")

# ✅ التأكد من وجود عمود الوظائف
if "job_title" in Jadarat.columns:
    # 🔄 إصلاح النصوص العربية
    Jadarat["job_title_fixed"] = Jadarat["job_title"].astype(str).apply(lambda x: get_display(arabic_reshaper.reshape(x)))

    # 📊 حساب أكثر الوظائف طلبًا
    job_counts_fixed = Jadarat["job_title_fixed"].value_counts().head(10)

    # 🎨 إعداد النصوص العربية
    title_text = get_display(arabic_reshaper.reshape("📊 أكثر الوظائف طلبًا في مختلف مناطق السعودية"))
    xlabel_text = get_display(arabic_reshaper.reshape("عدد الوظائف"))
    ylabel_text = get_display(arabic_reshaper.reshape("المسمى الوظيفي"))

    # 🎨 رسم المخطط البياني مع دعم الخط العربي
    fig, ax = plt.subplots(figsize=(10, 5))
    bars = ax.barh(job_counts_fixed.index, job_counts_fixed.values, color="steelblue")

    # إضافة الأرقام على أشرطة البيانات
    for bar in bars:
        ax.text(bar.get_width(), bar.get_y() + bar.get_height()/2, str(int(bar.get_width())), va='center', ha='left', fontsize=12, fontweight="bold")

    ax.set_xlabel(xlabel_text, fontsize=12, fontweight="bold")
    ax.set_ylabel(ylabel_text, fontsize=12, fontweight="bold")
    ax.set_title(title_text, fontsize=14, fontweight="bold")
    ax.invert_yaxis()  # جعل أكثر الوظائف طلبًا في الأعلى

    # 🚀 عرض المخطط البياني في Streamlit
    st.pyplot(fig)
else:
    st.error("❌ لم يتم العثور على عمود 'job_title' في الملف.")



# ✅ عنوان التحليل
st.markdown("<h1 style='text-align: center; color: blue;'>📊 تحليل سوق العمل في السعودية</h1>", unsafe_allow_html=True)



# ✅ عرض الإحصائيات الرئيسية
st.markdown(
    """
        <div class="styled-text">

    ### 🔍 **أهم الملاحظات من البيانات:**
    ✔️ **قطاع المبيعات والمحاسبة والإدارة يشكلون الجزء الأكبر من الوظائف المطلوبة.**  
    ✔️ **الشركات تركز على تعزيز فرق المبيعات والتسويق لتحسين الأداء التجاري.**  
    ✔️ **الموارد البشرية والمحاسبة لا تزال ذات أهمية، لكن ليست بنفس مستوى المبيعات.**  
    ✔️ **الوظائف التقليدية مثل السكرتارية بدأت تفقد بعض الاهتمام مقارنة بالوظائف التقنية والإدارية المتقدمة.**  

    🔥 **إذا كنت تبحث عن وظيفة، فإن المهارات في المبيعات، الإدارة، والمحاسبة تمنحك فرصًا أكبر في السوق! 🚀**
        </div>

    """, unsafe_allow_html=True
)




# ✅ التأكد من وجود الأعمدة المطلوبة
if "job_title" in Jadarat.columns:
    # 🔄 إصلاح النصوص العربية بشكل صحيح
    Jadarat["job_title_fixed"] = Jadarat["job_title"].astype(str).apply(lambda x: get_display(arabic_reshaper.reshape(x.strip())))

    # 🎯 فرز الوظائف وعرضها بالشكل الصحيح
    unique_jobs = sorted(Jadarat["job_title_fixed"].unique(), key=lambda x: x[::-1])
    selected_jobs = st.multiselect(
        "🔍 اختر الوظائف التي تريد عرضها:",
        unique_jobs,
        default=unique_jobs[:5],
        format_func=lambda x: get_display(arabic_reshaper.reshape(x))
    )

    # 🔽 تصفية البيانات بناءً على الاختيار
    filtered_data = Jadarat[Jadarat["job_title_fixed"].isin(selected_jobs)]

    # 📊 حساب عدد الوظائف لكل مسمى وظيفي
    job_counts_fixed = filtered_data["job_title_fixed"].value_counts().head(10)

    # 🎨 إعداد النصوص العربية
    title_text = get_display(arabic_reshaper.reshape("📊 أكثر الوظائف طلبًا في مختلف مناطق السعودية"))
    xlabel_text = get_display(arabic_reshaper.reshape("عدد الوظائف"))
    ylabel_text = get_display(arabic_reshaper.reshape("المسمى الوظيفي"))

    # 🎨 إنشاء المخطط باستخدام Seaborn
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(y=job_counts_fixed.index, x=job_counts_fixed.values, palette="Blues_r", ax=ax)

    # ✅ إضافة عدد الوظائف فوق كل شريط
    for index, value in enumerate(job_counts_fixed.values):
        ax.text(value, index, str(value), va='center', ha='left', fontsize=12, fontweight="bold")

    ax.set_xlabel(xlabel_text, fontsize=12, fontweight="bold")
    ax.set_ylabel(ylabel_text, fontsize=12, fontweight="bold")
    ax.set_title(title_text, fontsize=14, fontweight="bold")
    ax.invert_yaxis()

    # 🚀 عرض المخطط في Streamlit
    st.pyplot(fig)
else:
    st.error("❌ لم يتم العثور على عمود 'job_title' في الملف.")


# القصة بعد الصورة

st.markdown("""
    <div class="styled-text">
        <h2>الواقع: تحديات ما بعد التخرج</h2>
    </div>
""", unsafe_allow_html=True)


st.markdown(
    """
        <div class="styled-text">

    🚀 **سوق العمل مليء بالفرص، لكن المنافسة شرسة!**  
    إذا كنت حديث التخرج، فالمجال مفتوح أمامك، لكنك بحاجة إلى المهارات المناسبة للتميز.  
    أما إذا كنت في منتصف مسيرتك المهنية، فقد تلاحظ أن الفرص تصبح أكثر تحديًا، حيث تبحث الشركات عن مبتدئين جاهزين للتطوير أو خبراء جاهزين للقيادة!  

    🔹 **اجعل مهاراتك سلاحك الأقوى، وكن مستعدًا لأي فرصة تأتي في طريقك!** 💪🔥  
    <div>
    """, 
    unsafe_allow_html=True
)



# ✅ تحليل فرص العمل بناءً على الخبرة
if "benefits" in Jadarat.columns and "exper" in Jadarat.columns:
    # تحويل الرواتب إلى أرقام
    Jadarat['benefits'] = pd.to_numeric(Jadarat['benefits'], errors='coerce')

    # حساب عدد الوظائف بناءً على مستوى الخبرة
    experience_counts = Jadarat['exper'].value_counts().sort_index()

    # تحديد لوحة الألوان
    palette = sns.color_palette("husl", len(experience_counts))

    # 🎨 رسم المخطط البياني
    fig, ax = plt.subplots(figsize=(5, 5))
    bars = ax.bar(experience_counts.index, experience_counts.values, color=palette)

    # إصلاح النصوص العربية
    xlabel_text = get_display(arabic_reshaper.reshape("سنوات الخبرة"))
    ylabel_text = get_display(arabic_reshaper.reshape("عدد الوظائف المتاحة"))
    title_text = get_display(arabic_reshaper.reshape("فرص العمل: حديثو التخرج مقابل أصحاب الخبرة"))

    # إضافة التنسيقات
    ax.set_xlabel(xlabel_text, fontsize=12, fontweight="bold")
    ax.set_ylabel(ylabel_text, fontsize=12, fontweight="bold")
    ax.set_title(title_text, fontsize=14, fontweight="bold")
    ax.grid(axis='y', linestyle='--', alpha=0.4)

    # إضافة الأرقام فوق الأعمدة
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, height, str(int(height)), ha='center', va='bottom', fontsize=10, fontweight='bold')

    # إضافة وسيلة إيضاح
    legend_labels = [get_display(arabic_reshaper.reshape(f"{exp} سنوات")) for exp in experience_counts.index]
    ax.legend(bars, legend_labels, title=get_display(arabic_reshaper.reshape("مستوى الخبرة")), loc='upper right', fontsize=10, frameon=True)

    # 🚀 عرض المخطط في Streamlit
    st.pyplot(fig)
else:
    st.error("❌ لم يتم العثور على الأعمدة المطلوبة 'benefits' و 'exper' في الملف.")


st.markdown(
    """
        <div class="styled-text1">


1️⃣ **حديثي التخرج مسيطرين على السوق!**

2️⃣ **بعد سنتين، الفرص تقل بشكل كبير!**

3️⃣ **اللي عندهم خبرة متوسطة (4+ سنوات) يعانون أكثر!**

4️⃣ **الوظايف لكبار السن (10+ سنوات) شبه معدومة**


✔ **إذا توك متخرج، وضعك تمام والشركات تبيك!**
✔ **إذا عندك سنتين إلى 4 سنوات، عندك فرصة لكن مو زي الخريجين الجدد.**
✔ **إذا عندك أكثر من 7 سنوات خبرة، لازم تعتمد على العلاقات أو الترقيات الداخلية، لأن التوظيف بيكون صعب!**

💡 **النصيحة؟** لا تجلس تعتمد على الوظايف بس، طور نفسك، وسّع علاقاتك، وخلك جاهز لأي فرصة تجيك! 🚀
    <div>
    """, 
    unsafe_allow_html=True
)




