import pandas as pd

sales = pd.read_csv("sales_by_employee.csv", parse_dates=["Date"])

# print(sales.tail())

# print(sales.pivot_table(index = "Date"))

# print(sales.pivot_table(index = "Date", aggfunc="mean"))

# print(sales.pivot_table(index = "Date", aggfunc="sum"))

# sp = sales.pivot_table(
#     index= "Date",
#     columns= "Name",
#     values= "Revenue",
#     aggfunc= "sum"
# )

sp1 = sales.pivot_table(
    index= "Date",
    columns= "Name",
    values= "Revenue",
    aggfunc= "sum",
    fill_value=0,
    margins= True,
    margins_name= "Total"
)

sp2 = sales.pivot_table(
    index = "Date",
    columns = "Name",
    values = "Revenue",
    aggfunc = "count",
    fill_value=0
)

sp3 = sales.pivot_table(
    index = "Date",
    columns = "Name",
    values = "Revenue",
    aggfunc = ["sum", "count"],
    fill_value = 0
)

sp4 = sales.pivot_table(
    index = "Date",
    columns = "Name",
    values = ["Revenue", "Expenses"],
    fill_value = 0,
    aggfunc = { "Revenue": "min", "Expenses": "min" }
)

sp5 = sales.pivot_table(
    index = ["Name", "Date"], values = "Revenue", aggfunc = "sum"
).head(10)

sp6 = sales.pivot_table(
    index = ["Date", "Name"], values = "Revenue", aggfunc = "sum"
).head(10)

print(sp5)
print(sp6)