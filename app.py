import streamlit as st
import pandas as pd

 
# تحميل البيانات
@st.cache_data
def load_data():
    df = pd.read_csv("Data/Jadarat_data.csv")
    return df

data = load_data()

# تحسين الشكل العام باستخدام HTML و CSS
st.markdown(
    """
    <style>
        .main-title {
            background-color: #E6E6FA;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            font-size: 30px;
            font-weight: bold;
            color: #4B0082;
            margin-bottom: 20px;
        }
        .sub-title {
            font-size: 22px;
            color: #4B0082;
            font-weight: bold;
            margin-top: 20px;
            margin-bottom: 10px;
            text-align: right;
        }
        .content {
            font-size: 18px;
            color: #333;
            margin-bottom: 20px;
            text-align: right;
        }
        .image-text-container {
            display: flex;
            align-items: center;
            gap: 20px;
        }
        .small-image {
            width: 150px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# عنوان التطبيق مع تحسين الشكل
st.markdown("<div class='main-title'>قراءة فرص سوق العمل لمستقبل أفضل!</div>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 3])
with col1:
    st.image("Photos/anxiety.png", caption="")
with col2:
    st.markdown("<div class='content'>ريناد خريجة المرحلة الثانوية، وتقطن في المنطقة الشرقية، لكنها ترغب في معرفة توجه سوق العمل السعودي بشكل عام قبل أن تختار تخصصها الجامعي.</div>", unsafe_allow_html=True)
    st.markdown("<div class='content'> </div>", unsafe_allow_html=True)
    st.markdown("<div class='content'> </div>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 3])
with col1:
    st.image("Photos/Jadarat.png", caption="")
with col2:
    st.markdown("<div class='sub-title'>استعانت ريناد بمنصة جدارات لتبدأ رحلة استكشافها للمجالات المطلوبة في سوق العمل</div>", unsafe_allow_html=True)
    st.markdown("<div class='content'>جدارات هي المنصة الموحدة للتوظيف وهي منصة وطنية تهدف لأن تكون الممكن الرئيسي لتوظيف القوة العاملة السعودية وذلك من خلال تسهيل رحلة الباحثين عن العمل في استكشاف جميع وظائف القطاع العام والخاص في سوق العمل السعودي.</div>", unsafe_allow_html=True)

# المنطقة ذات أكبر فرص وظيفية
st.markdown("<div class='sub-title'>ما هي المنطقة التي تضم أكبر عدد من الفرص الوظيفية؟</div>", unsafe_allow_html=True)
st.image("Photos/regions.png", caption="توزيع الوظائف في مختلف المناطق السعودية")
st.markdown("<div class='content'>بدأت أولاً بالبحث عن المنطقة التي تضم أكبر عدد من الفرص الوظيفية، فوجدت أن الرياض تتصدر الترتيب بعدد إعلانات الوظائف مضاعفة عدد إعلانات ثاني منطقة في الترتيب ألا وهي مكة المكرمة، وهذا نظراً لكونها أصبحت مركزًا لتجمع الشركات والمؤسسات.</div>", unsafe_allow_html=True)

# أكثر الوظائف طلبًا
st.markdown("<div class='sub-title'>ما هي أكثر الوظائف طلبًا في السعودية؟</div>", unsafe_allow_html=True)
st.image("Photos/jobTitels.png", caption="أكثر الوظائف طلبًا في سوق العمل السعودي")
st.markdown("<div class='content'>ومن ثم انتقلت للبحث عن الوظائف الأكثر طلبًا من قبل الجهات المختلفة، واتضح أن مجال التسويق ومجال المبيعات هو الأكثر طلبًا في سوق العمل السعودي!</div>", unsafe_allow_html=True)

# فرص النساء مقابل الرجال
st.markdown("<div class='sub-title'>ما هو توزيع الفرص الوظيفية حسب الجنس؟</div>", unsafe_allow_html=True)
st.image("Photos/genders.png", caption="توزيع الطلب حسب الجنس")
st.markdown("<div class='content'>وبعد ذلك قررت ألا تتسرع وترى أولاً هل فرص النساء في سوق العمل مقاربة لفرص الرجال أم لا؟ ما هو الجنس الأكثر طلبًا في سوق العمل؟ وتبين أن النسب متقاربة جدًا بل وأن الوظائف التي تبحث عن الجنسين تملك أكبر نسبة (%39.3).</div>", unsafe_allow_html=True)

# فرص حديثي التخرج
st.markdown("<div class='sub-title'>هل سوق العمل يبحث عن حديثي التخرج؟</div>", unsafe_allow_html=True)
st.image("Photos/graduates.png", caption="الفرص الوظيفية لحديثي التخرج")
st.markdown("<div class='content'>اتضح أيضًا لريناد أن سوق العمل السعودي يبحث عن حديثي التخرج أو الأشخاص الذين بدون خبرة عمل سابقة بنسبة كبيرة بل وأنها أكبر من نسبة البحث عن ذوي الخبرة.</div>", unsafe_allow_html=True)

# اكتساب المعرفة لاتخاذ القرار
st.markdown("<div class='sub-title'>ماذا تعلمت ريناد من هذا البحث؟</div>", unsafe_allow_html=True)
st.markdown("<div class='content'>اكتسبت ريناد بعض المعلومات التي سوف تسهم في مساعدتها أن تتخذ قرارًا يخص تخصصها الجامعي، فهي الآن تعرف أين أغلب فرص العمل وما هي أكثر المجالات المطلوبة. أيضًا اتضح لها أن الفرص الوظيفية متاحة للجنسين تقريبًا بالتساوي، وأيضًا أن سوق العمل يبحث عن حديثي التخرج. فالآن أصبحت قادرة على بناء أساس يساعدها في اتخاذ قرارها.</div>", unsafe_allow_html=True)

