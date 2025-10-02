import pandas as pd

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    print(" Transforming data...")

    df = df.dropna(subset=["timestamp", "level", "message"])
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
    df = df.dropna(subset=["timestamp"])
    df["date"] = df["timestamp"].dt.date
    df["hour"] = df["timestamp"].dt.hour
    df["message"] = df["message"].str.lower()

    return df
