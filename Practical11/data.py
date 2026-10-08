import pandas as pd

data = {
    "Name": ["Chaitanya", "Rahul", "Amit"],
    "Age": [20, 21, 19],
    "Marks": [85, 78, 92]
}

df = pd.DataFrame(data)

print(df)

print(df["Name"])

print(df.iloc[0])

print(df.shape)

print(df.columns)

print(df.dtypes)

print(df[df["Marks"] > 80])

df["Grade"] = ["A", "B", "A"]

print(df)
