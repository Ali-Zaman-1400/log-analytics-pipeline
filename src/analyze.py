import pandas as pd

def analyze_logs(df: pd.DataFrame):
    print(" Analyzing logs...")

    daily_counts = df.groupby("date").size().reset_index(name="total_logs")
    level_counts = df["level"].value_counts().reset_index()
    level_counts.columns = ["level", "count"]
    top_messages = df["message"].value_counts().head(5).reset_index()
    top_messages.columns = ["message", "count"]

    return {"daily": daily_counts, "levels": level_counts, "top_messages": top_messages}
