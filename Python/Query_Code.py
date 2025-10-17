import pandas as pd
from sqlalchemy import create_engine

# Load CSV
df = pd.read_csv("aerofit_treadmill_data.csv")

# Create engine
engine = create_engine("sqlite:///aerofit.db")

# Create a query
query = "SELECT Product, MaritalStatus, COUNT(*) AS Count,ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (PARTITION BY Product), 1) AS Percent FROM aerofit GROUP BY Product, MaritalStatus;"

# Print the result
result = pd.read_sql(query, engine)
print(result)