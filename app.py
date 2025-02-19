import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import arabic_reshaper
from bidi.algorithm import get_display
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

# Salary Distribution by Region
st.markdown('<h3 style="text-align: right; direction: rtl; font-family: DejaVu Sans;">🌐 توزيع الرواتب حسب المنطقة</h3>', unsafe_allow_html=True)

# Prepare data for the plot
region_counts = Jadarat_data.groupby('region')['Salary'].mean().sort_values(ascending=False)

# Reshape and apply BiDi algorithm to Arabic text
reshaped_labels = [get_display(arabic_reshaper.reshape(label)) for label in region_counts.index]

# Create a boxplot of salaries by region
fig, ax = plt.subplots(figsize=(12, 8))
sns.barplot(x=region_counts.values, y=region_counts.index, ax=ax, palette='viridis')

# Apply reshaped Arabic labels to the y-axis
ax.set_yticks(range(len(reshaped_labels)))
ax.set_yticklabels(reshaped_labels, fontsize=12)

# Add title and axis labels
ax.set_title('توزيع الرواتب حسب المنطقة', fontsize=16, fontname='DejaVu Sans')
ax.set_xlabel('متوسط الراتب', fontsize=14, fontname='DejaVu Sans')
ax.set_ylabel('المنطقة', fontsize=14, fontname='DejaVu Sans')

# Display the plot
st.pyplot(fig)

# Optionally, render another visualization (example: benefits analysis)
st.markdown('<h3 style="text-align: right; direction: rtl; font-family: DejaVu Sans;">🎁 تحليل المزايا الوظيفية</h3>', unsafe_allow_html=True)
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
