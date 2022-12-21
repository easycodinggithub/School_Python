import pandas as pd

nfl = pd.read_csv("nfl.csv", parse_dates = ["Birthday"])

nfl = nfl.set_index("Name")

# nfl = pd.read_csv("nfl.csv", index_col = "Name", parse_dates = ["Birthday"])

# print(nfl.head())

print(nfl.Team.value_counts().head())

# print(nfl["Team"].value_counts().head())

print(nfl.sort_values("Salary", ascending = False).head())

print(nfl.sort_values(
    by = ["Team", "Salary"],
    ascending = [True, False]
))

nfl = nfl.reset_index().set_index(keys = "Team")
print(nfl.head(3))

print(nfl.loc["New York Jets"].head())

print(nfl.loc["New York Jets"].sort_values("Birthday").head(1))
