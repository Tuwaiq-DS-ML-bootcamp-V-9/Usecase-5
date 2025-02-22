import streamlit as st
import pandas as pd

def main():
    # يمكنك ضبط إعدادات الصفحة (اختياري)
    st.set_page_config(
        page_title="رحلة التخرج",
        layout="centered"  # لجعل التطبيق يأخذ المساحة الوسطى بشكل أوضح
    )
    
    # استخدام HTML لتنسيق النص في المنتصف وإضافة الرموز
    st.markdown("""
    <h1 style='text-align: center;'>🎓 رحلة التخرج 🎓</h1>
    <div style='text-align: center; font-size:18px;'>
        <p>
            بعد مسيرة أكثر من ١٢ عامًا مليئة بالدراسة والاختبارات، جاء اليوم المنتظر الذي يحتفل فيه 
            عدد كبير من خريجي الجامعات بتخرجهم. في هذه اللحظة التاريخية، يحمل كل خريج حلمًا كبيرًا 
            وطموحًا لا حدود له. بعد هذا اليوم، تبدأ رحلة البحث عن وظيفة الأحلام، محملة بتوقعات وآمال 
            كثيرة وفرص ربما أكثر.
        </p>
    </div>
    
    <div style='text-align: center; font-size:18px;'>
        <p>:ومع ذلك، تظهر تساؤلات عدة في بال الخريجين، مثل</p>
        <p> هل سنجد وظيفة أحلامنا رغم عدم امتلاكنا للخبرة الكافية؟ 🤔</p>
        <p> كم سيكون متوسط الراتب الذي سنحصل عليه؟ 💰</p>
        <p> هل يجب أن نتوجه إلى العاصمة أو المدن الكبيرة لنجد فرص عمل أفضل، أم أن منطقتنا توفر الوظائف المناسبة؟ 🏙️</p>
        <p> هل الاختيار الأفضل هو العمل في القطاع الخاص أم الحكومي؟ 🏢</p>
    </div>
    
    <div style='text-align: center; font-size:18px;'>
        <p>
            تلك التساؤلات التي تتردد في أذهان الكثيرين بعد التخرج تستدعي إجابات واضحة وعملية. 
            هنا، ندعوكم لاستكشاف منصة "جدارات" المعروفة، حيث نعرض لكم البيانات والإحصائيات دون فلسفة 
            .أو تنظير، لنقدم لكم رؤى موضوعية تساعد في رسم ملامح المستقبل المهني بثقة وواقعية
        </p>
    </div>
    """, unsafe_allow_html=True)



def main():
    st.title("عرض الوظائف الفريدة في الداتا سيت")
    
    # قراءة الملف "cleaned_jadarat.csv" واستخدامه في التطبيق
    try:
        df = pd.read_csv("cleaned_jadarat.csv")
        st.success("تم تحميل الملف بنجاح!")
    except Exception as e:
        st.error(f"حدث خطأ أثناء تحميل الملف: {e}")
        return

    # استخراج الوظائف الفريدة من عمود "JobTitle"
    if "JobTitle" in df.columns:
        unique_jobs = df["JobTitle"].unique()

        st.subheader("الوظائف الفريدة في الداتا سيت:")
        # عرض كل وظيفة فريدة
        for job in unique_jobs:
            st.write(f"- {job}")
    else:
        st.error("عمود 'JobTitle' غير موجود في الداتا سيت.")


if __name__ == '__main__':
    main()
