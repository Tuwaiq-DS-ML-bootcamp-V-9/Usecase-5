import streamlit as st

# Styling
st.markdown("""
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f9f9f9;
            color: #333;
        }
        h1, h3, h4 {
            color: #007bff;
        }
        h1 {
            font-size: 2.5em;
            text-align: right;
        }
        h3 {
            font-size: 1.8em;
            text-align: right;
            margin-top: 20px;
        }
        h4 {
            font-size: 1.2em;
            text-align: right;
            margin-top: 10px;
            line-height: 1.6;
        }
        .image-container {
            display: flex;
            justify-content: center;
            margin-top: 30px;
        }
        .image-container img {
            max-width: 100%;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        .content-container {
            background-color: white;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }
        .content-container h4 {
            text-align: right;
        }
    </style>
""", unsafe_allow_html=True)

# Display the main title
st.markdown('<h1>📊 تحليل بيانات الوظائف في المملكة العربية السعودية</h1>', unsafe_allow_html=True)

# Introduction
st.markdown('''<div class="content-container">
            <h3>قمنا بتحليل البيانات المتعلقة بالإعلانات الوظيفية في السعودية، 
            وهدفنا هو تقديم نظرة شاملة على الوضع الوظيفي في المملكة من خلال تحليلات تتعلق بالرواتب، توزيع الوظائف حسب المناطق، 
            توزيع الوظائف حسب الخبرات المطلوبة، بالإضافة إلى توزيع عقود العمل.</h3>
        </div>''', unsafe_allow_html=True)

# Proportion of Job Postings by Region
st.markdown('''<h3>🌍 توزيع الإعلانات الوظيفية حسب المناطق</h3>''', unsafe_allow_html=True)
st.markdown('''<div class="content-container">
            <h4>من خلال تحليل بيانات الوظائف، نلاحظ أن معظم الإعلانات الوظيفية تأتي من منطقة الرياض،
            تليها مكة المكرمة والمنطقة الشرقية. بينما تكون المناطق الأخرى مثل عسير وتبوك وغيرها تساهم بنسب أقل بكثير في الإعلانات.</h4>
        </div>''', unsafe_allow_html=True)
st.markdown('<div class="image-container"><img src="images/1.png" alt="Proportion of Job Postings by Region"></div>', unsafe_allow_html=True)

# Gender Preference in Job Postings
st.markdown('''<h3>👨‍💻 توزيع الإعلانات الوظيفية حسب الجنس</h3>''', unsafe_allow_html=True)
st.markdown('''<div class="content-container">
            <h4>هناك تفضيل واضح في بعض الإعلانات الوظيفية لاستقطاب جميع الأجناس (كلا الجنسين)، 
            بينما هناك بعض الوظائف المخصصة فقط للذكور أو الإناث. لكن بشكل عام، تهيمن الإعلانات التي تقبل كلا الجنسين.</h4>
        </div>''', unsafe_allow_html=True)
st.markdown('<div class="image-container"><img src="images/2.png" alt="Gender Preference in Job Postings"></div>', unsafe_allow_html=True)

# Salary Distribution for Fresh Graduates
st.markdown('''<h3>💼 توزيع الرواتب للخريجين الجدد</h3>''', unsafe_allow_html=True)
st.markdown('''<div class="content-container">
            <h4>توزيع الرواتب يظهر أن الغالبية العظمى من الخريجين الجدد يتقاضون رواتب تتراوح بين 5000 و 10000 ريال، 
            مع بعض الحالات التي تتجاوز هذا المدى. لكن تظل الرواتب بشكل عام منخفضة مقارنة ببقية الخبرات.</h4>
        </div>''', unsafe_allow_html=True)
st.markdown('<div class="image-container"><img src="images/3.png" alt="Salary Distribution for Fresh Graduates"></div>', unsafe_allow_html=True)

# Proportion of Job Postings for Fresh Graduates vs Experienced Candidates
st.markdown('''<h3>👩‍🎓 الإعلانات الوظيفية للخريجين الجدد مقابل الخبرات المطلوبة</h3>''', unsafe_allow_html=True)
st.markdown('''<div class="content-container">
            <h4>الوظائف الموجهة للخريجين الجدد هي الأكثر انتشارًا، حيث تشكل أكثر من نصف الإعلانات الوظيفية،
            مقارنة بالإعلانات التي تطلب خبرات متعددة التي تشكل نسبة أقل بكثير.</h4>
        </div>''', unsafe_allow_html=True)
st.markdown('<div class="image-container"><img src="images/4.png" alt="Proportion of Job Postings for Fresh Graduates vs Experienced Candidates"></div>', unsafe_allow_html=True)

# Contract Type Distribution
st.markdown('''<h3>📝 توزيع نوع العقد في الإعلانات الوظيفية</h3>''', unsafe_allow_html=True)
st.markdown('''<div class="content-container">
            <h4>فيما يتعلق بنوع العقد، نجد أن غالبية الوظائف المعروضة هي بعقود دوام كامل، 
            بينما هناك عدد قليل من الوظائف التي تقدم عقودًا للعمل عن بعد.</h4>
        </div>''', unsafe_allow_html=True)
st.markdown('<div class="image-container"><img src="images/5.png" alt="Contract Type Distribution in Job Postings"></div>', unsafe_allow_html=True)

# Conclusion
st.markdown('''<h3>💬 الخاتمة</h3>''', unsafe_allow_html=True)
st.markdown('''<div class="content-container">
            <h4>باستخدام هذا التحليل، يمكننا ملاحظة توجهات مهمة مثل التوزيع غير المتكافئ للإعلانات 
            الوظيفية بين المناطق في المملكة، بالإضافة إلى الرواتب التي تهيمن عليها الرواتب الأقل للخريجين الجدد.
            كما أن تحليل الخبرات المطلوبة يبرز التحديات التي يواجهها الباحثون عن وظائف ذوي الخبرة. هذه الرؤية توفر لنا معطيات تساعدنا 
            في اتخاذ قرارات أكثر استراتيجية حول مستقبلنا المهني أو نوع الوظائف التي نرغب في التقديم لها.</h4>
        </div>''', unsafe_allow_html=True)
