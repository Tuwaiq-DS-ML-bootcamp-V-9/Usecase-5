import streamlit as st


# Title in RTL
st.markdown('<h1 style="text-align:right" dir="rtl">هل الرياض هي أرض الأحلام لحديثي التخرج؟</h1>', unsafe_allow_html=True)

# First paragraph in RTL
st.markdown('<p style="text-align:right" dir="rtl">الحمد لله، تخرجت من الجامعة، لكن لم أجد وظيفة حتى الآن. والكل يقول لي إن الرياض هي المكان الذي سأجد فيه وظيفة الأحلام.</p>', unsafe_allow_html=True)

# Another paragraph in RTL
st.markdown('<p style="text-align:right" dir="rtl">لكن، هل هذا الكلام صحيح؟</p>', unsafe_allow_html=True)

# More paragraphs in RTL
st.markdown('<p style="text-align:right" dir="rtl">لقد قمت بجمع بيانات الوظائف المعلنة على منصة جدارات وحللتها لأرى إذا كانت الرياض هي أكثر مدينة تعلن عن وظائف لحديثي التخرج.</p>', unsafe_allow_html=True)

# Another question in RTL
st.markdown('<h3 style="text-align:right" dir="rtl">هل الرياض هي المدينة الأكثر إعلانًا عن الوظائف؟</h3>', unsafe_allow_html=True)

st.image('chart/chart1.png', use_container_width=True)
# Data analysis paragraph in RTL
st.markdown('<p style="text-align:right" dir="rtl">من خلال البيانات المتاحة، يبدو أن الرياض هي الأكثر في إعلانات الوظائف، حيث تمثل تقريبًا نصف إجمالي الإعلانات على "جدارات".</p>', unsafe_allow_html=True)

# Gender discrimination question in RTL
st.markdown('<h3 style="text-align:right" dir="rtl">هل هناك تمييز بين الجنسين في الوظائف المعلنة بالرياض؟</h3>', unsafe_allow_html=True)
st.image('chart/chart2.png', use_container_width=True)
# Analysis paragraph about gender in RTL
st.markdown('<p style="text-align:right" dir="rtl">من خلال التحليل، يتضح أنه لا يوجد تمييز بين الجنسين، حيث تركز الجهات في الرياض على المهارات والكفاءات أكثر من التركيز على جنس المتقدم.</p>', unsafe_allow_html=True)

# Experience preference question in RTL
st.markdown('<h3 style="text-align:right" dir="rtl">هل تفضل الجهات بالرياض أصحاب الخبرة أم حديثي التخرج؟</h3>', unsafe_allow_html=True)
st.image('chart/chart3.png', use_container_width=True)
st.markdown('<p style="text-align:right" dir="rtl"> يظهر التمثيل ان اكثر من نصف الوظائف المعلنة في الرياض لحديثي التخرج، ممكن لان الكثير من الجهات تفضل لان حديثي التخرج لديهم الافكار الجديدة والروح الحماسية في العمل </p>', unsafe_allow_html=True)

# Final salary question in RTL
st.markdown('<h3 style="text-align:right" dir="rtl">ما هو متوسط رواتب حديثي التخرج بالرياض؟</h3>', unsafe_allow_html=True)
st.image('chart/chart4.png', use_container_width=True)
st.markdown('<p style="text-align:right" dir="rtl">متوسط الرواتب لحديثي التخرج في الرياض من 4000 الى 5000 بالشهر لكن السؤال هنا هل يكفي هذا الراتب للعيش بالرياض؟</p>', unsafe_allow_html=True)
st.markdown('<p style="text-align:right" dir="rtl">بحسب دراسة اجرتها منصة سكن تظهر ان يمكن تقدير متوسط تكلفة المعيشة في السعودية للفرد الواحد خلال الشهر من 3000 إلى 5000 ريال سعودي شهرياً./p>', unsafe_allow_html=True)

st.markdown("""<p style="text-align:right" dir="rtl">بعد مراجعة هذه البيانات، يمكننا أن نقول إن الرياض هي أرض الأحلام لحديثي التخرج. حيث إن معظم الوظائف المعلنة توجد في الرياض، ولا يوجد تمييز على أساس الجنس، مما يتيح الكثير من الفرص للخريجين الجدد. صحيح أن الراتب المتوقع قد لا يكون مرتفعًا جدًا، ولكن إذا أخذنا في الاعتبار العمل لمدة سنتين لاكتساب الخبرة، يمكننا بعدها البحث عن وظائف براتب أعلى.
</p>""", unsafe_allow_html=True)

