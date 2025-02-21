import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import ast

# Styling
st.markdown("""
    <style>
        /* General page styling */
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f4f7fc;
            color: #333;
            line-height: 1.6;
        }

        /* Header styling */
        h1 {
            font-size: 3rem;
            text-align: right;
            color: #0056b3;
            margin-bottom: 0.5em;
            font-weight: 700;
        }

        h3 {
            font-size: 2.5rem;
            color: #333;
            text-align: right;
            margin-top: 1em;
            font-weight: 600;
        }

        h4 {
            font-size: 1.2rem;
            color: #555;
            text-align: right;
            line-height: 1.8;
            margin-bottom: 1em;
        }

        /* Content container */
        .content-container {
            background-color: #ffffff;
            padding: 25px;
            border-radius: 12px;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
            margin-bottom: 3em;
            transition: all 0.3s ease;
        }

        /* Hover effect on content container */
        .content-container:hover {
            box-shadow: 0 12px 30px rgba(0, 0, 0, 0.15);
            transform: scale(1.02);
        }

        /* Footer */
        .footer {
            text-align: center;
            padding: 1em;
            background-color: #0056b3;
            color: white;
            font-size: 1rem;
            border-radius: 8px;
            margin-top: 3em;
        }

        /* Image styling */
        img {
            border-radius: 8px;
            max-width: 100%;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
            margin-top: 1em;
        }

        /* Animation for the elements */
        .animate-content {
            opacity: 0;
            animation: fadeIn 2s forwards;
        }

        @keyframes fadeIn {
            from {
                opacity: 0;
            }
            to {
                opacity: 1;
            }
        }
    </style>
""", unsafe_allow_html=True)

# Display the header image
st.image('images/kdkd.png', use_container_width=True)

# Display the main title
st.markdown('<h1 class="animate-content">📊 تحليل بيانات الوظائف في المملكة العربية السعودية</h1>', unsafe_allow_html=True)

# Introduction
st.markdown('''<div class="content-container animate-content">
                <h3>قمنا بتحليل البيانات المتعلقة بالإعلانات الوظيفية في السعودية، 
                وهدفنا هو تقديم نظرة شاملة على الوضع الوظيفي في المملكة من خلال تحليلات تتعلق بالرواتب، توزيع الوظائف حسب المناطق، 
                توزيع الوظائف حسب الخبرات المطلوبة، بالإضافة إلى توزيع عقود العمل.</h3>
            </div>''', unsafe_allow_html=True)

# Proportion of Job Postings by Region
st.markdown('''<h3 class="animate-content">🌍 توزيع الإعلانات الوظيفية حسب المناطق</h3>''', unsafe_allow_html=True)
st.markdown('''<div class="content-container animate-content">
                <h4>من خلال تحليل بيانات الوظائف، نلاحظ أن معظم الإعلانات الوظيفية تأتي من منطقة الرياض،
                تليها مكة المكرمة والمنطقة الشرقية. بينما تكون المناطق الأخرى مثل عسير وتبوك وغيرها تساهم بنسب أقل بكثير في الإعلانات.</h4>
            </div>''', unsafe_allow_html=True)
st.image("images/1.png", caption="Proportion of Job Postings by Region in Saudi Arabia")

# Gender Preference in Job Postings
st.markdown('''<h3 class="animate-content">👨‍💻 توزيع الإعلانات الوظيفية حسب الجنس</h3>''', unsafe_allow_html=True)
st.markdown('''<div class="content-container animate-content">
                <h4>هناك تفضيل واضح في بعض الإعلانات الوظيفية لاستقطاب جميع الأجناس (كلا الجنسين)، 
                بينما هناك بعض الوظائف المخصصة فقط للذكور أو الإناث. لكن بشكل عام، تهيمن الإعلانات التي تقبل كلا الجنسين.</h4>
            </div>''', unsafe_allow_html=True)
st.image("images/2.png", caption="Gender Preference in Job Postings")

# Salary Distribution for Fresh Graduates
st.markdown('''<h3 class="animate-content">💼 توزيع الرواتب للخريجين الجدد</h3>''', unsafe_allow_html=True)
st.markdown('''<div class="content-container animate-content">
                <h4>توزيع الرواتب يظهر أن الغالبية العظمى من الخريجين الجدد يتقاضون رواتب تتراوح بين 5000 و 10000 ريال، 
                مع بعض الحالات التي تتجاوز هذا المدى. لكن تظل الرواتب بشكل عام منخفضة مقارنة ببقية الخبرات.</h4>
            </div>''', unsafe_allow_html=True)
st.image("images/3.png", caption="Salary Distribution for Fresh Graduates")

# Proportion of Job Postings for Fresh Graduates vs Experienced Candidates
st.markdown('''<h3 class="animate-content">👩‍🎓 الإعلانات الوظيفية للخريجين الجدد مقابل الخبرات المطلوبة</h3>''', unsafe_allow_html=True)
st.markdown('''<div class="content-container animate-content">
                <h4>الوظائف الموجهة للخريجين الجدد هي الأكثر انتشارًا، حيث تشكل أكثر من نصف الإعلانات الوظيفية،
                مقارنة بالإعلانات التي تطلب خبرات متعددة التي تشكل نسبة أقل بكثير.</h4>
            </div>''', unsafe_allow_html=True)
st.image("images/4.png", caption="Proportion of Job Postings for Fresh Graduates vs Experienced Candidates")

# Contract Type Distribution
st.markdown('''<h3 class="animate-content">📝 توزيع نوع العقد في الإعلانات الوظيفية</h3>''', unsafe_allow_html=True)
st.markdown('''<div class="content-container animate-content">
                <h4>فيما يتعلق بنوع العقد، نجد أن غالبية الوظائف المعروضة هي بعقود دوام كامل، 
                بينما هناك عدد قليل من الوظائف التي تقدم عقودًا للعمل عن بعد.</h4>
            </div>''', unsafe_allow_html=True)
st.image("images/5.png", caption="Contract Type Distribution in Job Postings")

# Conclusion
st.markdown('''<h3 class="animate-content">💬 الخاتمة</h3>''', unsafe_allow_html=True)
st.markdown('''<div class="content-container animate-content">
                <h4>باستخدام هذا التحليل، يمكننا ملاحظة توجهات مهمة مثل التوزيع غير المتكافئ للإعلانات 
                الوظيفية بين المناطق في المملكة، بالإضافة إلى الرواتب التي تهيمن عليها الرواتب الأقل للخريجين الجدد.
                كما أن تحليل الخبرات المطلوبة يبرز التحديات التي يواجهها الباحثون عن وظائف ذوي الخبرة. هذه الرؤية توفر لنا معطيات تساعدنا 
                في اتخاذ قرارات أكثر استراتيجية حول مستقبلنا المهني أو نوع الوظائف التي نرغب في التقديم لها.</h4>
            </div>''', unsafe_allow_html=True)

# Footer
st.markdown('''<div class="footer">تم التحليل بواسطة مشعل الشقحاء | جميع الحقوق محفوظة 2025</div>''', unsafe_allow_html=True)
