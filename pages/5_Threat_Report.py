import streamlit as st
import pandas as pd

st.title("🚨 Threat Report")

# Check whether AI Detection has been run
if "results" not in st.session_state:
    st.warning("⚠️ Please upload a dataset and run AI Detection first.")
    st.stop()

results = st.session_state["results"]

# ==========================
# Statistics
# ==========================

total = len(results)
attacks = (results["Prediction"] == "🚨 Attack").sum()
normal = (results["Prediction"] == "✅ Normal").sum()
attack_rate = (attacks / total) * 100

# Risk Level
if attack_rate >= 70:
    risk = "🔴 HIGH"
elif attack_rate >= 30:
    risk = "🟡 MEDIUM"
else:
    risk = "🟢 LOW"

# ==========================
# Summary
# ==========================

st.subheader("📋 Threat Summary")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Records", total)
col2.metric("Attacks", attacks)
col3.metric("Normal", normal)
col4.metric("Risk Level", risk)

st.divider()

# ==========================
# Report
# ==========================

st.subheader("📝 Security Assessment")

st.write(f"""
### Overall Analysis

- **Total Network Records:** {total}
- **Detected Attacks:** {attacks}
- **Normal Records:** {normal}
- **Attack Percentage:** {attack_rate:.2f}%
- **Overall Risk Level:** {risk}

The Autoencoder-Based Zero-Day Intrusion Detection System analyzed the uploaded network traffic and identified anomalous behaviour using reconstruction error.

Records classified as **🚨 Attack** exceeded the learned anomaly threshold and are considered suspicious.

Security administrators should further investigate these anomalous network activities.
""")

st.divider()

# ==========================
# Recommendations
# ==========================

st.subheader("🛡 Security Recommendations")

recommendations = [
    "Monitor suspicious IP addresses.",
    "Investigate anomalous traffic immediately.",
    "Enable IDS/IPS logging.",
    "Update firewall and access control rules.",
    "Perform malware and vulnerability scans.",
    "Review authentication logs.",
    "Continue monitoring using the AI IDS model."
]

for rec in recommendations:
    st.success(rec)

st.divider()

# ==========================
# High Risk Records
# ==========================

st.subheader("🚨 Top 20 Suspicious Records")

top = results.sort_values(
    by="Reconstruction Error",
    ascending=False
).head(20)

st.dataframe(top, use_container_width=True)

st.divider()

# ==========================
# Download Report
# ==========================

report = f"""
===============================
ZERO-DAY IDS THREAT REPORT
===============================

Total Records : {total}
Attacks       : {attacks}
Normal        : {normal}
Attack Rate   : {attack_rate:.2f}%
Risk Level    : {risk}

The Autoencoder model detected anomalous network behaviour based on reconstruction error.

Recommendation:
- Monitor suspicious traffic.
- Update firewall policies.
- Investigate flagged records.
- Continue network monitoring.
"""

st.download_button(
    "📥 Download Threat Report",
    report,
    "Threat_Report.txt",
    "text/plain"
)