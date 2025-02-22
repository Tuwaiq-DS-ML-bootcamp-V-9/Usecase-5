import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('Jadarat_data_v2.csv')

# Apply RTL styling for the entire app
st.markdown(
    """
    <style>
    body {
        direction: rtl;
        text-align: right;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# CSS for RTL styling
st.markdown("""
<style>
.rtl-text {
    text-align: right;
    direction: rtl;
    font-family: 'Arial', sans-serif;
}
</style>
""", unsafe_allow_html=True)

# Title in RTL direction
st.markdown("""
<div class="rtl-text">
    <h1>اختيار التخصص</h1>
</div>
""", unsafe_allow_html=True)

# Description in RTL direction
st.markdown("""
<div class="rtl-text">
    اختيار التخصص من أصعب القرارات التي تواجه الطلاب، حيث يحدد هذا القرار مسارهم الوظيفي المستقبلي. 
ولأننا ندرك أهمية هذا القرار وتأثيره الكبير على حياة الطلاب،قمنا بتحليل الوظائف المتاحة على منصة جدارات لسنة ٢٠٢٢ و ٢٠٢٣م، بهدف توفير تصور واضح عن:
    <ol>
        <li><b>أكثر الوظائف طلبًا في السوق السعودي:</b> لمعرفة المجالات التي تزداد فيها فرص العمل.</li>
        <li><b>أكثر الوظائف أجرًا:</b> لتقديم نظرة على التخصصات التي تضمن عائدًا ماديًا مجزيًا.</li>
    </ol>
</div>
""", unsafe_allow_html=True)

# Sidebar for year selection
st.sidebar.header("تصفية حسب السنة")
years = [2022, 2023]  # The available years in the dataset
selected_years = st.sidebar.multiselect("اختر السنوات:", years, default=years)

# Filter the data based on selected years
if selected_years:
    filter_years = df[df['job_year'].isin(selected_years)]
else:
    filter_years = df  # If no year is selected, show all data

# Calculate the value counts for job titles
job_counts = filter_years['job_title'].value_counts().head(15)

# Create a bar chart using Plotly
fig = px.bar(
    job_counts,
    x=job_counts.index,
    y=job_counts.values,
    labels={'job_title': 'المسمى الوظيفي', 'y': 'عدد الوظائف'}
   
)
# Customize the layout to adjust the title and style
fig.update_layout(
    title={
        'text': 'أكثر ١٥ وظيفة طلب في السوق سعودي',
        'x': 0.99,  # Center the title horizontally
        'xanchor': 'right',
        'yanchor': 'top'
        
    },
     xaxis=dict(
        title="المسمى الوظيفي",
        title_standoff=90,  # Add space between x-axis title and the chart
        tickangle=45        # Rotate x-axis labels for better readability
    ),
    yaxis=dict(
        title="عدد الوظائف"
    ),
    font=dict(
        family="Arial",
        size=18
    )
)

# Display the chart in Streamlit
st.plotly_chart(fig)

st.write(""" 
الوظيفة الأكثر طلبًا في السوق هي "بائع" بعدد إجمالي 98.  
يشير هذا إلى ارتفاع الطلب على الوظائف المتعلقة بالمبيعات في السوق، ويرجع ذلك غالبًا إلى نمو قطاعات البيع بالتجزئة والصناعات التي تتطلب التعامل المباشر مع العملاء.

 
تأتي وظيفة "محاسب" في المرتبة الثانية بعدد 89.  
يبرز هذا أهمية أدوار المحاسبة وإدارة الشؤون المالية عبر مختلف الصناعات، مما يشير إلى اعتماد الشركات على هؤلاء المحترفين لإدارة أمورها المالية.
""")

# Show the filtered dataset
st.write("### البيانات المصفاة")
filtered_top_15 = filter_years[filter_years['job_title'].isin(job_counts.index)]
st.write(filtered_top_15)






# Levels of experience and their respective salary thresholds
experience_salary_conditions = {
    'خريج': 8000,
    'مبتدئ':10000,
    'متوسط': 15000,
    'خبير': 20000
}

# Iterate through each experience level, filter the data, and create a chart
for level, min_salary in experience_salary_conditions.items():
    # Filter the data for the current level of experience and salary >= min_salary
    filtered_df = df[(df['level_experience'] == level) & (df['salary'] >= min_salary)]

    # Check if there is any data after filtering
    if not filtered_df.empty:
        # Create a bar chart to visualize job titles and their salaries
        fig = px.bar(
            filtered_df,
            x='job_title',
            y='salary',
            color='job_title',
            labels={'job_title': 'المسمى الوظيفي', 'salary': 'الراتب'}
        )
# Customize the layout for this chart
        fig.update_layout(
            title={
                'text': f'المسميات الوظيفية لـ "{level}" برواتب أعلى من {min_salary}',
                'x': 0.99,  # Align title closer to the right
                'xanchor': 'right',
                'yanchor': 'top',
            },
            xaxis=dict(
                title="المسمى الوظيفي",
                tickangle=45,  # Rotate the x-axis labels by 45 degrees
                automargin=True,  # Adjust margin to prevent cutoff
                title_standoff=90 # Add space between x-axis title and chart
            ),
            yaxis=dict(
                title="الراتب"
            ),
            font=dict(
                family="Arial",
                size=14
            ),
            bargap=0.2  # Add spacing between bars
        
        )


        # Display the chart in Streamlit
        st.plotly_chart(fig)

        # Display the filtered dataset
        st.write(f"### البيانات المصفاة لـ {level}")
        st.write(filtered_df)
    else:
        st.write(f"لا توجد بيانات مطابقة للمعايير المحددة لـ {level}.")

st.write("## الاستنتاجات:")

st.write("""
- **الصحة والهندسة في المقدمة:**
  التركيز على التخصصات الطبية والهندسية يؤكد أهمية هذه القطاعات في السوق السعودي.

- **زيادة الطلب على القيادة الإدارية:**
  الأدوار القيادية مثل إدارة الموارد البشرية وإدارة المشاريع تشهد طلبًا كبيرًا، مما يعكس حاجة المؤسسات إلى الكفاءات الإدارية.

- **التنوع في التخصصات:**
  السوق يظهر تنوعًا في الطلب على الوظائف، بما يشمل التخصصات الفنية (التصميم والبرمجيات)، والإدارية (الموارد البشرية)، والتقنية (الهندسة).

- **الرواتب المرتفعة للتخصصات المتخصصة:**
  الوظائف ذات المهارات العالية (مثل الطيارين) تتمتع برواتب مرتفعة، مما يعكس قيمة هذه المهارات في السوق.
""")

