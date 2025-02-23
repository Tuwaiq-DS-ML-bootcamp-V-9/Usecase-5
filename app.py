import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


st.set_page_config(page_title="وظايف لحديثين التخرج",  layout="wide")

st.markdown("""
    <style>
        .navbar {
            background-color: #0B67B7;
            padding: 15px;
            text-align: center;
            font-size: 22px;
            font-weight: bold;
            color: white;
            width: 100%;
            border-radius: 10px;
        }
        .navbar a {
            color: white;
            margin: 0 20px;
            text-decoration: none;
            font-weight: bold;
        }
        .navbar a:hover {
            text-decoration: underline;
        }
        .content {
            direction: rtl;
            text-align: right;
            padding: 20px;
            margin: 10px 0;
            border-radius: 10px;
            background: #F6F8FA;
        }
        .content h2 {
            color: #0B67B7;
            margin-bottom: 20px;
        }
        .content p {
            font-size: 20px;
            color: #333;
            line-height: 1.8;
        }
        .job-card {
            text-align: right;
            border: 1px solid #ddd;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
            background-color: #e8f4ff;
        }
        .stSelectbox, .stButton, .stSlider {
            background-color: #0B67B7;
            color: white;
            border-radius: 10px;
            font-size: 16px;
        }
        .stAlert {
            border-radius: 10px;
            border: 1px solid #0B67B7;
            background-color: #E4EBF0;
        }
    </style>
    <div class="navbar">
    <p></p>
      <p></p>
        <p></p>
          <p></p>
            <p></p>
            
    </div>
""", unsafe_allow_html=True)


col1, col2 = st.columns([6, 1])  
with col2:
    st.image("Photo/jadarat.png", width=150)  

col1, col2 = st.columns([5, 9])
with col2:
    st.markdown("""
        <h1 style="text-align: right; color: #0B67B7; margin-top: 10px; font-size: 60px;">
            حديث تخرج ؟ ... وظيفتك أقرب مما تتخيل
        </h1>
    """, unsafe_allow_html=True)

with col1:
    st.image("Photo/jobs.png", width=270)

# تحميل البيانات
df_cleaned = pd.read_csv('Data/Jadaratcleaned_dataset.csv')

# تحسين الأعمدة الرقمية
df_cleaned['available_positions'] = pd.to_numeric(df_cleaned['available_positions'], errors='coerce').fillna(0).astype(int)
df_cleaned['total_positions'] = pd.to_numeric(df_cleaned['total_positions'], errors='coerce').fillna(0).astype(int)

# نص إرشادي
st.markdown("""
<div style="text-align: right; padding: 20px; background-color: #f0f8ff; border-radius: 10px;">
    <p style="color: #0B67B7; font-size: 30px; font-weight: bold; margin-bottom: 20px;">
        كلنا نعرف معاناة حديثين التخرج
    </p>
     <p style="color: #0B67B7; font-size: 30px; font-weight: bold; margin-bottom: 20px;">
      وما في أسوء من سؤال حصلت وظيفة ؟ كأنه هو اللي بيدور لك أو عنده واسطة بيساعدك فيها  
        </p>
     <p style="color: #0B67B7; font-size: 30px; font-weight: bold; margin-bottom: 20px;">
      اليوم أقول لك: ما تحتاج واسطة! السعودية العظمى موفّرة لك منصة جدارات، اللي تجمع لك كل الفرص الوظيفية في مكان واحد أنت بس جهّز سيرتك الذاتية والباقي ازهله
       </p>
      <p style="color: #0B67B7; font-size: 30px; font-weight: bold; margin-bottom: 20px;">
والأحلى من كذا؟ الفرص الوظيفية للخريجين بدون خبرة أعلى مقارنة بذوي الخبرة ! يعني جدارات مضبطينك ومجهّزين لك انطلاقك بسوق العمل      </p>
</div>
""", unsafe_allow_html=True)

# توزيع الوظائف حسب الخبرة
df_cleaned['experience_category'] = df_cleaned['experience_years'].apply(lambda x: 'ذو خبرة' if int(x) > 0 else 'حديث لتخرج')
experience_counts = df_cleaned['experience_category'].value_counts().reset_index()
experience_counts.columns = ['الفئة', 'عدد الوظائف']

fig = px.bar(
    experience_counts, 
    x="عدد الوظائف", 
    y="الفئة", 
    orientation="h", 
    text="عدد الوظائف", 
    color="عدد الوظائف",  
    color_continuous_scale="blues"
)

fig.update_traces(
    textposition="inside", 
    textfont_size=14, 
    marker_line_width=2 
)

fig.update_layout(
    title="توزيع الوظائف حسب الخبرة",
    title_x=0.5,
    title_font_size=18,
    xaxis_title="عدد الوظائف",
    yaxis_title="الفئة",
    template="plotly_white",
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("""
<div style="text-align: right; padding: 20px; background-color: #f0f8ff; border-radius: 10px;">
    <p style="color: #0B67B7; font-size: 30px; font-weight: bold; margin-bottom: 20px;">
        <p style="color: #0B67B7; font-size: 25px;">
      الشركات صارت تستثمر أكثر في حديثين التخرج وتعطيهم فرصة يثبتون انفسهم 🔹 
        </p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="text-align: right; padding: 20px; background-color: #f0f8ff; border-radius: 10px;">
    <p style="color: #0B67B7; font-size: 30px; font-weight: bold; margin-bottom: 20px;">
        طيب خليني أوضح لك الصورة أكثر...
    إذا كنت حديث تخرج وما عندك خبرة، أكيد يهمك تعرف كم القيمة السوقية لحديثين التخرج بحيث تقدر تقارن بين العروض الوظيفية عشان تختار الافضل
        </p>
</div>
""", unsafe_allow_html=True)

fresh_graduates = df_cleaned[df_cleaned['experience_years'] == 0]
mean_salary = fresh_graduates['salary_extracted'].mean()
min_salary = fresh_graduates['salary_extracted'].min()
max_salary = fresh_graduates['salary_extracted'].max()

salary_data = {
    "المؤشر": ["متوسط الراتب", "الحد الأدنى", "الحد الأعلى"],
    "الراتب (ريال)": [f"{mean_salary:.2f}", f"{min_salary:.2f}", f"{max_salary:.2f}"]
}

salary_df = pd.DataFrame(salary_data)

fig = go.Figure(data=[go.Table(
    header=dict(values=["المؤشر", "الراتب (ريال)"],
                fill_color='#0B67B7',
                align='center',
                font=dict(color='white', size=16)),
    cells=dict(values=[salary_df["المؤشر"], salary_df["الراتب (ريال)"]],
               fill_color='#e8f4ff',
               align='center',
               font=dict(size=14)))
])

fig.update_layout(
    title="متوسط ونطاق الرواتب لحديثين التخرج",
    title_x=0.5 ,
    width=1000,
    height=400  
)
st.plotly_chart(fig, use_container_width=True)


st.markdown("""
<div style="text-align: right; padding: 20px; background-color: #f0f8ff; border-radius: 10px;">
     <p style="color: #0B67B7; font-size: 25px;">
     الحد الأدنى: 4,000 ريال – بداية معقولة تدخل بسوق العمل 🔹
          </p>
     <p style="color: #0B67B7; font-size: 25px;">
        الحد الأعلى: 8,500 ريال – يعتمد على التخصص والمهارات المطلوبة 🔹 
           </p>
</div>
""", unsafe_allow_html=True)


st.markdown("""
<div style="text-align: right; padding: 20px; background-color: #f0f8ff; border-radius: 10px;">
    <p style="color: #0B67B7; font-size: 30px; font-weight: bold; margin-bottom: 20px;">
    وبما أن منصة جدارات تخدم معظم المناطق بالسعودية، بعرض لك وين اكثر العروض الوظيفية، عشان تعرف وين تكون فرصتك أكبر في القبول      </p>
</div>
""", unsafe_allow_html=True)

import plotly.express as px


region_counts = df_cleaned['region'].value_counts().reset_index()
region_counts.columns = ['المنطقة', 'عدد الوظايف']


fig = px.bar(
    region_counts, 
    x="عدد الوظايف", 
    y="المنطقة", 
    orientation="h", 
    text="عدد الوظايف", 
    color="عدد الوظايف",  
    color_continuous_scale="blues"  
)


fig.update_traces(
    textposition="inside", 
    textfont_size=14, 
    marker_line_width=2 
)

fig.update_layout(
    title="عدد الوظايف حسب المنطقة",
    title_x=0.5,
    title_font_size=18,
    xaxis_title="عدد الوظايف",
    yaxis_title="المنطقة",
    template="plotly_white",
)


st.plotly_chart(fig, use_container_width=True)

st.markdown("""
<div style="text-align: right; padding: 20px; background-color: #f0f8ff; border-radius: 10px;">
            <p style="color: #0B67B7; font-size: 25px;">  
      الرياض متصدرة بعدد 587 وظيفة – يعني فرصتك فيها أكبر 🔹
        </p>
     <p style="color: #0B67B7; font-size: 25px;">
       لو انت مو ساكن بأحد المدن الاكثر فرص ارشح تتنقل لهم
      بس والله اذا تشوفه صعبه وانت في منطقة فرصها قليلة، ممكن تفكر في التقديم عن بعد 🔹
 </p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="text-align: right; padding: 20px; background-color: #f0f8ff; border-radius: 10px;">
    <p style="color: #0B67B7; font-size: 30px; font-weight: bold; margin-bottom: 20px;">
    اي بضبط فيه في وظايف عن بعد  يعني ان شاءالله ماراح تخلص من هنا الا امورك محلوله
       </p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="text-align: right; padding: 20px; background-color: #f0f8ff; border-radius: 10px;">
    <p style="color: #0B67B7; font-size: 30px; font-weight: bold; margin-bottom: 20px;">
  وطبعًا حنا عارفين بعض المجالات فيها فرص اكثر من غيرها  ، بوضح لك اكثر المسميات الوظيفيه 
</div>
""", unsafe_allow_html=True)


import plotly.express as px


top_categories = df_cleaned["job_category"].value_counts().head(75).reset_index()
top_categories.columns = ["الفئة الوظيفية", "عدد الوظايف"]

# إنشاء المخطط الشريطي
fig = px.bar(
    top_categories, 
    x="عدد الوظايف", 
    y="الفئة الوظيفية", 
    orientation="h", 
    text="عدد الوظايف", 
    color="عدد الوظايف",
    color_continuous_scale="blues"
)


fig.update_traces(textposition="inside", textfont_size=12, marker_line_width=1)

fig.update_layout(
    title="  عدد الوظايف حسب كل تصنيف",
    title_x=0.5,
    title_font_size=18,
    xaxis_title="عدد الوظايف",
    yaxis_title="الفئة الوظيفية",
    height=800,  
    template="plotly_white"
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("""
<div style="text-align: right; padding: 20px; background-color: #f0f8ff; border-radius: 10px;">
            <p style="color: #0B67B7; font-size: 25px;">  
أكثر الوظايف كانت بهذي المسميات أخصائيين ، مدراء، ومهندسين، وأقلها المهن اليدوية يوضح ان الطلب عالي على الإداريين والتخصصيين 🔹
        </p>
</div>
""", unsafe_allow_html=True)



st.markdown("""
<div style="text-align: right; padding: 20px; background-color: #f0f8ff; border-radius: 10px;">
    <p style="color: #0B67B7; font-size: 30px; font-weight: bold; margin-bottom: 20px;">
     الفرص كثيرة، والشركات متنوعة عندك القطاع الخاص ، وعندك الشبه حكومية
       أغلب الفرص في القطاع الخاص، بالمقابل شبه الحكومية نادره 
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="text-align: right; padding: 20px; background-color: #f0f8ff; border-radius: 10px;">
    <p style="color: #0B67B7; font-size: 30px; font-weight: bold; margin-bottom: 20px;">
اكيد جاء ببالك وش الفرق في الرواتب  بينهم 
</div>
""", unsafe_allow_html=True)

import pandas as pd
import plotly.express as px


salary_by_type = df_cleaned[df_cleaned['comp_type'].isin(['خاص', 'شبه حكومية'])]


salary_stats = salary_by_type.groupby('comp_type')['salary_extracted'].agg(['mean', 'min', 'max', 'count']).reset_index()


salary_stats.columns = ['نوع الشركة', 'متوسط الراتب', 'الحد الأدنى', 'الحد الأعلى', 'عدد الرواتب']


salary_stats[['متوسط الراتب', 'الحد الأدنى', 'الحد الأعلى']] = salary_stats[['متوسط الراتب', 'الحد الأدنى', 'الحد الأعلى']].round(2)


salary_stats['التوضيح'] = salary_stats.apply(lambda row: f" عدد الرواتب لحساب المتوسط: {row['عدد الرواتب']}", axis=1)


fig = px.bar(
    salary_stats, 
    x="نوع الشركة", 
    y=["متوسط الراتب", "الحد الأدنى", "الحد الأعلى"], 
    barmode="group",
    text_auto=True,
    color_discrete_map={"متوسط الراتب": "blue", "الحد الأدنى": "lightblue", "الحد الأعلى": "darkblue"}
)


fig.update_layout(
    title="تحليل رواتب القطاع الخاص وشبه الحكومي",
    title_x=0.5,
    title_font_size=18,
    xaxis_title="نوع الشركة",
    yaxis_title="الراتب (ريال)",
    template="plotly_white",
    annotations=[
        dict(
            x=row["نوع الشركة"],
            y=row["الحد الأعلى"] + 1000,  
            text=row["التوضيح"],
            showarrow=False,
            font=dict(size=14, color="black")
        ) for _, row in salary_stats.iterrows()
    ]
)


st.plotly_chart(fig, use_container_width=True)


st.markdown("""
<div style="text-align: right; padding: 20px; background-color: #f0f8ff; border-radius: 10px;">
     <p style="color: #0B67B7; font-size: 25px;"> 
  الرواتب في شبه الحكومي أعلى بالمتوسط، لكن الحد الأدنى والأعلى متساوي 🔹 
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="text-align: right; padding: 20px; background-color: #f0f8ff; border-radius: 10px;">
    <p style="color: #0B67B7; font-size: 30px; font-weight: bold; margin-bottom: 20px;">
نقطة مهمة ما راح أفوتها وش تتوقع الوظايف المتاحة تستهدف الذكور أكثر أو الإناث ؟ هنا تلقى الجواب
</div>
""", unsafe_allow_html=True)


import pandas as pd
import plotly.express as px


gender_mapping = {
    "M": "ذكر",
    "F": "أنثى",
    "both": "كلاهما"
}


gender_ar = df_cleaned['gender'].map(gender_mapping).dropna()


gender_counts = gender_ar.value_counts().reset_index()
gender_counts.columns = ["الجنس", "عدد الوظائف"]


fig = px.pie(
    gender_counts, 
    names="الجنس", 
    values="عدد الوظائف", 
    color="الجنس",
    color_discrete_map={"ذكر": "blue", "أنثى": "pink", "كلاهما": "lightgray"},
    title="توزيع الوظائف حسب الجنس"
)


fig.update_traces(
    textinfo="percent+label",
    marker=dict(line=dict(color="#000", width=2))
)

fig.update_layout(
    title_x=0.5,
    title_font_size=18,
    template="plotly_white",
     width=800,
     height=700  
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("""
<div style="text-align: right; padding: 20px; background-color: #f0f8ff; border-radius: 10px;">
             <p style="color: #0B67B7; font-size: 25px;"> 
لو تلاحظ الوظايف للذكور أكثر بشوي من الإناث، والجزء الأكبر مو محدد الجنس يعني الفرص متاحة للجميع 🔹 
</div>
""", unsafe_allow_html=True)


st.markdown("""
<div style="text-align: right; padding: 20px; background-color: #f0f8ff; border-radius: 10px;">
    <p style="color: #0B67B7; font-size: 30px; font-weight: bold; margin-bottom: 20px;">
حلوييين الحين جاء دورك، استعرض الوظايف زي ما تبي حسب تصنيف الوظيفة الي تبيه والمنطقة 
</div>
""", unsafe_allow_html=True)

categories = ['اختار التصنيف'] + list(df_cleaned['job_category'].dropna().unique())
regions = ['اختار المنطقة'] + list(df_cleaned['region'].dropna().unique())


st.markdown("""
    <style>
        body {text-align: right; color: white;}
        .stSelectbox label {color: white; font-weight: bold; font-size: 30px; direction: rtl;}
        .stSelectbox div {font-size: 10px; padding: 5px;direction: rtl;}
        .stSelectbox select {padding: 10px; font-size: 18px;direction: rtl;}
    </style>
""", unsafe_allow_html=True)


selected_category = st.selectbox('اختر تصنيف الوظيفة الي تناسبك:', categories, index=0, key="category", format_func=lambda x: x, help="اختر التصنيف المناسب")
selected_region = st.selectbox('اختار المنطقة :', regions, index=0, key="region", format_func=lambda x: x, help="اختر المنطقة المناسبة")

if selected_category != 'اختار التصنيف' and selected_region != 'اختار المنطقة':
    filtered_df = df_cleaned[
        (df_cleaned['job_category'] == selected_category) & 
        (df_cleaned['region'] == selected_region) & 
        ((df_cleaned['available_positions'] == 0) | (df_cleaned['total_positions'] > df_cleaned['available_positions']))
    ][['comp_name', 'comp_no', 'salary_extracted', 'benefits', 'qualif', 'job_desc', 'total_positions', 'available_positions', 'experience_category', 'gender', 'job_title']]

    if not filtered_df.empty:
        st.subheader("الوظائف المتاحة:")

        for index, row in filtered_df.iterrows():
            remaining_positions = row['total_positions'] - row['available_positions'] if row['available_positions'] > 0 else row['total_positions']
            benefits_text = ', '.join(str(item) for item in row['benefits']) if isinstance(row['benefits'], list) else row['benefits']
            qualif_text = ', '.join(str(item) for item in row['qualif']) if isinstance(row['qualif'], list) else row['qualif']
            job_desc_text = ' '.join(str(item) for item in row['job_desc']) if isinstance(row['job_desc'], list) else row['job_desc']
            
            gender_text = {
                'M': 'ذكر',
                'F': 'أنثى',
                'both': 'متاح كل الجنسين'
            }.get(row['gender'], row['gender'])

            st.markdown(f"""
            <div style="text-align: right; border: 1px solid #ddd; padding: 15px; border-radius: 10px; margin-bottom: 15px; background-color: #e8f4ff;">
                <p><strong>🏢 اسم الشركة:</strong> {row['comp_name']}</p>
                <p><strong>📞 رقم التواصل:</strong> {row['comp_no']}</p>
                <p><strong>💼 المسمى الوظيفي:</strong> {row['job_title']}</p>
                <p><strong>💰 الراتب:</strong> {row['salary_extracted']} ريال</p>
                <p><strong>🚻 الجنس المطلوب:</strong> {gender_text}</p>
                <p><strong>المزايا:</strong> {benefits_text}</p>
                <p><strong> المهارات المطلوبه:</strong> {qualif_text}</p>
                <p><strong>الوصف الوظيفي:</strong> {job_desc_text}</p>
                <p><strong> العدد الإجمالي للوظائف:</strong> {row['total_positions']}</p>
                <p><strong>الشواغر المتاحة:</strong> {remaining_positions}</p>
                {f'<p><strong>⌛ سنوات الخبرة المطلوبة:</strong> {row["experience_category"]}</p>' if row["experience_category"] == "حديث تخرج" else ""}
            </div>
            """, unsafe_allow_html=True)
        
    else:
        st.warning("❌ لا توجد وظائف متاحة بهذا التصنيف وهذه المنطقة.")
else:
    st.info("يرجى اختيار **التصنيف** و**المنطقة** لعرض الوظائف المتاحة.")



st.markdown("""
<div style="text-align: right; padding: 20px; background-color: #f0f8ff; border-radius: 10px;">
    <p style="color: #0B67B7; font-size: 30px; font-weight: bold; margin-bottom: 20px;">
من الاخر؟ بدال قعدة البيت واسئلة العالم اللي ما تخلص، ادخل على جدارات وقدّم ... فالك التوفيق
</div>
""", unsafe_allow_html=True)


st.markdown("""
    <style>
        .navbar {
            background-color: #0B67B7;
            padding: 15px;
            text-align: center;
            font-size: 22px;
            font-weight: bold;
            color: white;
            width: 100%;
            border-radius: 10px;
        }
        .navbar a {
            color: white;
            margin: 0 20px;
            text-decoration: none;
            font-weight: bold;
        }
        .navbar a:hover {
            text-decoration: underline;
        }
        .content {
            direction: rtl;
            text-align: right;
            padding: 20px;
            margin: 10px 0;
            border-radius: 10px;
            background: #F6F8FA;
        }
        .content h2 {
            color: #0B67B7;
            margin-bottom: 20px;
        }
        .content p {
            font-size: 20px;
            color: #333;
            line-height: 1.8;
        }
        .job-card {
            text-align: right;
            border: 1px solid #ddd;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
            background-color: #e8f4ff;
        }
        .stSelectbox, .stButton, .stSlider {
            background-color: #0B67B7;
            color: white;
            border-radius: 10px;
            font-size: 16px;
        }
        .stAlert {
            border-radius: 10px;
            border: 1px solid #0B67B7;
            background-color: #E4EBF0;
        }
    </style>
    <div class="navbar">
    <p></p>
      <p></p>
        <p></p>
          <p></p>
            <p></p>
    </div>
""", unsafe_allow_html=True)
