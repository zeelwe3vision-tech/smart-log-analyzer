from analyzer.log_parser import parse_logs
from analyzer.anomaly_detector import detect_anomalies
from analyzer.report_generator import generate_summary

log_file = "logs/sample.log"

df = parse_logs(log_file)
anomalies = detect_anomalies(df)
summary = generate_summary(df, anomalies)

print("\n===== LOG SUMMARY =====")
for key, value in summary.items():
    print(f"{key}: {value}")

print("\n===== ANOMALIES =====")
print(anomalies)