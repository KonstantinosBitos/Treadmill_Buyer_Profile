import pandas as pd
from sqlalchemy import create_engine

# Load CSV
#df = pd.read_csv("C:/Users/bitos/OneDrive/Desktop/Treadmill Project/aerofit_treadmill_data.csv")

# Create SQLite database in a local file
engine = create_engine("sqlite:///aerofit.db")

# Load data into SQL table
#df.to_sql("aerofit", engine, index=False, if_exists="replace")

#print("✅ CSV loaded successfully into SQLite database aerofit.db")

query = "SELECT Product, MaritalStatus, COUNT(*) AS Count,ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (PARTITION BY Product), 1) AS Percent FROM aerofit GROUP BY Product, MaritalStatus;"
result = pd.read_sql(query, engine)
print(result)
