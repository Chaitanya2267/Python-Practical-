import pandas as pd

df = pd.read_csv("students.csv")

print(df)

print(df.head())

print(df.shape)

print(df.columns)

print(df.info())

print(df["Name"])

print(df[["Name", "Marks"]])

print(df[df["Marks"] > 80])
