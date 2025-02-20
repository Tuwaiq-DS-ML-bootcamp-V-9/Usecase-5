import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.markdown(
    """
    <style>
    body {
        direction: rtl;
        text-align: right;
    }
    .css-1d391kg, .css-1v3fvcr {
        direction: rtl;
        text-align: right;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.title("📖 توك متخرج و شايل هم الوظيفة")
st.header("📊  تعال خلني اعطيك نظره على السوق")

st.write("""
    معك سلمان بيتخرج قريب وما يدري وش السوق الوظيفي عندنا. 
         
     خلنا نعرف وش يبي سلمان يعرف 

    1️⃣ وين اكثر الوظائف المتاحة؟ في منطقة؟
          
    2️⃣ كم المتوقع يكون الراتب؟
         
    3️⃣ هل الجنس يؤثر على توفر الوظائف؟
         
    4️⃣ هل كل الوظائف تتطلب خبره؟

         

         
     خل نجاوب سلمان اكثر المدن طلبا للوظائف
    """)

st.markdown("###  📌اكثر المدن طلبا للوظائف")
st.image("image/output.png")

st.write("""
 بنلاحظ ان الرياض هي اكثر مدينة فيها عروض ،لان الرياض هي عاصمة السعودية وصار فيها فرص كثيره بسبب مشاريع رؤية 2030 وفرت الكثير من الفرص فالرياض تعتبر من افضل المدن للفرص الوظيفية.

    وهاذي متوسط الرواتب في مناطق السعودية
         """)

st.markdown("###  متوسط الرواتب في مناطق السعودية")

st.image("image/output2.png")

st.write("""
وهنا بنلاحظ متوسط الرواتب لكل منطقة 
""")


st.markdown("### نسبة كل جنس في الوظائف")

st.image("image/output3.png")

st.write("""
لو نلاحظ الحمدالله ان الوظائف متوزعة بشكل جيد بين الجنسين ولا يوجد تفاوت كبير بين الجنسين في الوظائف
         الا لبعض الوظائف ممكن تكون للرجال اكثر من النساء والعكس صحيح.""")


st.markdown("### عدد الوظائف التي تتطلب خبرة")

st.image("image/output4.png")

st.write("""

نلاحظ ان اغلب الوظائف ما تتطلب خبره وهذا شي جيد للخريجين الجدد لانهم يبدأون مشوارهم الوظيفي بدون خبره ويكونون متخصصين في مجالهم بعد فتره من العمل والتعلم.
         
""")
