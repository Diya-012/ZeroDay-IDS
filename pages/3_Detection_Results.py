import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🛡️ AI Detection Dashboard")

# -----------------------------
# Check Results
# -----------------------------

if "results" not in st.session_state:
    st.warning("⚠️ Please upload a dataset and run AI Detection first.")
    st.stop()

results = st.session_state["results"]

# -----------------------------
# Statistics
# -----------------------------

total = len(results)

attacks = (results["Prediction"] == "🚨 Attack").sum()

normal = (results["Prediction"] == "✅ Normal").sum()

attack_rate = attacks / total * 100

# -----------------------------
# Dashboard Cards
# -----------------------------

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "📂 Total Records",
    f"{total:,}"
)

col2.metric(
    "🟢 Normal",
    f"{normal:,}"
)

col3.metric(
    "🚨 Attacks",
    f"{attacks:,}"
)

col4.metric(
    "📊 Attack Rate",
    f"{attack_rate:.2f}%"
)

st.divider()

# -----------------------------
# Charts
# -----------------------------

left, right = st.columns(2)

with left:

    pie = px.pie(
        names=["Normal", "Attack"],
        values=[normal, attacks],
        title="Attack Distribution",
        hole=0.45
    )

    st.plotly_chart(
        pie,
        use_container_width=True
    )

with right:

    bar = px.bar(
        x=["Normal", "Attack"],
        y=[normal, attacks],
        color=["Normal", "Attack"],
        title="Network Traffic Summary"
    )

    st.plotly_chart(
        bar,
        use_container_width=True
    )

st.divider()

# -----------------------------
# Reconstruction Error
# -----------------------------

st.subheader("📈 Reconstruction Error")

line = px.line(
    results.reset_index(),
    x="index",
    y="Reconstruction Error",
    title="Reconstruction Error per Record"
)

st.plotly_chart(
    line,
    use_container_width=True
)

st.divider()

# -----------------------------
# Highest Risk Records
# -----------------------------

st.subheader("🚨 Top 10 Highest Risk Records")

top10 = results.sort_values(
    by="Reconstruction Error",
    ascending=False
).head(10)

st.dataframe(
    top10,
    use_container_width=True
)

st.divider()

# -----------------------------
# Search
# -----------------------------

st.subheader("🔍 Search Results")

search = st.text_input("Search any value")

if search:

    filtered = results[
        results.astype(str)
        .apply(
            lambda x: x.str.contains(
                search,
                case=False
            )
        )
        .any(axis=1)
    ]

    st.dataframe(
        filtered,
        use_container_width=True
    )

else:

    st.dataframe(
        results,
        use_container_width=True
    )

st.divider()

# -----------------------------
# Download
# -----------------------------

st.download_button(
    "📥 Download Detection Results",
    results.to_csv(index=False),
    "Detection_Results.csv",
    "text/csv"
)