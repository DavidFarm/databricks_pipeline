# Databricks Medallion Pipeline (Bronze–Silver–Gold)

This project demonstrates a full ELT workflow in Databricks Free Edition.

## 🧱 Architecture
- **Bronze:** Ingests CSV files using `COPY INTO`.
- **Silver:** Cleans data and enforces correct datatypes.
- **Gold:** Aggregates and outputs analytics-ready data for BI use.
- **Job Orchestration:** A Databricks Job runs all three notebooks in sequence, no manual input required.

## ⚙️ Tools & Technologies
Databricks | Apache Spark | Delta Tables | SQL | Python

