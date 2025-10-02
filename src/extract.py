import pandas as pd

def extract_data(file_path: str) -> pd.DataFrame:
    print(f" Extracting data from {file_path}")
    return pd.read_csv(file_path)
