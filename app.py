import streamlit as st
import pandas as pd
import plotly.express as px

from utils.nlp import clean_text, extract_keywords
from utils.generator import template_generator
from utils.scorer import rank_subjects
from utils.spam_detector import check_spam
from utils.intent_detector import detect_intent
from utils.tone_detector import detect_tone
from utils.audience_detector import detect_audience
from utils.explainability import explain
from utils.ab_testing import compare_subjects

# =====================
# PAGE CONFIG
# =====================

st.set_page_config(
    page_title="AI Subject Line Composer",
    page_icon="✉️",
    layout="wide"
)
st.markdown("""
<style>

/* Main Background */
.stApp {
    background-color: #0f172a;
    color: white;
}

/* Headers */
h1 {
    color: #60a5fa;
    text-align: center;
    font-weight: 800;
}

h2,h3 {
    color: #93c5fd;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #111827;
}

/* Text Area */
textarea {
    background-color: #1f2937 !important;
    color: white !important;
    border-radius: 12px !important;
    border: 2px solid #3b82f6 !important;
}

/* Generate Button */
div.stButton > button:first-child {
    background: #2563eb;
    color: white;
    border-radius: 12px;
    border: none;
    font-weight: bold;
    height: 3em;
    width: 100%;
}

/* Generate Button Hover */
div.stButton > button:hover {
    background: #1d4ed8;
    color: white;
}

/* Success Box */
div[data-baseweb="notification"] {
    border-radius: 12px;
}

/* Metrics */
[data-testid="metric-container"] {
    background-color: #1f2937;
    border: 1px solid #374151;
    padding: 15px;
    border-radius: 15px;
}

/* Download Button */
.stDownloadButton button {
    background-color: #10b981 !important;
    color: white !important;
    border-radius: 12px !important;
    font-weight: bold !important;
}

/* Input Fields */
input {
    background-color: #1f2937 !important;
    color: white !important;
}

/* Charts Container */
.element-container {
    border-radius: 12px;
}

</style>
""", unsafe_allow_html=True)

# =====================
# SESSION STATE
# =====================

if "generated" not in st.session_state:
    st.session_state.generated = False

if "ranked" not in st.session_state:
    st.session_state.ranked = []

if "intent" not in st.session_state:
    st.session_state.intent = ""

if "tone" not in st.session_state:
    st.session_state.tone = ""

if "audience" not in st.session_state:
    st.session_state.audience = ""

if "best_subject" not in st.session_state:
    st.session_state.best_subject = ("", 0)

if "worst_subject" not in st.session_state:
    st.session_state.worst_subject = ("", 0)

if "spam_counts" not in st.session_state:
    st.session_state.spam_counts = {
        "Safe": 0,
        "Spam": 0
    }

# =====================
# TITLE
# =====================
st.markdown("""
            <div style="
            background: linear-gradient(90deg,#111827,#1f2937,#2563eb);
            padding:25px;
            border-radius:20px;
            text-align:center;
            margin-bottom:20px;
            ">
            
            <h1 style="color:white;">
            📧 AI Subject Line Composer
            </h1>
            <p style="color:#d1d5db;font-size:18px;">
            Generate High-Converting Email Subject Lines using NLP, Machine Learning, Spam Detection & A/B Testing
            </p>
            </div>
            """, unsafe_allow_html=True)
st.sidebar.title(" About Project")

st.sidebar.info("""
                Features:
                
                • NLP Keyword Extraction
                
                • Intent Detection
                
                • Tone Detection
                
                • Audience Detection
                
                • Subject Generation
                
                • Spam Detection
                
                • Open Rate Prediction
                
                • A/B Testing
                
                """)

email = st.text_area(
    "Enter Email Body",
    height=200
    )

# =====================
# GENERATE BUTTON
# =====================

if st.button("Generate"):

    if not email.strip():
        st.warning("Please enter an email body.")
        st.stop()

    clean = clean_text(email)

    intent = detect_intent(email)
    tone = detect_tone(email)
    audience = detect_audience(email)

    keywords = extract_keywords(clean)

    subjects = template_generator(
        keywords,
        intent,
        tone,
        audience
    )

    ranked = rank_subjects(subjects)

    safe_subjects = []

    spam_counts = {
        "Safe": 0,
        "Spam": 0
    }

    for subject, score in ranked:

        spam_result = check_spam(subject)

        if str(spam_result).lower() == "safe":
            safe_subjects.append((subject, score))
            spam_counts["Safe"] += 1
        else:
            spam_counts["Spam"] += 1

    if len(safe_subjects) > 0:
        best_subject = safe_subjects[0]
    else:
        best_subject = ranked[0]

    worst_subject = ranked[-1]

    st.session_state.generated = True
    st.session_state.ranked = ranked
    st.session_state.intent = intent
    st.session_state.tone = tone
    st.session_state.audience = audience
    st.session_state.best_subject = best_subject
    st.session_state.worst_subject = worst_subject
    st.session_state.spam_counts = spam_counts

# =====================
# DISPLAY RESULTS
# =====================

if st.session_state.generated:

    ranked = st.session_state.ranked

    st.subheader(" Email Analysis")

    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Intent", st.session_state.intent)
        
    with col2:
        st.metric("Tone", st.session_state.tone)
        
    with col3:
        st.metric("Audience", st.session_state.audience)
        
    st.sidebar.title("📈 Results")
    
    st.sidebar.metric(
    "Generated Subjects",
    len(ranked)
    )
    
    st.sidebar.metric(
    "Safe Subjects",
    st.session_state.spam_counts["Safe"]
    )
    
    st.sidebar.metric(
    "Spam Subjects",
    st.session_state.spam_counts["Spam"]
    )
    
    st.success(
        f" Recommended Subject: {st.session_state.best_subject[0]} | Score: {st.session_state.best_subject[1]}"
        )
    
    st.error(
        f" Least Ranked Subject: {st.session_state.worst_subject[0]} | Score: {st.session_state.worst_subject[1]}"
        )
    
    st.subheader(" Generated Subject Lines")
    
    for subject, score in ranked:
        
        spam_result = check_spam(subject)
        
        st.write(f"### {subject}")
        
        st.write(
            f"**Predicted Open Rate:** {score}"
            )

        st.write(
            f"**Spam Status:** {spam_result}"
            )
        
        reasons = explain(subject)

        st.write("**Reason:**")

        if len(reasons) == 0:
            st.write("✓ General professional subject line")
        else:
            for r in reasons:
                st.write(f"✓ {r}")

        st.write("---")

    # =====================
    # CSV DOWNLOAD
    # =====================
    df_download = pd.DataFrame({
        "Subject": [s for s, score in ranked],
        "Predicted Score": [score for s, score in ranked],
        "Spam Status": [check_spam(s) for s, score in ranked],
        "Intent": [st.session_state.intent] * len(ranked),
        "Tone": [st.session_state.tone] * len(ranked),
        "Audience": [st.session_state.audience] * len(ranked)
    })
    
    csv = df_download.to_csv(index=False)
    
    st.download_button(
        label=" Download Results CSV",
        data=csv,
        file_name="subject_lines.csv",
        mime="text/csv"
        )

    # =====================
    # SCORE CHART
    # =====================
    
    st.subheader(" Subject Score Analysis")
    
    df_chart = pd.DataFrame(
        ranked,
        columns=["Subject", "Score"]
        )
    
    fig = px.bar(
        df_chart,
        x="Subject",
        y="Score",
        title="Predicted Open Rate by Subject Line"
        )
    
    st.plotly_chart(
        fig,
        use_container_width=True
        )

    # =====================
    # SPAM CHART
    # =====================
    st.subheader(" Spam vs Safe Analysis")
    
    spam_df = pd.DataFrame(
        st.session_state.spam_counts.items(),
        columns=["Type", "Count"]
        )

    fig2 = px.pie(
        spam_df,
        names="Type",
        values="Count",
        title="Spam vs Safe Subjects"
        )

    st.plotly_chart(
        fig2,
        use_container_width=True
        )




# =====================
# A/B TESTING
# =====================

if st.session_state.generated:

    ranked = st.session_state.ranked

    st.subheader("A/B Testing")

    default_a = ranked[0][0]

    if len(ranked) > 1:
        default_b = ranked[1][0]
    else:
        default_b = ""

    subject_a = st.text_input(
        "Subject A",
        value=default_a,
        key="subject_a"
    )

    subject_b = st.text_input(
        "Subject B",
        value=default_b,
        key="subject_b"
    )

    if st.button("Compare Subjects"):
        winner, confidence = compare_subjects(
            subject_a,
            subject_b,
            ranked
            )
        
        st.success(f"Winner: {winner}")
        st.write(f"Confidence Score: {confidence}")


# =====================================
# FOOTER
# =====================================

st.markdown("---")

st.markdown("""
<div style="
text-align:center;
color:#9ca3af;
padding:20px;
font-size:14px;
">
AI Subject Line Composer<br>
Built using Python • NLP • Machine Learning • Streamlit<br>
Developed by Sandhya Choubey
</div>
""", unsafe_allow_html=True)