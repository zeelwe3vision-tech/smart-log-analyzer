from fastapi import FastAPI
from analyzer.log_parser import parse_logs
from analyzer.anomaly_detector import detect_anomalies

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Smart Log Analyzer API Running"}

@app.get("/analyze")
def analyze_logs():
    df = parse_logs("logs/sample.log")
    anomalies = detect_anomalies(df)

    return {
        "total_logs": len(df),
        "anomalies": len(anomalies)
    }