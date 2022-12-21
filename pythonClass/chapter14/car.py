import pandas as pd

cars = pd.read_csv("used_cars.csv")

wage = pd.read_csv("minimum_wage.csv")

# print(used_cars.dtypes)

# print(used_cars.head())

used_cars_pivoting_price = cars.pivot_table(
    values="Price",
    index="Fuel",
    aggfunc="sum",
    fill_value=0
)

used_cars_pivoting_carCount = cars.pivot_table(
    values="Price",
    index="Manufacturer",
    columns="Transmission",
    aggfunc="count",
    margins=True
)

used_cars_pivoting_meanPrice = cars.pivot_table(
    values="Price",
    index=["Year", "Fuel"],
    columns=["Transmission"],
    aggfunc="mean"
)

year_columns = [
    "2010", "2011", "2012", "2013",
    "2014", "2015", "2016", "2017"
]

wagemelt1 = wage.melt(id_vars = "State", value_vars = year_columns)

wagemelt2 = wage.melt(
    id_vars = "State", var_name = "Year", value_name = "Wage"
)

print(used_cars_pivoting_price.head())
print(used_cars_pivoting_carCount.tail())
print(used_cars_pivoting_meanPrice.head())
print(used_cars_pivoting_meanPrice.stack())
print(wagemelt1.head())
print(wagemelt2.head())