import streamlit as st

st.title("ℹ️ About Project")

st.markdown("---")

st.header("🎯 Project Objective")

st.write("""
The **Autoencoder-Based Zero-Day Intrusion Detection System (IDS)** is an AI-powered
cybersecurity solution designed to detect unknown and previously unseen network attacks.

Unlike traditional signature-based IDS, this project uses a **Deep Learning Autoencoder**
to learn normal network behaviour and identify anomalies using reconstruction error.
""")

st.markdown("---")

st.header("🧠 Project Workflow")

st.markdown("""
1. 📁 Upload Network Traffic CSV
2. 🧹 Data Preprocessing
3. ⚖ Feature Scaling
4. 🤖 Autoencoder Prediction
5. 📈 Reconstruction Error Calculation
6. 🚨 Zero-Day Attack Detection
7. 📊 Threat Report Generation
""")

st.markdown("---")

st.header("📂 Dataset")

st.write("""
**Dataset Used:** UNSW-NB15

The dataset contains both normal and malicious network traffic and is widely
used for evaluating Intrusion Detection Systems.

It includes network flow features such as:

- Source/Destination IP
- Protocol
- Service
- Packet Statistics
- Flow Duration
- Attack Categories
""")

st.markdown("---")

st.header("⚙️ Technologies Used")

col1, col2 = st.columns(2)

with col1:
    st.success("🐍 Python")
    st.success("🧠 TensorFlow / Keras")
    st.success("📊 Pandas")
    st.success("🔢 NumPy")

with col2:
    st.success("🌐 Streamlit")
    st.success("📈 Plotly")
    st.success("💾 Joblib")
    st.success("🐙 Git & GitHub")

st.markdown("---")

st.header("🏗 System Architecture")

st.info("""
CSV Dataset
      ↓
Data Preprocessing
      ↓
Feature Scaling
      ↓
Autoencoder Model
      ↓
Reconstruction Error
      ↓
Threshold Comparison
      ↓
Normal / Attack Prediction
      ↓
Threat Report Dashboard
""")

st.markdown("---")

st.header("✨ Key Features")

features = [
    "AI-Based Zero-Day Attack Detection",
    "Autoencoder Deep Learning Model",
    "Real-Time CSV Analysis",
    "Interactive Dashboard",
    "Detection Results Visualization",
    "Reconstruction Error Analysis",
    "Threat Report Generation",
    "Downloadable Reports",
]

for feature in features:
    st.success(feature)

st.markdown("---")

st.header("👥 Team Members")

st.table({
    "Member": [
        "Member 1",
        "Member 2",
        "Member 3",
        "Member 4 (You)"
    ],
    "Responsibility": [
        "Dataset Collection & Preprocessing",
        "Autoencoder Model Development",
        "Evaluation & Performance Analysis",
        "Dashboard Development & Integration"
    ]
})

st.markdown("---")

st.header("🚀 Future Scope")

st.write("""
Future improvements may include:

- Live network packet capture
- Real-time monitoring dashboard
- Email alerts for detected attacks
- Cloud deployment
- Multi-class attack classification
- Explainable AI (XAI)
- SIEM integration
""")

st.markdown("---")

st.success("✅ Project Successfully Developed using Deep Learning & Streamlit")

st.caption("© 2026 Zero-Day IDS | AI-Powered Intrusion Detection System")