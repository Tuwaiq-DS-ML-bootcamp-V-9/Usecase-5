import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from st_vizzu import create_vizzu_obj, vizzu_animate

# Load the dataset
data_path = 'Jadarat_data.csv'
Jadarat_data = pd.read_csv(data_path)

# Display the title and introduction
st.markdown('<h1 style="text-align: right; direction: rtl;">📰 تحليل بيانات الوظائف في المملكة العربية السعودية</h1>', unsafe_allow_html=True)
st.markdown('''<h3 style="text-align: right; direction: rtl;">قمنا بتحليل البيانات المتعلقة بالإعلانات الوظيفية في السعودية، ونهدف إلى الكشف عن معلومات مهمة حول الرواتب، الخبرات المطلوبة، والفرص المتاحة في مختلف المناطق.</h3>''', unsafe_allow_html=True)

# Data Cleaning & Preprocessing
Jadarat_data['Salary'] = pd.to_numeric(Jadarat_data['Salary'], errors='coerce')
Jadarat_data['exper'] = Jadarat_data['exper'].str.extract('(\d+)').astype(int)
Jadarat_data['job_date'] = pd.to_datetime(Jadarat_data['job_date'], errors='coerce')

# Analyzing Salary Distribution for Fresh Graduates
fresh_grads = Jadarat_data[Jadarat_data['exper'] == 0]
st.markdown('<h3 style="text-align: right; direction: rtl;">🔍 توزيع الرواتب للخريجين الجدد</h3>', unsafe_allow_html=True)
plt.figure(figsize=(6, 4))
sns.histplot(fresh_grads['Salary'], bins=30, kde=True)
plt.title('توزيع الرواتب للخريجين الجدد')
plt.xlabel('الراتب')
plt.ylabel('التكرار')
st.pyplot()

# Show Outliers in Salary (Values above 15000)
outliers = Jadarat_data[Jadarat_data['Salary'] > 15000]
st.markdown('<h3 style="text-align: right; direction: rtl;">🚨 القيم الشاذة في الرواتب (أعلى من 15000)</h3>', unsafe_allow_html=True)
st.write(outliers[['job_title', 'Salary']])

# Animation of Salary vs Required Positions
st.markdown('<h3 style="text-align: right; direction: rtl;">📈 التوزيع البياني بين الراتب وعدد المناصب المطلوبة</h3>', unsafe_allow_html=True)
vizzu_obj = create_vizzu_obj(Jadarat_data)
vizzu_obj = vizzu_animate(vizzu_obj, x="Salary", y="required_positions", color="region", title="الراتب مقابل المناصب المطلوبة")
st.write(vizzu_obj)

# Final Conclusion
st.markdown('''<h3 style="text-align: right; direction: rtl;">في النهاية، التحليل يكشف عن بعض الاتجاهات المهمة مثل توزيع الرواتب بشكل غير متساوي في بعض المناطق، والفرص المتاحة للخريجين الجدد. باستخدام هذا التحليل، يمكننا اتخاذ قرارات أكثر فاعلية في اختيار الوظائف أو حتى تحديد الوظائف التي تناسب مهاراتنا واهتماماتنا.</h3>''', unsafe_allow_html=True)
