
import os
import streamlit as st
import requests

# Page configuration
st.set_page_config(
    page_title="Financial Anomaly Detection",
    page_icon="💳",
    layout="centered"
)

# API configuration
API_BASE_URL = os.getenv(
    "API_URL",
    "http://127.0.0.1:8000"
).rstrip("/")

PREDICT_URL = (
    API_BASE_URL
    if API_BASE_URL.endswith("/predict")
    else f"{API_BASE_URL}/predict")

# Feature names
feature_names = (
    ["Time"]
    + [f"V{i}" for i in range(1, 29)]
    + ["_scaled"]
)

# Sample fraud transaction
sample_features = {
    "Time": 406,
    "V1": -2.31222654,
    "V2": 1.951992011,
    "V3": -1.60985073,
    "V4": 3.997905588,
    "V5": -0.52218786,
    "V6": -1.42654532,
    "V7": -2.53738731,
    "V8": 1.391657248,
    "V9": -2.77008928,
    "V10": -2.77227214,
    "V11": 3.202033207,
    "V12": -2.89990739,
    "V13": -0.59522188,
    "V14": -4.28925378,
    "V15": 0.38972412,
    "V16": -1.14074718,
    "V17": -2.83005567,
    "V18": -0.01682247,
    "V19": 0.416955705,
    "V20": 0.126910559,
    "V21": 0.517232371,
    "V22": -0.03504937,
    "V23": -0.46521108,
    "V24": 0.320198199,
    "V25": 0.044519167,
    "V26": 0.177839798,
    "V27": 0.261145003,
    "V28": -0.14327587,
    "_scaled": -0.307413
}

# Page heading
st.title("💳 Real-Time Financial Anomaly Detection")
st.write("Enter transaction details to detect suspicious activity.")

# Sample transaction button
if st.button("Test Sample Fraud Transaction"):
    try:
        response = requests.post(
            PREDICT_URL,
            json={"features": sample_features},
            timeout=30
        )
        response.raise_for_status()

        st.write("### Sample Prediction")
        result = response.json()

        if result["prediction"] == 1:
            st.error("🚨 Anomaly Detected!")
        else:
            st.success("✅ Normal Transaction")

        st.json(result)

    except requests.exceptions.RequestException as error:
        st.error(f"API connection failed: {error}")

# Transaction input form
with st.form("transaction_form"):
    st.subheader("Transaction Details")

    features = {}

    for name in feature_names:
        features[name] = st.number_input(
            name,
            value=0.0,
            format="%.6f"
        )

    submitted = st.form_submit_button("Check Transaction")

# Prediction
if submitted:
    try:
        response = requests.post(
            PREDICT_URL,
            json={"features": features},
            timeout=30
        )

        response.raise_for_status()
        result = response.json()

        if result["prediction"] == 1:
            st.error("🚨 Anomaly Detected!")
        else:
            st.success("✅ Normal Transaction")

        st.write("### Prediction Results")
        st.write("Prediction:", result["prediction"])
        st.write("Anomaly Score:", result["anomaly_score"])
        st.write("Threshold:", result["threshold"])

    except requests.exceptions.RequestException as error:
        st.error(f"API connection failed: {error}")
