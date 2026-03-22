import streamlit as st
from log_parser import parse_logs
from anomaly_detector import detect_anomalies

st.set_page_config(layout="wide")

st.title("📊 Smart Log Analyzer Dashboard")

df = parse_logs("../logs/sample.log")
anomalies = detect_anomalies(df)

st.subheader("All Logs")
st.dataframe(df)

st.subheader("Anomalies")
st.dataframe(anomalies)

st.subheader("Response Time Distribution")
st.line_chart(df['response_time'])