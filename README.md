# 📌 Jobs Employment Landscape

## 📖 Overview
This project analyzes job postings to uncover insights into the employment landscape. It explores trends such as **most in-demand jobs, salary distributions, required skills, and language preferences** using data visualization techniques.

---
## 🔗 Streamlit app
https://usecase-5-eutgn5gkld728cpcwmdvs9.streamlit.app/
## 📊 Key Features
- 📈 **Job Trends Over Time** – Track job posting patterns.
- 💼 **Most Common Job Titles** – Identify high-demand roles.
- 💰 **Salary Analysis** – Explore salary distributions.
- 🛠️ **Top Skills & Languages** – Find essential job requirements.
- 🚻 **Gender-Based Job Distribution** – Analyze job postings by gender.

---

## 📂 Dataset
The dataset includes key columns:
- `job_title`, `job_date`, `job_desc`, `job_tasks`
- `comp_name`, `comp_size`, `qualif`, `region`, `city`
- `required_languages`, `Skills`, `Certificate`, `Salary`, `Benefits`

---

## 📦 Installation & Setup
### 🔹 Install Dependencies
Run the following command to install the required packages:
```bash
pip install numpy pandas matplotlib seaborn scipy ydata_profiling hijridate arabic_reshaper bidi
```

### 🔹 Running the Analysis
Execute the Python script to generate insights and visualizations:
```python
python analysis.py
```

If using **Jupyter Notebook**, make sure to enable inline plotting:
```python
%matplotlib inline
```

---

## 📌 Sample Output
### 📊 Most Common Job Titles
```python
top_jobs = employment_landscape['job_title'].value_counts().head(10)
sns.barplot(x=top_jobs.values, y=top_jobs.index, palette="coolwarm")
plt.xlabel("عدد الوظائف")
plt.ylabel("المسمى الوظيفي")
plt.title("أكثر 10 وظائف مطلوبة")
plt.show()
```
✅ **Output:**  
![image](https://github.com/user-attachments/assets/4fe2b8f3-a040-4f7d-ba9a-2bd6c471397f)

---

### 📈 Job Trends Over Time
```python
jobs_over_time = employment_landscape.groupby('date').size()
plt.plot(jobs_over_time.index, jobs_over_time.values, marker="o", color="red")
plt.xlabel("التاريخ")
plt.ylabel("عدد الوظائف")
plt.title("توزيع الوظائف عبر الوقت")
plt.show()
```
✅ **Output:**  
![Job Trends](sample_output/job_trends.png)

---

## 🔗 Future Improvements
- **Predictive analysis** using machine learning.
- **Interactive dashboards** for real-time job insights.

🚀 **Contributions & feedback are welcome!**

