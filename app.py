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

# Step 1: Split the 'positions' column into 'filling_positions' and 'required_positions' by the '/' separator
Jadarat_data[['filling_positions', 'required_positions']] = Jadarat_data['positions'].str.split('/', expand=True)

# Step 2: Clean up any extra spaces around the values (if any)
Jadarat_data['filling_positions'] = Jadarat_data['filling_positions'].str.strip()
Jadarat_data['required_positions'] = Jadarat_data['required_positions'].str.strip()

# Display the title and introduction
st.markdown('<h1 style="text-align: right; direction: rtl;">📰 تحليل بيانات الوظائف في المملكة العربية السعودية</h1>', unsafe_allow_html=True)
st.markdown('''<h3 style="text-align: right; direction: rtl;">قمنا بتحليل البيانات المتعلقة بالإعلانات الوظيفية في السعودية، ونهدف إلى الكشف عن معلومات مهمة حول الرواتب، الخبرات المطلوبة، والفرص المتاحة في مختلف المناطق.</h3>''', unsafe_allow_html=True)

# Analyzing Salary Distribution for Fresh Graduates
fresh_grads = Jadarat_data[Jadarat_data['exper'] == 0]
st.markdown('<h3 style="text-align: right; direction: rtl;">🔍 توزيع الرواتب للخريجين الجدد</h3>', unsafe_allow_html=True)

# Create a figure and plot the histogram
fig, ax = plt.subplots(figsize=(6, 4))
sns.histplot(fresh_grads['Salary'], bins=30, kde=True, ax=ax)
ax.set_title('توزيع الرواتب للخريجين الجدد')
ax.set_xlabel('الراتب')
ax.set_ylabel('التكرار')

# Display the plot using st.pyplot()
st.pyplot(fig)

# Show Outliers in Salary (Values above 15000)
outliers = Jadarat_data[Jadarat_data['Salary'] > 15000]
st.markdown('<h3 style="text-align: right; direction: rtl;">🚨 القيم الشاذة في الرواتب (أعلى من 15000)</h3>', unsafe_allow_html=True)
st.write(outliers[['job_title', 'Salary']])

# Animation of Salary vs Required Positions
st.markdown('<h3 style="text-align: right; direction: rtl;">📈 التوزيع البياني بين الراتب وعدد المناصب المطلوبة</h3>', unsafe_allow_html=True)

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

# Final Conclusion
st.markdown('''<h3 style="text-align: right; direction: rtl;">في النهاية، التحليل يكشف عن بعض الاتجاهات المهمة مثل توزيع الرواتب بشكل غير متساوي في بعض المناطق، والفرص المتاحة للخريجين الجدد. باستخدام هذا التحليل، يمكننا اتخاذ قرارات أكثر فاعلية في اختيار الوظائف أو حتى تحديد الوظائف التي تناسب مهاراتنا واهتماماتنا.</h3>''', unsafe_allow_html=True)
