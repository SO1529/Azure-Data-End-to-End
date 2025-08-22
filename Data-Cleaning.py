import pandas as pd
df = pd.read_csv("data.csv") 
df = df.drop_duplicates()
df = df.dropna()