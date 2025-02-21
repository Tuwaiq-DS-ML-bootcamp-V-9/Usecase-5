import streamlit as st
#How do job postings vary by region and gender?"
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import arabic_reshaper
from bidi.algorithm import get_display

# Sample Data (replace this with your actual Jadarat_data)
# Example dataset containing region and gender columns
Jadarat_data=pd.read_csv("Jadarat_data.csv")
st.header("🔍 رحلتي في البحث عن وظيفة")

st.markdown('<p style="text-align:right" dir="rtl">تخرجتُ حديثًا من الجامعة، وبدأتُ رحلة البحث عن وظيفتي الأولى. الجميع يقول لي إن الرياض هي المكان الذي تتوفر فيه الفرص أكثر من أي مدينة أخرى.</p>', unsafe_allow_html=True)

#st.markdown('<h1 style="text-align:right" dir="rtl">💻 هل الرياض هي الوجهة الأفضل للباحثين عن عمل؟</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align:right" dir="rtl">💻لكن، هل هذا صحيح؟ هل الرياض فعلًا هي الوجهة الأفضل للباحثين عن عمل؟</p>', unsafe_allow_html=True)




# 1. Calculate job postings by region
region_counts = Jadarat_data['region'].value_counts().head(10)

# 2. Set up Arabic labels for the chart
title_ar = get_display(arabic_reshaper.reshape("توزيع إعلانات الوظائف حسب المنطقة"))
xlabel_ar = get_display(arabic_reshaper.reshape("المنطقة"))
ylabel_ar = get_display(arabic_reshaper.reshape("عدد إعلانات الوظائف"))

# 3. Reshape the region labels to Arabic
region_labels = [get_display(arabic_reshaper.reshape(region)) for region in region_counts.index]


#st.markdown('<h3 style="text-align:right" dir="rtl">هل الرياض هي المدينة الأكثر إعلانًا عن الوظائف؟</h3>', unsafe_allow_html=True)
# Streamlit Layout
#st.title("هل الرياض هي المدينة الأكثر إعلانًا عن الوظائف؟<")
#st.markdown('<h3 style="text-align:right" dir="rtl">هل هناك تفاوت في الوظائف بين الجنسين؟</h3>', unsafe_allow_html=True)


# 4. Plot Job Postings by Region in Arabic
st.header("كما توقعت، الرياض كانت في الصداره!")
#st.markdown('<h3 style="text-align:right" dir="rtl">ما هي نسبة الوظائف المتاحة لكل جنس؟</h3>', unsafe_allow_html=True)

# Create the bar chart
fig, ax = plt.subplots(figsize=(10, 6))

# Apply custom colors, make Riyadh red
colors = ['red' if region == 'الرياض' else 'lightblue' for region in region_counts.index]
ax.bar(region_labels, region_counts.values, color=colors, edgecolor="black")

# Set titles and labels (in Arabic)
ax.set_title(title_ar, fontsize=14)
ax.set_xlabel(xlabel_ar, fontsize=12)
ax.set_ylabel(ylabel_ar, fontsize=12)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha="right", fontsize=10)

# Add gridlines to the y-axis
ax.grid(axis="y", linestyle="--", alpha=0.7)

# Adjust layout and display the plot
plt.tight_layout()
st.pyplot(fig)



# Job Postings by Gender
st.header("لكن السؤال الذي راودني بعد ذلك كان: هل هناك تفاوت في فرص العمل بين الجنسين؟")

# Count job postings by region and gender
region_gender_counts = Jadarat_data.groupby(['region', 'gender']).size().unstack()

# Reshape the region and gender labels to Arabic
region_gender_counts.index = [get_display(arabic_reshaper.reshape(region)) for region in region_gender_counts.index]
region_gender_counts.columns = [get_display(arabic_reshaper.reshape(gender)) for gender in region_gender_counts.columns]

# Plotting Job Postings by Region and Gender (Bars side by side)
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the bars side by side instead of stacking with custom colors
region_gender_counts.plot(kind='bar', position=0, color=['pink','blue' , 'green'], edgecolor='black', ax=ax)

ax.set_title(get_display(arabic_reshaper.reshape("توزيع إعلانات الوظائف حسب المنطقة والجنس")), fontsize=14)
ax.set_xlabel(get_display(arabic_reshaper.reshape("المنطقة")), fontsize=12)
ax.set_ylabel(get_display(arabic_reshaper.reshape("عدد إعلانات الوظائف")), fontsize=12)
plt.xticks(rotation=45, ha="right")
plt.legend(title=get_display(arabic_reshaper.reshape("الجنس")))
st.pyplot(fig)

st.header("بعض المناطق توفر فرصًا متساوية، بينما في مناطق أخرى كان هناك تباين بسيط بين فرص الرجال والنساء")

# Percentage of Job Postings by Region and Gender
st.header("لكن ما هي النسب الفعلية لكل فئة؟")

# Calculate the percentage of job postings by region and gender
region_gender_percentage = region_gender_counts.divide(region_gender_counts.sum(axis=1), axis=0) * 100

# Plotting Percentage of Job Postings by Region and Gender (Bars side by side)
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the bars side by side for percentage with custom colors
region_gender_percentage.plot(kind='bar', position=0, color=['pink','blue' , 'green'], edgecolor='black', ax=ax)

ax.set_title(get_display(arabic_reshaper.reshape("نسبة إعلانات الوظائف حسب المنطقة والجنس")), fontsize=14)
ax.set_xlabel(get_display(arabic_reshaper.reshape("المنطقة")), fontsize=12)
ax.set_ylabel(get_display(arabic_reshaper.reshape("نسبة إعلانات الوظائف")), fontsize=12)
plt.xticks(rotation=45, ha="right")
plt.legend(title=get_display(arabic_reshaper.reshape("الجنس")))
st.pyplot(fig)

st.markdown('<p style="text-align:right" dir="rtl">الآن، أصبح لدي رؤية أوضح عن سوق العمل. الرياض حقًا هي الوجهة الأكثر إعلانًا عن الوظائف، ولكن هناك أيضًا فرص جيدة في مدن أخرى.</p>', unsafe_allow_html=True)

st.markdown('<p style="text-align:right" dir="rtl">إذا كنتُ أبحث عن أكبر عدد من الفرص، فالرياض هي الخيار الأفضل. أما إذا كنتُ أبحث عن فرص في مناطق أخرى، فمن المهم معرفة طبيعة الوظائف المطروحة هناك.</p>', unsafe_allow_html=True)

