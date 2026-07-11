import streamlit as st

# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="Zero-Day IDS",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================================================
# CUSTOM CSS
# ==================================================

st.markdown("""
<style>

.stApp{
    background-color:#0E1117;
}

section[data-testid="stSidebar"]{
    background-color:#1A1F2E;
}

div[data-testid="metric-container"]{
    background-color:#161B22;
    border:1px solid #30363D;
    padding:20px;
    border-radius:12px;
}

h1,h2,h3{
    color:white;
}

</style>
""", unsafe_allow_html=True)

# ==================================================
# SIDEBAR
# ==================================================

st.sidebar.image("assests/logo.png.png", width=170)

st.sidebar.markdown(
"""
<h2 style='text-align:center;color:white;'>
Zero-Day IDS
</h2>

<p style='text-align:center;color:lightgray;'>
AI-Powered Intrusion Detection System
</p>
""",
unsafe_allow_html=True
)

st.sidebar.markdown("---")

st.sidebar.success("🟢 System Online")

st.sidebar.info("🤖 Autoencoder Model")

st.sidebar.warning("📂 Waiting for Dataset")

st.sidebar.markdown("---")

st.sidebar.markdown(
"""
### 📌 Quick Navigation

Use the pages above to

• Upload CSV

• Detect Intrusions

• View Reconstruction Error

• Generate Threat Report
"""
)

# ==================================================
# MAIN PAGE
# ==================================================

st.title("🛡️ Zero-Day Intrusion Detection System")

st.subheader("AI-Powered Network Intrusion Detection Dashboard")

st.info("""
### Welcome 👋

This dashboard uses an **Autoencoder-Based Deep Learning Model**
to detect **Zero-Day Network Intrusions**.

Upload a network traffic CSV from the sidebar to begin analysis.
""")

st.markdown("---")

# ==================================================
# METRICS
# ==================================================

col1,col2,col3,col4=st.columns(4)

with col1:
    st.metric(
        "📂 Dataset",
        "Not Uploaded"
    )

with col2:
    st.metric(
        "🤖 AI Model",
        "Waiting"
    )

with col3:
    st.metric(
        "🚨 Threats",
        "0"
    )

with col4:
    st.metric(
        "📊 Accuracy",
        "--"
    )

st.markdown("---")

# ==================================================
# PROJECT OVERVIEW
# ==================================================

st.header("🔍 Project Overview")

st.write("""
This project detects **Zero-Day Cyber Attacks**
using an **Autoencoder Deep Learning Model**.

The system analyses network traffic,
calculates reconstruction error,
and identifies anomalous behaviour that
may indicate previously unseen attacks.
""")

# ==================================================
# FEATURES
# ==================================================

st.header("🚀 Features")

left,right=st.columns(2)

with left:

    st.success("✔ Upload Network Traffic CSV")

    st.success("✔ Autoencoder Deep Learning")

    st.success("✔ Zero-Day Detection")

with right:

    st.success("✔ Reconstruction Error Graph")

    st.success("✔ Threat Report")

    st.success("✔ Interactive Dashboard")

st.markdown("---")

# ==================================================
# WORKFLOW
# ==================================================

st.header("⚙ Detection Workflow")

st.write("""
1️⃣ Upload CSV Dataset

⬇️

2️⃣ Data Preprocessing

⬇️

3️⃣ Autoencoder Prediction

⬇️

4️⃣ Reconstruction Error Calculation

⬇️

5️⃣ Detect Anomalies

⬇️

6️⃣ Generate Threat Report
""")

st.markdown("---")

# ==================================================
# PROJECT STATUS
# ==================================================

st.header("📈 Dashboard Status")

c1,c2,c3=st.columns(3)

with c1:

    st.success("System Ready")

with c2:

    st.info("Awaiting Dataset Upload")

with c3:

    st.warning("AI Detection Pending")

st.markdown("---")

# ==================================================
# FOOTER
# ==================================================

st.caption(
"© 2026 Zero-Day IDS | Autoencoder-Based Zero-Day Intrusion Detection Framework | Team Project"
)

from pathlib import Path

model_path = Path("Autoencoder-ZeroDay-IDS/results/autoencoder_model.keras")
scaler_path = Path("Autoencoder-ZeroDay-IDS/scaler/standard_scaler.pkl")
threshold_path = Path("Autoencoder-ZeroDay-IDS/results/best_threshold.pkl")

st.write("Model:", model_path.exists())
st.write("Scaler:", scaler_path.exists())
st.write("Threshold:", threshold_path.exists())