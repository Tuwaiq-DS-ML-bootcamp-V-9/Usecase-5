import streamlit as st
import plotly.express as px
import pandas as pd
# Load cleaned data
df = pd.read_csv('cleaned_data_jadarat.csv')

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
        font-size: 3em;
        font-weight: bold;
        text-align: center;
        color: #007BFF;
    }
    .highlight {
        color: #FF5733;
        font-weight: bold;
        font-size: 1.2em;
    }
    .subtitle {
        font-size: 2em;
        font-weight: bold;
        color: #28A745;
    }
    .divider-custom {
        border-top: 3px solid #007BFF;
        margin: 20px 0;
    }
    p {
        font-size: 1.4em;
    }
    /* Apply justification to all text elements */
    div.stMarkdown p {
        text-align: justify;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.image("images/bg.png", caption="")

# عنوان التطبيق
st.markdown('<h1 class="title">حديث تخرج؟ السوق فاتح لك أبوابه!</h1>', unsafe_allow_html=True)

st.markdown('<hr class="divider-custom">', unsafe_allow_html=True)

# مقدمة
st.markdown(
    """
كخريجين جدد، كلنا نمر بمرحلة تساؤل وشوي قلق، "هل في فرصة شغل تناسبنا وإحنا لسه متخرجين؟" من يوم ما ناخذ الشهادة، نبدأ نسمع عن التحديات في السوق وكيف إن الخبرة مطلوبة. لكن اليوم بنقول لكم قصة مختلفة، قصة تثبت إن في فرص حقيقية لحديثين التخرج في سوق العمل السعودي.

    """,
    unsafe_allow_html=True
)

st.markdown('<hr class="divider-custom">', unsafe_allow_html=True)

# القسم الأول: نظرة عامة على فرص العمل للحديثين التخرج
st.markdown('<p class="subtitle">1. نظرة عامة على فرص العمل للحديثين التخرج</p>', unsafe_allow_html=True)
st.markdown(
    """
    أول شيء لازم نعرفه إن السوق مو كله للناس اللي عندها سنوات طويلة من الخبرة. الداتا تثبت إن فيه نسبة كبيرة 
    من الوظايف مخصصة للي لسه باديين مشوارهم. يعني إذا كنت حديث تخرج، لا تخاف، في فرص تستناك!
    """,
    unsafe_allow_html=True
)
# st.image("images/image1.png", caption="")
# Create a new column to distinguish between Fresh Graduates and Experienced candidates
df['experience_level'] = df['exper'].apply(lambda x: 'Fresh Graduate' if x == 0 else 'Experienced')

# Count the job postings for each experience level
experience_counts = df['experience_level'].value_counts().reset_index()
experience_counts.columns = ['Experience Level', 'Number of Job Postings']

# Create an interactive bar chart

custom_colors = ["#A1C9F4", "#FFB482", "#8DE5A1", "#FF9F9B", "#D0BBFF", "#DEBB9B", "#FAB0E4", "#BFD3C1", "#C4A5E3", "#89A894"]






# Create an interactive bar chart with the updated color scheme
fig = px.bar(
    experience_counts, 
    x="Experience Level", 
    y="Number of Job Postings", 
    color="Experience Level", 
    labels={"Experience Level": "Experience Level", "Number of Job Postings": "Number of Job Postings"},
    text_auto=True,  # Show values inside bars
    color_discrete_sequence=custom_colors  # Apply consistent colors
)

# Keep layout styling the same
fig.update_layout(
    autosize=True,
    margin=dict(l=20, r=20, t=50, b=20)  # Maintain clean spacing
)

# Display the updated chart in Streamlit
st.plotly_chart(fig, use_container_width=True)



st.markdown(
    """
    من الرسم، نلاحظ إن عدد الوظايف المخصصة لحديثين التخرج أعلى من اللي تتطلب خبرة. هذا مؤشر إن الشركات صارت تركز على الكوادر الشابة اللي توها متخرجة، وتعطيهم فرصة يدخلون السوق ويطورون مهاراتهم على أرض الواقع.
    """,
    unsafe_allow_html=True
)

st.markdown('<hr class="divider-custom">', unsafe_allow_html=True)

# القسم الثاني: توزيع الوظائف حسب المناطق
st.markdown('<p class="subtitle">2. توزيع الوظائف حسب المناطق</p>', unsafe_allow_html=True)
st.markdown(
    """
    السؤال الثاني اللي يمكن يخطر ببالكم: "وين ألقى الفرصة اللي تناسبني؟" الداتا تكشف إن الوظايف تتوزع بشكل مختلف في 
    مناطق المملكة. بعض المناطق تشوف فيها عدد كبير من الإعلانات الوظيفية، بينما مناطق ثانية تكون الفرص فيها أقل. 
    """,
    unsafe_allow_html=True
)
# st.image("images/image2.png", caption="")
# Calculate the count of job postings per region
region_counts = df['region'].value_counts().reset_index()
region_counts.columns = ['Region', 'Number of Job Postings']

# Create an interactive bar chart
fig = px.bar(
    region_counts, 
    x="Region", 
    y="Number of Job Postings", 
    color="Region", 
    labels={"Region": "Region", "Number of Job Postings": "Number of Job Postings"},
    color_discrete_sequence=custom_colors  # Apply consistent colors
)

# Ensure the chart is responsive and fits inside Streamlit
fig.update_layout(
    autosize=True,
    margin=dict(l=20, r=20, t=50, b=20),  # Adjust margins for better layout
    xaxis_tickangle=-45  # Rotate x-axis labels for better readability if needed
)

# Display the chart in Streamlit
st.plotly_chart(fig, use_container_width=True)

st.markdown(
    """
    هذا زي ما هو واضح في الرسم، الرياض متصدرة بشكل كبير في عدد الوظايف الأعلى أجرًا، وتجي بعدها مناطق مثل مكة المكرمة والمنطقة الشرقية. هالشي يدل على إن الفرص المميزة غالبًا تتمركز في العاصمة وحول المراكز الاقتصادية الكبرى.
    """,
    unsafe_allow_html=True
)

st.markdown('<hr class="divider-custom">', unsafe_allow_html=True)

# القسم الثالث: الرواتب المتوقعة للحديثين التخرج
st.markdown('<p class="subtitle">3. الرواتب المتوقعة للحديثين التخرج</p>', unsafe_allow_html=True)
st.markdown(
    """
أول ما يجي في بال أي حديث تخرج وهو يدور على فرصته في سوق العمل هو: "كم راح اللي يكون راتبي أول وظيفة؟"
الداتا تبين إن الرواتب لحديثي التخرج متباينة؛ يعني في البداية ممكن تكون الرواتب بسيطة، لكنها تعتبر نقطة انطلاق توعد بتطور لاحق مع زيادة الخبرة


    """,
    unsafe_allow_html=True
)
# st.image("images/image3.png", caption="")
# Filter the dataset for Fresh Graduates
fresh_grad_df = df[df['exper'] == 0]

# Create an interactive histogram for salary distribution
fig = px.histogram(
    fresh_grad_df, 
    x="salary", 
    nbins=15,  # Keeping the same bin count
    labels={"salary": "Salary (SAR)", "count": "Frequency"},
    opacity=0.7,  # Slight transparency for better readability
    color_discrete_sequence=custom_colors  # Apply consistent colors
)

# Add a KDE-like curve using density normalization
fig.update_traces(histnorm='probability density')

# Improve layout for better visualization
fig.update_layout(
    autosize=True,
    margin=dict(l=20, r=20, t=50, b=20),
    bargap=0.1  # Small gap between bars for better readability
)

# Display the chart in Streamlit
st.plotly_chart(fig, use_container_width=True)


st.markdown(
    """
    من الرسم واضح إن رواتب حديثي التخرج تتراوح من 3000 ريال كحد أدنى إلى 10250 ريال كحد أعلى، مع متوسط حوالي 4700 ريال. نلاحظ إن أغلب الرواتب تتمركز حوالي 4000 ريال، لكن فيه شريحة أصغر تحصل على رواتب توصل للحد الأعلى. هالشي يشير إن السوق يعطي بداية معقولة للخرجين الجدد، ومع اكتساب الخبرة والتطوير، الرواتب ممكن تتحسن وتوصل لمستويات أفضل.
    """,
    unsafe_allow_html=True
)

st.markdown('<hr class="divider-custom">', unsafe_allow_html=True)

# القسم الرابع: العلاقة بين الخبرة والراتب
st.markdown('<p class="subtitle">4. العلاقة بين الخبرة والراتب</p>', unsafe_allow_html=True)
st.markdown(
    """
    الكل يعرف إن كل ما زادت الخبرة، غالبًا يزيد الراتب، بس السؤال هو: قد إيش الفرق فعليًا؟ هل الرواتب تقفز بشكل كبير مع كل سنة خبرة، ولا الزيادة تكون بسيطة؟

    """,
    unsafe_allow_html=True
)
# st.image("images/image4.png", caption="")
# Group data to find average salary per experience level
salary_trend = df.groupby("exper")["salary"].mean().reset_index()

# Create a line chart to show salary trends
fig = px.line(
    salary_trend, 
    x="exper", 
    y="salary", 
    labels={"exper": "Years of Experience", "salary": "Average Salary (SAR)"},
    markers=True , # Adds data points to the line
    color_discrete_sequence=custom_colors  # Apply consistent colors
)

# Improve layout for better visualization
fig.update_layout(
    autosize=True,
    margin=dict(l=20, r=20, t=50, b=20),
    xaxis_title="Years of Experience",
    yaxis_title="Average Salary (SAR)"
)

# Display the chart in Streamlit
st.plotly_chart(fig, use_container_width=True)

st.markdown(
    """
    
من الرسم واضح أن هناك علاقة طردية بين عدد سنوات الخبرة ومتوسط الراتب، حيث تزداد الرواتب تدريجياً مع زيادة الخبرة. لكن أكبر قفزة في الراتب تحدث بعد 4 سنوات من الخبرة، حيث يبدأ النمو في التسارع بشكل أوضح. بعد 10 سنوات خبرة، الرواتب تكون أعلى بحوالي 70% مقارنةً بحديثي التخرج، مما يوضح أن الأثر الحقيقي للخبرة يظهر بشكل أكبر على المدى الطويل.

    """,
    unsafe_allow_html=True
)


st.markdown('<hr class="divider-custom">', unsafe_allow_html=True)

# الخاتمة
st.markdown('<p class="subtitle">الخلاصة</p>', unsafe_allow_html=True)

st.markdown(
    """
الداتا تثبت لنا إن سوق العمل السعودي ما يقتصر بس على ذوي الخبرة فقط، ولكن يعطي فرصة حقيقية للحديثين التخرج:
- **فرص الوظائف:** فيه نسبة كبيرة من الوظايف مخصصة للناس اللي ما عندهم خبرة.
- **المناطق:** بعض المناطق مثل الرياض وجدة تتركز فيها فرص أفضل.
- **الرواتب:** الرواتب للحديثين التخرج معقولة وتعطي دفعة لبداية مشوار ناجح.
- **التطور مع الوقت:** حتى مع بداية متواضعة، مع زيادة الخبرة وتطوير المهارات، الرواتب تتحسن.

سوق العمل لحديثين التخرج مبشر بالخير. الشركات مهتمة تجيب الكفاءات الجديدة، ونلقى نسبة كبيرة من الوظايف مخصصة للي ما عندهم خبرة. الفرص تتركز بشكل أكبر في المدن الكبيرة مثل الرياض وجدة، والرواتب المبدئية تعتبر مبشرة. يعني حتى لو البداية بسيطة، مع اكتساب الخبرة وتطوير المهارات، الأمور تتحسن والآفاق تتوسع. بشكل عام، الوضع يبشر بمستقبل مهني ناجح لحديثي التخرج.

    """,
    unsafe_allow_html=True
)
