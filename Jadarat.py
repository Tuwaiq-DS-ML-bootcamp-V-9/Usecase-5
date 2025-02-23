import streamlit as st

# --- Streamlit App ---


# ضبط اتجاه النص ليكون من اليمين إلى اليسار وتحسين تجربة القراءة
st.markdown(
    """
    <style>
    body {
        direction: rtl;
        text-align: right;
        font-family: 'Cairo', sans-serif;
    }
    .title {
        font-size: 3em;  /* تكبير العنوان الرئيسي */
        font-weight: bold;
        text-align: center;
        color: #007BFF;
    }
    .highlight {
        color: #FF5733;
        font-weight: bold;
        font-size: 1.2em;  /* تكبير النصوص المميزة */
    }
    .subtitle {
        font-size: 2em;  /* تكبير العناوين الفرعية */
        font-weight: bold;
        color: #28A745;
    }
    .divider-custom {
        border-top: 3px solid #007BFF;
        margin: 20px 0;
    }
    p {
        font-size: 1.4em;  /* تكبير النصوص العادية */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# إضافة App Bar مع صورة
st.markdown(
    """
    <div class="app-bar">
        <img src="https://zameenblog.s3.amazonaws.com/blog/wp-content/uploads/2021/08/1440x625-1-1-1024x447.jpg" alt="Logo">
    </div>
    """,
    unsafe_allow_html=True
)

# عنوان التطبيق
st.markdown('<h1 class="title">]الوظائف في جدارات</h1>', unsafe_allow_html=True)

st.markdown('<hr class="divider-custom">', unsafe_allow_html=True)

# عنوان التطبيق
st.markdown('<h4 class="title">🚀 تفكر تستثمر في الفلل؟ الرياض هي وجهتك الذكية!</h4>', unsafe_allow_html=True)



# مقدمة
st.markdown(
    """
    إذا كنت تفكر في استثمار عقاري مربح، فأبشرك أنك وصلت للمكان الصح! سوق الفلل في الرياض يشهد حركة قوية، والفرص اليوم أفضل من أي وقت مضى، خاصة مع تزايد الطلب، المشاريع الجديدة، البنية التحتية القوية، والنمو السكاني السريع، مما يجعل الاستثمار في الفلل خيارًا ذكيًا ومربحًا.  
    """
)

# القسم الأول: لماذا الفلل في الرياض؟
st.markdown('🔎 ليه الفلل في الرياض؟')

st.markdown(
    """
    لأن الطلب في تصاعد مستمر، والمشاريع الجديدة، والبنية التحتية القوية، والنمو السكاني السريع كلها عوامل ترفع من قيمة الاستثمار في الفلل.  
    """
)

# القسم الثاني: توزيع الفلل في الرياض
st.markdown('<p class="subtitle">📊 وين الفرصة الحقيقية؟</p>', unsafe_allow_html=True)

st.image("fig_1.png", caption="")

st.markdown(
    """
    مو كل حي في الرياض راح يعطيك نفس العائد الاستثماري! الأرقام واضحة—الشمال والغرب هم الأبرز من حيث عدد الفلل المعروضة، والطلب فيهم عالي.  
    """
)

st.markdown('<hr class="divider-custom">', unsafe_allow_html=True)

# القسم الثالث: متوسط أسعار المتر المربع
st.markdown('<p class="subtitle">📊 كم وصل متوسط الأسعار؟</p>', unsafe_allow_html=True)

st.image("fig_2.png", caption="")

st.markdown(
    """
    السعر يحدد القرار! إذا كنت تبحث عن أقوى عائد استثماري، لازم تعرف أين أعلى سعر للمتر المربع:  
    **📍 الشمال في القمة بمتوسط 9,219.01 ريال/م²**  
    **📍 الجنوب يقدم فرصًا بأسعار تبدأ من 3,390.89 ريال/م²**  
    """
)

st.markdown('<hr class="divider-custom">', unsafe_allow_html=True)

# القسم الرابع: أرخص 10 أحياء في شمال الرياض
st.markdown('<p class="subtitle">📊 أرخص 10 أحياء في شمال الرياض</p>', unsafe_allow_html=True)

st.image("fig_3.png", caption="")

st.markdown(
    """
    حددنا لك أرخص 10 أحياء من حيث متوسط سعر المتر المربع للفلل—وهنا تكمن الفرصة للمستثمر الذكي اللي يعرف أن الأسعار في الرياض قاعدة ترتفع بسرعة!  
    """
)

st.markdown('<hr class="divider-custom">', unsafe_allow_html=True)
st.image("fig_3.png", caption="")

# خاتمة
st.markdown(
    """
    **🚀 الخلاصة: الأسئلة التي تمت الإجابة عليها**  
    - **أين تكمن الفرصة الذهبية في الرياض؟**  
      الفرصة تكمن في المناطق الشمالية والغربية، حيث يوجد أكبر عدد من الفلل المعروضة والطلب مرتفع.  
    
    - **كم وصل متوسط أسعار المتر المربع؟**  
      الشمال في القمة بمتوسط 9,219.01 ريال/م²، بينما الجنوب يقدم فرصًا بأسعار تبدأ من 3,390.89 ريال/م².  
    
    - **أين أرخص الأحياء في شمال الرياض؟**  
      حددنا أرخص 10 أحياء في شمال الرياض بناءً على متوسط سعر المتر المربع، وهي فرصة ذهبية للمستثمرين.  
     
    """
)
