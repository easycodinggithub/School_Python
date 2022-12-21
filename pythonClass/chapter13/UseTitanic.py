import pandas as pd
df = pd.read_csv("titanic.csv")
# print(df.head())
# print(df.Age)
# print(df["Age"])

# print(df.Name[max(df.Age)])
#
# # print(df.Name[df.Survived == 1 & min(int(df.Age))])
#
# print(df.describe())
# print(df.dtypes)

# dfi = pd.read_csv("titanic.csv", index_col=0) # PassengerId 를 index 로 정함

dfi = pd.read_csv("titanic.csv", index_col=0) # Name 을 index 로 정함

# print(df["Name"], df["Age"], df["Gender"])

print(df[(df.Gender == "female") & (df.Survived > 0) | (df.SibSp > 0) ].loc[:, ["Name", "Age", "Gender"]])

# print(dfi)

# dfi.to_excel("titanic.xlsx", sheet_name="passengerID")