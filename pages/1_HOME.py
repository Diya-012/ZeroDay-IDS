import streamlit as st

# -------------------------
# PAGE CONFIGURATION
# -------------------------

st.set_page_config(
    page_title="Zero-Day IDS",
    page_icon="🛡️",
    layout="wide"
)

# -------------------------
# CUSTOM CSS
# -------------------------

st.markdown("""
<style>

.stApp{
    background-color:#0E1117;
}

div[data-testid="metric-container"]{
    background:#161B22;
    border:1px solid #2B3137;
    padding:18px;
    border-radius:12px;
}

.main-title{
    text-align:center;
    color:#00BFFF;
    font-size:42px;
    font-weight:bold;
}

.sub-title{
    text-align:center;
    color:#B0B0B0;
    font-size:18px;
}

.status-box{
    background:#161B22;
    padding:15px;
    border-radius:10px;
    border-left:5px solid #00BFFF;
}

</style>
""", unsafe_allow_html=True)

# -------------------------
# HEADER
# -------------------------

st.markdown(
"""
<div class="main-title">
🛡️ Zero-Day Intrusion Detection System
</div>

<div class="sub-title">
AI-Powered Cybersecurity Dashboard
</div>
""",
unsafe_allow_html=True
)

st.markdown("---")

# -------------------------
# DASHBOARD METRICS
# -------------------------

col1, col2, col3, col4 = st.columns(4)

col1.metric("📂 Dataset", "Ready")
col2.metric("🤖 Model", "Loaded")
col3.metric("🚨 Threats", "--")
col4.metric("📊 Accuracy", "--")

st.markdown("---")

# -------------------------
# SYSTEM STATUS
# -------------------------

left, right = st.columns([2, 1])

with left:

    st.subheader("🟢 System Status")

    st.success("Autoencoder Model Loaded")

    st.success("TensorFlow Connected")

    st.success("CSV Upload Ready")

    st.success("Threat Detection Ready")

with right:

    st.subheader("📌 Information")

    st.info("Model : Autoencoder")

    st.info("Dataset : UNSW-NB15")

    st.info("Framework : Streamlit")

    st.info("Version : 1.0")

st.markdown("---")

# -------------------------
# PROJECT OVERVIEW
# -------------------------

st.subheader("📖 Project Overview")

st.write("""
The **Zero-Day Intrusion Detection System (IDS)** uses an
**Autoencoder Deep Learning Model** to detect unknown cyber attacks.

Unlike traditional IDS solutions that rely on known signatures,
this project learns the behaviour of normal network traffic and
detects anomalies using reconstruction error.
""")

st.markdown("---")

# -------------------------
# PROJECT WORKFLOW
# -------------------------

st.subheader("⚙️ Detection Workflow")

workflow = """
📂 Upload CSV

⬇️

🧹 Data Preprocessing

⬇️

⚖️ Feature Scaling

⬇️

🤖 Autoencoder Prediction

⬇️

📈 Reconstruction Error

⬇️

🚨 Attack Detection

⬇️

📄 Threat Report
"""

st.code(workflow)

st.markdown("---")

# -------------------------
# TECHNOLOGIES
# -------------------------

st.subheader("🛠️ Technologies Used")

c1, c2, c3 = st.columns(3)

with c1:
    st.success("🐍 Python")
    st.success("📊 Pandas")
    st.success("🔢 NumPy")

with c2:
    st.success("🧠 TensorFlow")
    st.success("🤖 Keras")
    st.success("📈 Plotly")

with c3:
    st.success("🌐 Streamlit")
    st.success("💾 Joblib")
    st.success("🐙 GitHub")

st.markdown("---")

# -------------------------
# FOOTER
# -------------------------

st.caption(
    "© 2026 Zero-Day IDS | Autoencoder-Based Intrusion Detection System | Team Project"
)