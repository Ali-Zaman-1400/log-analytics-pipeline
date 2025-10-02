# Log Analytics Pipeline

This repository contains a professional **ETL pipeline** for log data.  
It extracts raw logs, transforms and cleans them, analyzes trends, and loads the results into CSV and SQLite.

---

##  Features
- Extract raw logs from CSV
- Transform data: clean missing values, normalize text, convert timestamps
- Analyze logs: daily counts, error levels, top messages
- Load results into CSV and SQLite database
- Central logging with `logs/pipeline.log`

---

##  Project Structure
```
log-analytics-pipeline/
├── data/
│   ├── raw/                # raw input logs
│   ├── processed/          # cleaned data
│   └── analytics/          # final reports
├── logs/                   # execution logs
├── src/                    # ETL scripts
│   ├── extract.py
│   ├── transform.py
│   ├── analyze.py
│   ├── load.py
│   └── main.py
├── notebooks/              # Jupyter notebooks for EDA
├── requirements.txt
└── README.md
```

---

##  Usage
1. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
2. Place your raw logs in `data/raw/logs.csv`. Example provided in this repo.
3. Run the pipeline:
   ```bash
   python src/main.py
   ```
4. Results will be available in:
   - `data/processed/clean_logs.csv`
   - `data/analytics/*.csv`
   - `data/analytics/logs.db`

---

##  Example Report
| date       | total_logs |
|------------|------------|
| 2025-10-01 | 5          |
| 2025-10-02 | 3          |

---

##  Author
Ali Zamanpour
  
*Data Engineer & AI Specialist*  

---
