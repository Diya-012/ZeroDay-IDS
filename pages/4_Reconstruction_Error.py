import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📈 Reconstruction Error Analysis")

# Check whether prediction has been performed
if "results" not in st.session_state:

    st.warning("⚠️ Please upload a dataset and run AI Detection first.")
    st.stop()

results = st.session_state["results"]
threshold = st.session_state["threshold"]

st.success("✅ Reconstruction errors loaded successfully.")

# ==========================
# Summary
# ==========================

avg_error = results["Reconstruction Error"].mean()
max_error = results["Reconstruction Error"].max()
min_error = results["Reconstruction Error"].min()

col1, col2, col3 = st.columns(3)

col1.metric("Average Error", f"{avg_error:.6f}")
col2.metric("Maximum Error", f"{max_error:.6f}")
col3.metric("Threshold", f"{threshold:.6f}")

st.divider()

# ==========================
# Line Chart
# ==========================

chart_df = results.reset_index()

fig = px.line(
    chart_df,
    x="index",
    y="Reconstruction Error",
    title="Reconstruction Error for Each Network Record"
)

fig.add_hline(
    y=threshold,
    line_dash="dash",
    line_color="red",
    annotation_text="Threshold"
)

st.plotly_chart(fig, use_container_width=True)

# ==========================
# Histogram
# ==========================

st.subheader("📊 Error Distribution")

hist = px.histogram(
    results,
    x="Reconstruction Error",
    nbins=50,
    title="Distribution of Reconstruction Errors"
)

hist.add_vline(
    x=threshold,
    line_color="red",
    line_dash="dash"
)

st.plotly_chart(hist, use_container_width=True)

# ==========================
# Highest Errors
# ==========================

st.subheader("🚨 Highest Reconstruction Errors")

top10 = results.sort_values(
    by="Reconstruction Error",
    ascending=False
).head(10)

st.dataframe(top10, use_container_width=True)