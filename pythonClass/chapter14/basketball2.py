import pandas as pd
nba = pd.read_csv(
    "nba.csv", parse_dates = ["Birthday"], index_col = "Name"
)

# nba = nba.set_index(keys = "Name")

# print(nba.Salary)

# print(nba.loc["LeBron James"])

# print(nba.loc[["Kawhi Leonard", "Paul George"]])

# print(nba.sort_index().loc["Otto Porter":"Patrick Beverley"])

# print(nba.sort_values(by="Salary", ascending=False).head())
#
# # loc : 양쪽 끝 값을 포함
#
# print(nba.sort_index().loc["Zach Collins":])
#
# print(nba.sort_index().loc[:"Al Horford"])
#
# print(nba.iloc[300])
#
# print(nba.iloc[[100, 200, 300, 400]])
#
# # iloc : 마지막 값을 포함 안함
#
# print(nba.iloc[400:404])
#
# print(nba.iloc[:2])
#
# print(nba.iloc[447:])
#
# print(nba.iloc[-10:-6])
#
# print(nba.iloc[0:10:2])

# print(nba.loc["Giannis Antetokounmpo", "Team"])
#
# print(nba.loc["James Harden", ["Position", "Birthday"]])
#
# print(nba.loc[
#     ["Russell Westbrook", "Anthony Davis"],
#     ["Team", "Salary"]
# ])

# print(nba.loc["Joel Embiid", "Position":"Salary"])

# print(nba.loc["Joel Embiid", "Salary":"Position"])

# print(nba.iloc[57, 3])

# print(nba.iloc[100:104, :3])

nba.columns = ["Team", "Position", "Date of Birth", "Pay"]

print(nba.head(1))

print(nba.rename(columns = { "Date of Birth": "Birthday" }))