def send_alert(anomalies):
    if len(anomalies) > 0:
        print("⚠️ ALERT: Anomalies detected!")
        print(anomalies[['timestamp', 'level', 'message']])