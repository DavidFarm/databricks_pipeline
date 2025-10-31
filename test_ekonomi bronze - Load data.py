# Databricks notebook source
# MAGIC %md
# MAGIC Set enviroment

# COMMAND ----------

spark.sql("USE CATALOG workspace")
spark.sql("USE SCHEMA default")

# COMMAND ----------

# MAGIC %md
# MAGIC So, import from csv file uploaded to Databricks volume using COPY INTO. 
# MAGIC Table setup in setup notebook
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC COPY INTO test_ekonomi_bronze
# MAGIC FROM '/Volumes/workspace/default/test_ekonomi'
# MAGIC FILEFORMAT = CSV
# MAGIC FORMAT_OPTIONS ('mergeSchema' = 'true',
# MAGIC                 'delimiter' = ';',
# MAGIC                 'header' = 'true');
# MAGIC
# MAGIC SELECT * FROM test_ekonomi_bronze;

# COMMAND ----------

