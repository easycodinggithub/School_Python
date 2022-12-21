import pandas as pd

df = pd.read_csv("countries.csv")

# print(df)
# df["density"] = df.population / df.area
# print(df.head())

df1 = pd.DataFrame({"code" : ["CA"], "country" : ["Cannada"], "area" : [9984670], "capital" : ["Ottawa"], "population" : [34300000]})
df2 = df.append(df1, ignore_index=True)

# print(df2)

# axis 1 = 열, axis 0 = 행

df2.drop(index=2, axis=0, inplace=True)
df2.drop(["capital"], axis=1, inplace=True)

print(df2)