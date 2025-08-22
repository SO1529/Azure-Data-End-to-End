import pandas as pd
df = pd.read_csv("SalesData.csv") 
df = df.drop_duplicates()
df = df.dropna()