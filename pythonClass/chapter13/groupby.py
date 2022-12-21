import pandas as pd

df = pd.read_csv("titanic.csv")

# print(df["Age"].mean())
# print(df[["Age", "Fare"]].median())
# print(df[["Gender", "Age"]].groupby("Gender").mean())
# print(df.groupby("Gender").mean())

# print(df.groupby(["Gender", "Pclass"])["Fare"].mean())
# print(df.groupby(["Pclass", "Gender"])["Fare"].mean())

print(df["Pclass"].value_counts())