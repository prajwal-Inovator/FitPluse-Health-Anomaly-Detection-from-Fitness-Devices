import streamlit as st
import pandas as pd
import io
from preprocess import preprocess_fitpulse_pipeline

st.set_page_config(
    page_title="FitPulse Anomaly Detection",
    layout="centered"
)

st.title("🏃‍♂️ FitPulse Anomaly Detection")
st.caption("Health Data Collection & Preprocessing")

# ---------------------------
# Sidebar (RESTORED)
# ---------------------------
st.sidebar.header("⚙️ Preprocessing Options")

timestamp_col = st.sidebar.text_input(
    "Timestamp column name",
    value="timestamp"
)

timezone_from = st.sidebar.text_input(
    "Source timezone (optional)",
    placeholder="Asia/Kolkata"
)

to_utc = st.sidebar.checkbox(
    "Convert to UTC",
    value=True
)

# ---------------------------
# File Upload
# ---------------------------
uploaded = st.file_uploader(
    "Upload Fitness CSV or JSON file",
    type=["csv", "json"]
)

if uploaded:
    bytes_data = uploaded.read()
    st.success(f"Loaded file: {uploaded.name}")

    # Preview raw data
    try:
        if uploaded.name.lower().endswith(".csv"):
            raw_df = pd.read_csv(io.BytesIO(bytes_data))
        else:
            try:
                raw_df = pd.read_json(io.BytesIO(bytes_data))
            except:
                raw_df = pd.read_json(io.BytesIO(bytes_data), lines=True)

        st.subheader("📄 Raw Data Preview")
        st.dataframe(raw_df.head())

    except Exception as e:
        st.error("❌ Unable to read file")
        st.warning(str(e))
        st.stop()

    # ---------------------------
    # Run pipeline
    # ---------------------------
    if st.button("🚀 Run FitPulse Preprocessing"):
        try:
            df_processed, out_csv = preprocess_fitpulse_pipeline(
                contents=bytes_data,
                filename=uploaded.name,
                timestamp_col=timestamp_col,
                timezone_from=timezone_from or None,
                to_utc=to_utc
            )

            st.success("✅ Preprocessing completed successfully")

            st.subheader("📊 Processed Data Preview")
            st.dataframe(df_processed.head(10))

            st.download_button(
                label="⬇️ Download Cleaned CSV",
                data=out_csv,
                file_name=f"cleaned_{uploaded.name.replace('.json', '.csv')}",
                mime="text/csv"
            )

        except Exception as e:
            st.error("❌ Preprocessing failed")
            st.warning(str(e))

else:
    st.info("⬆️ Upload a CSV or JSON fitness file to begin")
