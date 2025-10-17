import pandas as pd

#Load the file
df = pd.read_csv("aerofit_treadmill_data.csv")

# Average profile per product
profile = df.groupby('Product').agg({
    'Age': 'mean',
    'Education': 'mean',
    'Usage': 'mean',
    'Fitness': 'mean',
    'Income': 'mean',
    'Miles': 'mean'
    
}).round(2)

print(profile)

# Mean profile per product
profile2 = df.groupby('Product').agg({
    'Age': 'median',
    'Education': 'median',
    'Usage': 'median',
    'Fitness': 'median',
    'Income': 'median',
    'Miles': 'median'
    
}).round(2)

print(profile2)
