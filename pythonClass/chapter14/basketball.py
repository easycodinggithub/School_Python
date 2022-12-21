import pandas as pd

# pd.read_csv("nba.csv")

# pd.read_csv("nba.csv", parse_dates= ["Birthday"])

nba = pd.read_csv("nba.csv", parse_dates=["Birthday"])

# print(nba.dtypes)
#
# print(nba.count().sum())
#
# print(nba.nlargest(n = 4, columns="Salary"))
#
# print(nba.nsmallest(n = 3, columns=["Birthday"]))
#
# # print(nba.nsmallest(n = 3, columns="Birthday"))
#
# print(nba.sum(numeric_only=True))

# print(nba.sort_values(by=["Team", "Salary"], ascending=[True, False]))

# print(nba.head())

# print(nba.sort_index().head())

# print(nba.sort_index(ascending=True).head())

# print(nba.sort_index(ascending=False).head())

# print(nba.sort_index(axis="columns").head())

# print(nba.set_index("Name"))

print(nba.Salary)