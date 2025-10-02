import logging
import os
from src.extract import extract_data
from src.transform import transform_data
from src.analyze import analyze_logs
from src.load import save_to_csv, save_to_sqlite

# Setup logging
os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def run_pipeline():
    logging.info(" Starting Log Analytics Pipeline...")

    try:
        df = extract_data("data/raw/logs.csv")
        logging.info(f"Extracted {len(df)} records.")

        df_clean = transform_data(df)
        logging.info(f"After transform: {len(df_clean)} records remain.")

        reports = analyze_logs(df_clean)
        logging.info("Analysis reports generated.")

        save_to_csv(df_clean, "data/processed/clean_logs.csv")
        save_to_sqlite(df_clean, "data/analytics/logs.db", "logs")

        for name, rep in reports.items():
            save_to_csv(rep, f"data/analytics/{name}_report.csv")

        logging.info(" Pipeline finished successfully!")
        print(" Pipeline finished successfully!")

    except Exception as e:
        logging.error(f" Pipeline failed: {e}")
        print(f" Pipeline failed: {e}")

if __name__ == "__main__":
    run_pipeline()
