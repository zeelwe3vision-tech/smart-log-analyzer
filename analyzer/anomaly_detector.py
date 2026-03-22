from sklearn.ensemble import IsolationForest

def detect_anomalies(df):
    if df.empty:
        return df

    # Simple anomaly detection based on log levels
    error_count = len(df[df['level'] == 'ERROR'])
    warning_count = len(df[df['level'] == 'WARNING'])
    
    # Mark logs with ERROR or WARNING levels as anomalies
    df['anomaly'] = df['level'].apply(lambda x: -1 if x in ['ERROR', 'WARNING'] else 1)
    
    anomalies = df[df['anomaly'] == -1]
    return anomalies