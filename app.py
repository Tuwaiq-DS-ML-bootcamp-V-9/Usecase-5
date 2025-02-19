import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import ast
from st_vizzu import create_vizzu_obj, vizzu_animate

# Load the dataset
data_path = 'Jadarat_data.csv'  # Adjust this if needed for your environment
Jadarat_data = pd.read_csv(data_path)

# Data Cleaning & Preprocessing
# Convert the string representation of the list into an actual list
Jadarat_data['benefits'] = Jadarat_data['benefits'].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else x)

# Create the 'Salary' column by extracting the salary value
Jadarat_data['Salary'] = Jadarat_data['benefits'].apply(
    lambda x: float(x[1]) if isinstance(x, list) and len(x) > 1 and 'Salary' in str(x[0]) else None
)

# Create the 'Benefits' column by extracting the remaining items in the list (if any)
Jadarat_data['Benefits'] = Jadarat_data['benefits'].apply(
    lambda x: ', '.join(x[2:]) if isinstance(x, list) and len(x) > 2 else None
)

# Split the 'positions' column into 'filling_positions' and 'required_positions' by the '/' separator
Jadarat_data[['filling_positions', 'required_positions']] = Jadarat_data['positions'].str.split('/', expand=True)

# Clean up any extra spaces around the values (if any)
Jadarat_data['filling_positions'] = Jadarat_data['filling_positions'].str.strip()
Jadarat_data['required_positions'] = Jadarat_data['required_positions'].str.strip()

# Set up the Streamlit page configuration
st.set_page_config(page_title="تحليل بيانات الوظائف في السعودية", layout="wide")

# Set the font to support Arabic characters
plt.rcParams['font.family'] = 'DejaVu Sans'

# Display the title and introduction
st.markdown('<h1 style="text-align: right; direction: rtl; font-family: DejaVu Sans;">📊 تحليل بيانات الوظائف في المملكة العربية السعودية</h1>', unsafe_allow_html=True)
st.markdown('''<h3 style="text-align: right; direction: rtl; font-family: DejaVu Sans;">قمنا بتحليل البيانات المتعلقة بالإعلانات الوظيفية في السعودية، ونهدف إلى الكشف عن معلومات مهمة حول الرواتب، الخبرات المطلوبة، والفرص المتاحة في مختلف المناطق.</h3>''', unsafe_allow_html=True)

# Analyzing Salary Distribution for Fresh Graduates
fresh_grads = Jadarat_data[Jadarat_data['exper'] == 0]
st.markdown('<h3 style="text-align: right; direction: rtl; font-family: DejaVu Sans;">🔍 توزيع الرواتب للخريجين الجدد</h3>', unsafe_allow_html=True)

# Create a figure and plot the histogram
fig, ax = plt.subplots(figsize=(10, 6))
sns.histplot(fresh_grads['Salary'], bins=30, kde=True, ax=ax, color='skyblue')
ax.set_title('توزيع الرواتب للخريجين الجدد', fontsize=16, fontname='DejaVu Sans')
ax.set_xlabel('الراتب', fontsize=14, fontname='DejaVu Sans')
ax.set_ylabel('التكرار', fontsize=14, fontname='DejaVu Sans')

# Display the plot using st.pyplot()
st.pyplot(fig)

# Show Outliers in Salary (Values above 15000)
outliers = Jadarat_data[Jadarat_data['Salary'] > 15000]
st.markdown('<h3 style="text-align: right; direction: rtl; font-family: DejaVu Sans;">🚨 القيم الشاذة في الرواتب (أعلى من 15000)</h3>', unsafe_allow_html=True)
st.write(outliers[['job_title', 'Salary']])

# Animation of Salary vs Required Positions
st.markdown('<h3 style="text-align: right; direction: rtl; font-family: DejaVu Sans;">📈 التوزيع البياني بين الراتب وعدد المناصب المطلوبة</h3>', unsafe_allow_html=True)

# Make sure the necessary columns are numeric
Jadarat_data['Salary'] = pd.to_numeric(Jadarat_data['Salary'], errors='coerce')
Jadarat_data['required_positions'] = pd.to_numeric(Jadarat_data['required_positions'], errors='coerce')

# Now create the vizzu object and animate using correct syntax
vizzu_obj = create_vizzu_obj(Jadarat_data)

# Use a dictionary-based argument to animate the graph
anim_obj = vizzu_animate(
    vizzu_obj,
    {
        "x": "Salary",  # Salary column on the x-axis
        "y": "required_positions",  # Required Positions column on the y-axis
        "color": "region",  # Color by region
        "title": "الراتب مقابل المناصب المطلوبة",  # Title of the chart
        "label": "job_title"  # Adding labels as the job title
    }
)

# Render the animation chart using Chartipyvizzu
st.write(anim_obj)  # This renders the Vizzu animation on the Streamlit page

# Salary Distribution by Region
st.markdown('<h3 style="text-align: right; direction: rtl; font-family: DejaVu Sans;">🌐 توزيع الرواتب حسب المنطقة</h3>', unsafe_allow_html=True)
fig, ax = plt.subplots(figsize=(12, 8))
sns.boxplot(x='region', y='Salary', data=Jadarat_data, ax=ax, palette='viridis')
ax.set_title('توزيع الرواتب حسب المنطقة', fontsize=16, fontname='DejaVu Sans')
ax.set_xlabel('المنطقة', fontsize=14, fontname='DejaVu Sans')
ax.set_ylabel('الراتب', fontsize=14, fontname='DejaVu Sans')
st.pyplot(fig)

# Experience vs. Salary
st.markdown('<h3 style="text-align: right; direction: rtl; font-family: DejaVu Sans;">📅 العلاقة بين الخبرة والراتب</h3>', unsafe_allow_html=True)
fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(x='exper', y='Salary', data=Jadarat_data, ax=ax, hue='region', palette='coolwarm')
ax.set_title('العلاقة بين الخبرة والراتب', fontsize=16, fontname='DejaVu Sans')
ax.set_xlabel('الخبرة (سنوات)', fontsize=14, fontname='DejaVu Sans')
ax.set_ylabel('الراتب', fontsize=14, fontname='DejaVu Sans')
st.pyplot(fig)

# Top Job Titles by Salary
st.markdown('<h3 style="text-align: right; direction: rtl; font-family: DejaVu Sans;">🏆 أعلى المسميات الوظيفية من حيث الراتب</h3>', unsafe_allow_html=True)
top_job_titles = Jadarat_data.groupby('job_title')['Salary'].mean().sort_values(ascending=False).head(10)
fig, ax = plt.subplots(figsize=(12, 8))
sns.barplot(x=top_job_titles.values, y=top_job_titles.index, ax=ax, palette='magma')
ax.set_title('أعلى المسميات الوظيفية من حيث الراتب', fontsize=16, fontname='DejaVu Sans')
ax.set_xlabel('متوسط الراتب', fontsize=14, fontname='DejaVu Sans')
ax.set_ylabel('المسمى الوظيفي', fontsize=14, fontname='DejaVu Sans')
st.pyplot(fig)

# Benefits Analysis
st.markdown('<h3 style="text-align: right; direction: rtl; font-family: DejaVu Sans;">🎁 تحليل المزايا الوظيفية</h3>', unsafe_allow_html=True)
benefits_counts = Jadarat_data['Benefits'].str.split(', ', expand=True).stack().value_counts()
fig, ax = plt.subplots(figsize=(12, 8))
sns.barplot(x=benefits_counts.values, y=benefits_counts.index, ax=ax, palette='husl')
ax.set_title('تحليل المزايا الوظيفية', fontsize=16, fontname='DejaVu Sans')
ax.set_xlabel('عدد الإعلانات', fontsize=14, fontname='DejaVu Sans')
ax.set_ylabel('المزايا', fontsize=14, fontname='DejaVu Sans')
st.pyplot(fig)

# Final Conclusion
st.markdown('''<h3 style="text-align: right; direction: rtl; font-family: DejaVu Sans;">في النهاية، التحليل يكشف عن بعض الاتجاهات المهمة مثل توزيع الرواتب بشكل غير متساوي في بعض المناطق، والفرص المتاحة للخريجين الجدد. باستخدام هذا التحليل، يمكننا اتخاذ قرارات أكثر فاعلية في اختيار الوظائف أو حتى تحديد الوظائف التي تناسب مهاراتنا واهتماماتنا.</h3>''', unsafe_allow_html=True)
