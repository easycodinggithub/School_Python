import pandas as pd

groups1 = pd.read_csv("groups1.csv")
groups2 = pd.read_csv("groups2.csv")
categories = pd.read_csv("categories.csv")
cities = pd.read_csv("cities.csv", dtype= {"zip" : "string"})

# groups = pd.concat(objs=[groups1, groups2])

# 새 인덱스 만들기

groups = pd.concat(objs=[groups1, groups2], ignore_index=True)

# groups = pd.concat(objs = [groups1, groups2], keys = ["G1", "G2"])

leftJoin = groups.merge(categories, how = "left", on = "category_id")

innerJoin = groups.merge(categories, how = "inner", on = "category_id")

outerJoin = groups.merge(cities, how = "outer", left_on = "city_id", right_on = "id")

outerJoin = groups.merge(cities, how = "outer", left_on = "city_id", right_on = "id", indicator=True)

inRightOnly = outerJoin["_merge"] == "right_only"

# print(groups)
print(leftJoin.head())
print(innerJoin.head())
print(outerJoin)

print(groups[groups["category_id"] == 14])

print(outerJoin[inRightOnly].head())

print(groups[groups.city_id == 16330])