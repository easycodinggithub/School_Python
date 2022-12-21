import pandas as pd

video_game_sales = pd.read_csv("video_game_sales.csv")

# print(video_game_sales.head())
#
# print(video_game_sales.melt(id_vars="Name", value_vars="NA").head())

regional_sales_columns = ["NA", "EU", "JP", "Other"]

vgs1 = video_game_sales.melt(
    id_vars = "Name", value_vars = regional_sales_columns
)

video_game_sales_by_region = video_game_sales.melt(
    id_vars = "Name",
    value_vars = regional_sales_columns,
    var_name = "Region",
    value_name = "Sales"
)

v1 = video_game_sales_by_region.pivot_table(
    index = "Name", values = "Sales", aggfunc = "sum"
).head()

print(v1)