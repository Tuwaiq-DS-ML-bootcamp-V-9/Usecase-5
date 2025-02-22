import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import arabic_reshaper
from bidi.algorithm import get_display

def main():
    # ضبط إعدادات الصفحة
    st.set_page_config(page_title="رحلة التخرج", layout="centered")
    # مقدمة التطبيق مع تنسيق HTML
    st.markdown("""
    <h1 style='text-align: center;'>🎓🌟🎉 رحلة التخرج </h1>
    <div style='text-align: center; font-size:18px; margin-top: 20px;'>
        <p><strong>بداية الرحلة – لحظة التخرج</strong></p>
        <p>
            بعد مسيرة أكثر من ١٢ عامًا مليئة بالدراسة والاختبارات، جاء اليوم المنتظر الذي يحتفل فيه 
            عدد كبير من خريجي الجامعات بتخرجهم. في هذه اللحظة التاريخية، يحمل كل خريج حلمًا كبيرًا 
            وطموحًا لا حدود له. بعد هذا اليوم، تبدأ رحلة البحث عن وظيفة الأحلام، محملة بتوقعات وآمال 
            كثيرة وفرص ربما أكثر
        </p>
        <p>:ومع ذلك، تظهر تساؤلات عدة في بال الخريجين، مثل</p>
        <p> هل سنجد وظيفة أحلامنا رغم عدم امتلاكنا للخبرة الكافية؟ 🤔</p>
        <p> كم سيكون متوسط الراتب الذي سنحصل عليه؟ 💰</p>
        <p> هل يجب أن نتوجه إلى العاصمة أو المدن الكبيرة لنجد فرص عمل أفضل، أم أن منطقتنا توفر الوظائف المناسبة؟ 🏙️</p>
        <p> ماهو القطاع الذي يوفر عدد كبير من الوظائف ؟ 🏢</p>
        <p>
            .تلك التساؤلات التي تتردد في أذهان الكثيرين بعد التخرج تستدعي إجابات واضحة وعملية
            هنا، ندعوهم لاستكشاف منصة "جدارات" المعروفة، حيث نعرض لهم البيانات والإحصائيات دون فلسفة 
            .أو تنظير، لنقدم لهم رؤى موضوعية تساعد في رسم ملامح المستقبل المهني بثقة وواقعية
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # فقرة "التحديات الأولية – مواجهة سوق العمل"
    st.markdown("""
    <div style='text-align: center; font-size:18px; margin-top: 40px;'>
        <p><strong>التحديات الأولية – مواجهة سوق العمل</strong></p>
        <p>
            .مع بداية بحثهم عن فرص العمل، يواجه الخريجون واقعاً مختلفاً عن أمانيهم الجامعية
            تُبرز البيانات معدلات التوظيف لكل تخصص، حيث يظهر أن بعض التخصصات تحظى بفرص عمل وفيرة،
            بينما تواجه أخرى صعوبة أكبر في دخول سوق العمل. هنا تبدأ القصة الحقيقية، إذ يتجلى
            .الفارق بين التوقعات والواقع
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # قراءة الملف "cleaned_jadarat.csv" واستخدامه في التطبيق
    try:
        df = pd.read_csv("cleaned_jadarat.csv")
    except Exception as e:
        st.error(f"حدث خطأ أثناء تحميل الملف: {e}")
        return

    # استخدام الداتا سيت باسم jadarat
    jadarat = df
    
    # =============================
    st.markdown(
    "<h2 style='text-align: center;'>تحليل الوظائف الأكثر طلباً في السوق</h2>",
    unsafe_allow_html=True
    )

    
    # تحديد لوحة ألوان مخصصة
    custom_palette = sns.color_palette("viridis", n_colors=10)
    
    # حساب الوظائف الأكثر طلباً (يفضل أن يكون اسم العمود "job_title" أو "JobTitle")
    if 'job_title' in jadarat.columns:
        top_jobs = jadarat['job_title'].value_counts().head(10)
    elif 'JobTitle' in jadarat.columns:
        top_jobs = jadarat['JobTitle'].value_counts().head(10)
    else:
        st.error("عمود الوظائف غير موجود في الداتا سيت.")
        return

    # إعادة تشكيل النص العربي للعرض الصحيح
    reshaped_title = get_display(arabic_reshaper.reshape("أعلى 10 وظائف مطلوبة في السوق حسب تحليل بيانات منصة جدارات ٢٠٢٣"))
    reshaped_xlabel = get_display(arabic_reshaper.reshape("عدد الوظائف"))
    reshaped_ylabel = get_display(arabic_reshaper.reshape("المسمى الوظيفي"))
    
    # إعداد حجم الشكل
    plt.figure(figsize=(10, 5))
    
    # رسم المخطط الشريطي الأفقي باستخدام لوحة الألوان المخصصة
    sns.barplot(
        x=top_jobs.values, 
        y=[get_display(arabic_reshaper.reshape(job)) for job in top_jobs.index],
        palette=custom_palette[:len(top_jobs)]
    )
    
    # إضافة العنوان والمحاور
    plt.title(reshaped_title, fontsize=14)
    plt.xlabel(reshaped_xlabel, fontsize=12)
    plt.ylabel(reshaped_ylabel, fontsize=12)
    
    # عرض المخطط في تطبيق Streamlit
    st.pyplot(plt.gcf())
    plt.clf()  # تفريغ الشكل الحالي

    # =============================
    
    # قسم عرض قائمة الوظائف الفريدة ونسب توفرها
    
    st.markdown(
    "<h4 style='text-align: center;'>اختر الوظيفة لمعرفة مدى توفرها في البيانات:</h4>",
    unsafe_allow_html=True
    )

    # حساب تكرارات الوظائف (معتمدًا على نفس العمود المستخدم سابقاً)
    if 'job_title' in jadarat.columns:
        job_counts = jadarat["job_title"].value_counts()
    elif 'JobTitle' in jadarat.columns:
        job_counts = jadarat["JobTitle"].value_counts()
    else:
        st.error("عمود الوظائف غير موجود في الداتا سيت.")
        return
    
    selected_job = st.selectbox("الوظائف المتاحة", job_counts.index)

    count = job_counts[selected_job]
    total = job_counts.sum()
    ratio = (count / total) * 100
    
    # عدد توفر الوظيفة
    st.markdown(
        "<p style='text-align: center; font-weight: bold;'>عدد توفر هذه الوظيفة: {}</p>".format(count),
        unsafe_allow_html=True
    )
    
    # نسبة توفر الوظيفة
    st.markdown(
        "<p style='text-align: center; font-weight: bold;'>نسبة توفرها مقارنة ببقية الوظائف: {:.2f}%</p>".format(ratio),
        unsafe_allow_html=True
    )


    # =============================
    st.markdown(
    "<h2 style='text-align: center;'>التوزيع النسبي للوظائف بحسب مستوى الخبرة</h2>",
    unsafe_allow_html=True
    )
    # تأكد من وجود العمود الذي يحدد الخبرة (مثلاً experience_categories)
    if 'experience_categories' not in jadarat.columns:
        st.error("لا يوجد عمود 'experience_categories' في الداتا سيت.")
        return
    
    # ====== قسم رسم Pie Chart لبيان نسبة الوظائف لحديثي التخرج مقابل ذوي الخبرة ======
    st.markdown("""
    <div style='text-align: center; font-size:18px; margin-top: 40px;'>
        <p><strong>نسبة الوظائف بين حديثي التخرج والخبراء</strong></p>
    </div>
    """, unsafe_allow_html=True)
    
    # حساب عدد الوظائف لكل فئة خبرة (Fresh Graduate / Expert)
    experience_counts = jadarat['experience_categories'].value_counts()
    
    # إنشاء لوحة ألوان مخصصة
    custom_palette = sns.color_palette("viridis", n_colors=10)
    
    # إنشاء الشكل
    fig, ax = plt.subplots(figsize=(5,5))
    
    # إعادة تشكيل النص بالعربية إذا لزم الأمر (حسب القيم الموجودة)
    labels = [get_display(arabic_reshaper.reshape(str(x))) for x in experience_counts.index]
    
    # رسم المخطط الدائري باستخدام لوحة الألوان المخصصة
    ax.pie(
        experience_counts.values,
        labels=labels,
        autopct='%1.1f%%',
        startangle=140,
        colors=custom_palette[:len(experience_counts)]  # عدد الألوان يطابق عدد الشرائح
    )
    ax.axis('equal')  # لجعل الرسم دائريًا تمامًا
    
    # عرض المخطط في ستريمليت
    st.pyplot(fig)
    plt.clf()


    # =============================
    st.markdown(
    "<h2 style='text-align: center;'>متوسط الرواتب لحديثي التخرج حسب الوظيفة</h2>",
    unsafe_allow_html=True)
    
    # التأكد من وجود عمود "salary" و "experience_categories" و "job_title"
    if 'salary' not in jadarat.columns:
        st.error("عمود 'salary' غير موجود في الداتا سيت.")
        return
    if 'job_title' not in jadarat.columns and 'JobTitle' not in jadarat.columns:
        st.error("عمود الوظائف غير موجود في الداتا سيت.")
        return


    # تصفية البيانات لحديثي التخرج
    df_fresh = jadarat[jadarat['experience_categories'] == "خريجون جدد"]
        
        
       

    # حساب متوسط الراتب لحديثي التخرج حسب الوظيفة
    avg_salary_by_job = df_fresh.groupby('job_title')['salary'].mean()
    
    # ترتيب الوظائف من الأعلى إلى الأدنى
    avg_salary_by_job_sorted = avg_salary_by_job.sort_values(ascending=False)
    
    # اختيار أعلى 10 وظائف
    top_10_jobs = avg_salary_by_job_sorted.head(10)
    
    # إعادة تشكيل أسماء الوظائف بالعربية
    reshaped_jobs = [get_display(arabic_reshaper.reshape(str(job))) for job in top_10_jobs.index]
        
    plt.figure(figsize=(10, 5))
    # استخدمنا القائمة reshaped_jobs بدلًا من top_10_jobs.index
    sns.barplot(x=reshaped_jobs, y=top_10_jobs.values, palette="viridis")
    
    plt.xticks(rotation=45)
    
    # إعادة تشكيل النصوص العربية على المحاور والعنوان
    plt.xlabel(get_display(arabic_reshaper.reshape("المسمى الوظيفي")), fontsize=12)
    plt.ylabel(get_display(arabic_reshaper.reshape("متوسط الراتب")), fontsize=12)
    plt.title(get_display(arabic_reshaper.reshape("أعلى 10 وظائف لحديثي التخرج من حيث متوسط الراتب")), fontsize=14)
    
    st.pyplot(plt.gcf())
    plt.clf()




    
    # قائمة منسدلة لعرض متوسط الراتب لوظيفة محددة
    selected_job = st.selectbox("اختر الوظيفة لعرض متوسط الراتب", avg_salary_by_job.index)
    avg_salary = avg_salary_by_job[selected_job]
    
    st.markdown(
        "<p style='text-align: center; font-size: 18px;'><strong>متوسط الراتب لهذه الوظيفة:</strong> {:.2f}</p>"
        .format(avg_salary),
        unsafe_allow_html=True
    )




        
    st.markdown("""
    <h2 style='text-align: center;'>توزيع الوظائف على حسب المنطقة</h2>
    
    """, unsafe_allow_html=True)

    # تأكد من وجود عمود 'region'
    if 'region' not in jadarat.columns:
        st.error("عمود 'region' غير موجود في الداتا سيت.")
        return

    # تحديد لوحة ألوان مخصصة
    custom_palette = sns.color_palette("viridis", n_colors=10)
    
    # حساب توزيع الوظائف (بالنسب المئوية) عبر المناطق
    region_counts = jadarat['region'].value_counts(normalize=True) * 100

    # إعادة تشكيل النص العربي للعناوين
    region_labels = [get_display(arabic_reshaper.reshape(str(label))) for label in region_counts.index]

    # إعداد حجم الشكل قبل الرسم
    plt.figure(figsize=(12, 6))

    # رسم المخطط الشريطي باستخدام لوحة الألوان المخصصة
    sns.barplot(x=region_labels, y=region_counts.values, palette=custom_palette[:len(region_labels)])

    # إضافة العناوين والتسميات مع إعادة تشكيل النص العربي
    plt.title(get_display(arabic_reshaper.reshape("توزيع الوظائف على حسب المنطقة")), fontsize=14)
    plt.xlabel(get_display(arabic_reshaper.reshape("المنطقة")), fontsize=12)
    plt.ylabel(get_display(arabic_reshaper.reshape("نسبة الوظائف (%)")), fontsize=12)

    # تعديل تدوير الخطوط والمحاذاة لتصحيح عرض النصوص العربية
    plt.xticks(rotation=45, fontsize=12, fontfamily="DejaVu Sans")
    plt.yticks(fontsize=12)

    # عرض الرسم البياني في Streamlit
    st.pyplot(plt.gcf())
    plt.clf()



    # ---------------------------
    # قائمة منسدلة للمناطق: عند اختيار منطقة تظهر عدد الوظائف فيها ونسبة الوظائف من إجمالي الوظائف.
    st.markdown("<h2 style='text-align: center;'>تفاصيل المنطقة المختارة</h2>", unsafe_allow_html=True)
    
    # الحصول على قائمة المناطق الفريدة (يمكنك استخدام ترتيب أبجدي)
    region_list = sorted(jadarat['region'].unique())
    selected_region = st.selectbox("اختر المنطقة", region_list)
    
    # حساب عدد الوظائف في المنطقة المختارة
    region_count = jadarat[jadarat['region'] == selected_region].shape[0]
    total_jobs = jadarat.shape[0]
    region_percentage = (region_count / total_jobs) * 100
    
    # عرض النتائج في منتصف الصفحة باستخدام تنسيق HTML
    st.markdown(
        "<p style='text-align: center; font-size:18px; font-weight: bold;'>عدد الوظائف في المنطقة {}: {}</p>"
        .format(selected_region, region_count),
        unsafe_allow_html=True
    )
    st.markdown(
        "<p style='text-align: center; font-size:18px; font-weight: bold;'>نسبة الوظائف في هذه المنطقة من إجمالي الوظائف: {:.2f}%</p>"
        .format(region_percentage),
        unsafe_allow_html=True
    )



    
    st.markdown("""
    <h2 style='text-align: center;'>تحليل نوع الشركة (خاص مقابل شبه حكومي) وأكثر الوظائف المعروضة في المنصة</h2>
    """, unsafe_allow_html=True)


    # حساب عدد الشركات حسب النوع
    company_counts = jadarat['comp_type'].value_counts()
    
    # إعادة تشكيل النصوص العربية لعناوين الشرائح
    labels = [get_display(arabic_reshaper.reshape(str(label))) for label in company_counts.index]
    
    # تحديد لوحة ألوان مخصصة باستخدام viridis (نفس المستخدمة سابقًا)
    custom_palette = sns.color_palette("viridis", n_colors=10)
    
    # إعداد الشكل ورسم المخطط الدائري مع تمرير الألوان من لوحة الألوان المخصصة
    plt.figure(figsize=(6,6))
    plt.pie(
        company_counts.values, 
        labels=labels, 
        autopct='%1.1f%%', 
        startangle=140,
        colors=custom_palette[:len(company_counts)]
    )
    plt.title(get_display(arabic_reshaper.reshape("توزيع الشركات: خاص مقابل شبه حكومي")), fontsize=14)
    plt.axis('equal')  # لضمان أن يكون الشكل دائرياً
    
    st.pyplot(plt.gcf())
    plt.clf()




if __name__ == "__main__":
    main()
