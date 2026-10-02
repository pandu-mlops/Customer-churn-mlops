import pandas as pd

df = pd.read_csv("data/churn.csv")

print("Number of rows:", len(df))
print("Number of columns:", len(df))

print("\nColumn names:")
print(df.columns.tolist())

print("\nFirst 5 rows:")
print(df.head())
print("\nChurn distribution:")
print(df["Churn"].value_counts())