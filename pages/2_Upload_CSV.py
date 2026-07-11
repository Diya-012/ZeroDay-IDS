import streamlit as st
import pandas as pd
import numpy as np
import tensorflow as tf
import joblib

# ================================
# Load AI Model
# ================================

model = tf.keras.models.load_model(
    "Autoencoder-ZeroDay-IDS/results/autoencoder_model.keras"
)

scaler = joblib.load(
    "Autoencoder-ZeroDay-IDS/scaler/standard_scaler.pkl"
)

threshold = joblib.load(
    "Autoencoder-ZeroDay-IDS/results/best_threshold.pkl"
)

st.title("📁 Upload CSV")

uploaded_file = st.file_uploader(
    "Upload Network Traffic CSV",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.success("✅ File uploaded successfully!")

    # ================================
    # Dataset Information
    # ================================

    st.subheader("📊 Dataset Information")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Rows", df.shape[0])

    with col2:
        st.metric("Columns", df.shape[1])

    st.subheader("📋 Column Names")
    st.write(list(df.columns))

    st.subheader("👀 Preview")
    st.dataframe(df.head())

    # ================================
    # AI Prediction Button
    # ================================

    if st.button("🚀 Run AI Detection"):

        try:

            # Scale data
            X_scaled = scaler.transform(df)

            # Autoencoder prediction
            reconstructed = model.predict(X_scaled)

            # Reconstruction Error
            mse = np.mean(np.square(X_scaled - reconstructed), axis=1)

            predictions = mse > threshold

            results = df.copy()

            results["Reconstruction Error"] = mse

            results["Prediction"] = np.where(
                predictions,
                "🚨 Attack",
                "✅ Normal"
            )

            st.session_state["results"] = results
            st.session_state["uploaded"] = True
            st.session_state["threshold"] = threshold

            st.success("Detection Completed!")

            st.subheader("Detection Results")

            st.dataframe(results)

            st.download_button(
                "📥 Download Results",
                results.to_csv(index=False),
                "detection_results.csv",
                "text/csv"
            )

        except Exception as e:

            st.error(f"Error: {e}")

else:
    st.info("Please upload a CSV file.")