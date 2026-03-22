from analyzer.log_parser import parse_logs
from analyzer.anomaly_detector import detect_anomalies
from alert_manager import send_alert
from search_engine import search_logs

LOG_FILE = "logs/sample.log"

def run_pipeline():
    print("📊 Parsing logs...")
    df = parse_logs(LOG_FILE)

    print("🔍 Detecting anomalies...")
    anomalies = detect_anomalies(df)

    print("🚨 Sending alerts...")
    send_alert(anomalies)

    print("🔎 Searching ERROR logs...")
    errors = search_logs(df, "error")

    print("\n=== SUMMARY ===")
    print(f"Total Logs: {len(df)}")
    print(f"Anomalies: {len(anomalies)}")
    print(f"Errors: {len(errors)}")

if __name__ == "__main__":
    run_pipeline()