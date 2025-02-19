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
st.markdown('''<h3 style="text-align: right; direction: rtl; font-family: DejaVu Sans;">مرحبًا بكم في تحليل شامل لبيانات الوظائف المتاحة في السعودية. سنستعرض معًا توزيع الرواتب، الخبرات المطلوبة، وأكثر الوظائف طلبًا. هدفنا هو تقديم رؤى عملية تُساعد الباحثين عن وظائف وصنّاع القرار.</h3>''', unsafe_allow_html=True)

# Section 1: Salary Distribution for Fresh Graduates
st.markdown('<h3 style="text-align: right; direction: rtl; font-family: DejaVu Sans;">🔍 توزيع الرواتب للخريجين الجدد</h3>', unsafe_allow_html=True)
st.markdown('<p style="text-align: right; direction: rtl; font-family: DejaVu Sans;">هل تساءلت يومًا عن متوسط الرواتب التي يحصل عليها الخريجون الجدد؟ دعونا نستعرض معًا توزيع الرواتب لنكتشف الفرص المتاحة للمبتدئين.</p>', unsafe_allow_html=True)

# Filter data for fresh graduates
fresh_grads = Jadarat_data[Jadarat_data['exper'] == 0]

# Create a figure and plot the histogram
fig, ax = plt.subplots(figsize=(10, 6))
sns.histplot(fresh_grads['Salary'], bins=30, kde=True, ax=ax, color='skyblue')
ax.set_title('توزيع الرواتب للخريجين الجدد', fontsize=16, fontname='DejaVu Sans')
ax.set_xlabel('الراتب', fontsize=14, fontname='DejaVu Sans')
ax.set_ylabel('التكرار', fontsize=14, fontname='DejaVu Sans')

# Display the plot using st.pyplot()
st.pyplot(fig)

# Section 2: Outliers in Salary
st.markdown('<h3 style="text-align: right; direction: rtl; font-family: DejaVu Sans;">🚨 القيم الشاذة في الرواتب (أعلى من 15000)</h3>', unsafe_allow_html=True)
st.markdown('<p style="text-align: right; direction: rtl; font-family: DejaVu Sans;">قد تشير الرواتب المرتفعة جدًا إلى وظائف تتطلب مهارات خاصة أو خبرات طويلة. دعونا نُلقِ نظرة على هذه القيم الشاذة.</p>', unsafe_allow_html=True)

# Show outliers in salaries
outliers = Jadarat_data[Jadarat_data['Salary'] > 15000]
st.write(outliers[['job_title', 'Salary']])

# Section 3: Animated Salary vs Required Positions
st.markdown('<h3 style="text-align: right; direction: rtl; font-family: DejaVu Sans;">📈 التوزيع البياني بين الراتب وعدد المناصب المطلوبة</h3>', unsafe_allow_html=True)
st.markdown('<p style="text-align: right; direction: rtl; font-family: DejaVu Sans;">هل هناك علاقة بين ارتفاع الرواتب وعدد المناصب المطلوبة؟ سنستكشف هذه العلاقة باستخدام رسم بياني متحرك.</p>', unsafe_allow_html=True)

# Ensure the necessary columns are numeric
Jadarat_data['Salary'] = pd.to_numeric(Jadarat_data['Salary'], errors='coerce')
Jadarat_data['required_positions'] = pd.to_numeric(Jadarat_data['required_positions'], errors='coerce')

# Create and animate the Vizzu chart
vizzu_obj = create_vizzu_obj(Jadarat_data)
anim_obj = vizzu_animate(
    vizzu_obj,
    {
        "x": "Salary",
        "y": "required_positions",
        "color": "region",
        "title": "الراتب مقابل المناصب المطلوبة",
        "label": "job_title"
    }
)
st.write(anim_obj)

# Section 4: Salary Distribution by Region
st.markdown('<h3 style="text-align: right; direction: rtl; font-family: DejaVu Sans;">🌐 توزيع الرواتب حسب المنطقة</h3>', unsafe_allow_html=True)

# Boxplot of salary by region
fig, ax = plt.subplots(figsize=(12, 8))
sns.boxplot(x='region', y='Salary', data=Jadarat_data, ax=ax, palette='viridis')
ax.set_title('توزيع الرواتب حسب المنطقة', fontsize=16, fontname='DejaVu Sans')
ax.set_xlabel('المنطقة', fontsize=14, fontname='DejaVu Sans')
ax.set_ylabel('الراتب', fontsize=14, fontname='DejaVu Sans')
st.pyplot(fig)

# Section 5: Experience vs Salary
st.markdown('<h3 style="text-align: right; direction: rtl; font-family: DejaVu Sans;">📅 العلاقة بين الخبرة والراتب</h3>', unsafe_allow_html=True)

# Scatterplot of experience vs salary
fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(x='exper', y='Salary', data=Jadarat_data, ax=ax, hue='region', palette='coolwarm')
ax.set_title('العلاقة بين الخبرة والراتب', fontsize=16, fontname='DejaVu Sans')
ax.set_xlabel('الخبرة (سنوات)', fontsize=14, fontname='DejaVu Sans')
ax.set_ylabel('الراتب', fontsize=14, fontname='DejaVu Sans')
st.pyplot(fig)

# Section 6: Top Job Titles by Salary
st.markdown('<h3 style="text-align: right; direction: rtl; font-family: DejaVu Sans;">🏆 أعلى المسميات الوظيفية من حيث الراتب</h3>', unsafe_allow_html=True)

# Barplot for top job titles by salary
top_job_titles = Jadarat_data.groupby('job_title')['Salary'].mean().sort_values(ascending=False).head(10)
fig, ax = plt.subplots(figsize=(12, 8))
sns.barplot(x=top_job_titles.values, y=top_job_titles.index, ax=ax, palette='magma')
ax.set_title('أعلى المسميات الوظيفية من حيث الراتب', fontsize=16, fontname='DejaVu Sans')
ax.set_xlabel('متوسط الراتب', fontsize=14, fontname='DejaVu Sans')
ax.set_ylabel('المسمى الوظيفي', fontsize=14, fontname='DejaVu Sans')
st.pyplot(fig)

# Section 7: Benefits Analysis
st.markdown('<h3 style="text-align: right; direction: rtl; font-family: DejaVu Sans;">🎁 تحليل المزايا الوظيفية</h3>', unsafe_allow_html=True)
st.markdown('<p style="text-align: right; direction: rtl; font-family: DejaVu Sans;">المزايا الوظيفية دائمًا ما تكون عامل جذب للباحثين عن عمل. لنستعرض أكثر المزايا شيوعًا في سوق العمل.</p>', unsafe_allow_html=True)

# Analyze benefits
benefits_counts = Jadarat_data['Benefits'].str.split(', ', expand=True).stack().value_counts()
fig, ax = plt.subplots(figsize=(12, 8))
sns.barplot(x=benefits_counts.values, y=benefits_counts.index, ax=ax, palette='husl')
ax.set_title('تحليل المزايا الوظيفية', fontsize=16, fontname='DejaVu Sans')
ax.set_xlabel('عدد الإعلانات', fontsize=14, fontname='DejaVu Sans')
ax.set_ylabel('المزايا', fontsize=14, fontname='DejaVu Sans')
st.pyplot(fig)

# Final Conclusion
st.markdown('<h3 style="text-align: right; direction: rtl; font-family: DejaVu Sans;">🔎 خلاصة التحليل</h3>', unsafe_allow_html=True)
st.markdown('''<p style="text-align: right; direction: rtl; font-family: DejaVu Sans;">هذا التحليل يُظهر معلومات قيّمة حول سوق العمل في السعودية. من توزيع الرواتب إلى المزايا الوظيفية، نأمل أن تُساعدك هذه البيانات في اتخاذ قرارات مدروسة سواء كنت باحثًا عن عمل أو جهة توظيف.</p>''', unsafe_allow_html=True)
