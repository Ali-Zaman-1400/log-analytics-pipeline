import sqlite3

def save_to_csv(df, path):
    df.to_csv(path, index=False)
    print(f" Saved CSV: {path}")

def save_to_sqlite(df, db_path, table_name):
    conn = sqlite3.connect(db_path)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()
    print(f" Saved table '{table_name}' to {db_path}")
