def search_logs(df, keyword):
    return df[df['message'].str.contains(keyword, case=False, na=False)]