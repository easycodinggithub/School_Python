# • week_1_sales.csv, week_2_sales.csv, customers.csv, food.csv 를 이용하여 아래의 문제를 풀어보세요. (join, merge 등)

# 1. 2주간의 판매 데이터를 하나의 Dataframe으로 결합하세요. week1 Dataframe에 ‘week 1’이라는 키를 할당하고 week2 Dataframe에 ‘week 2’라는 키를 할당하세요.
# 2. 2주 동안 매주 식당에서 식사한 고객을 찾으세요.
# 3. 2주 동안 매주 식당에서 식사를 하고 같은 음식을 주문한 고객을 찾으세요.
# 4. 1주차에만 방문한 고객과 2주차에만 방문한 고객이 누구인지 찾으세요.
# 5. week1 Dataframe의 각 행은 음식을 주문한 고객을 나타냅니다. 각 행에 대한 고객의 정보를 customers Dataframe에서 가져오세요.

import pandas as pd

w1 = pd.read_csv("week_1_sales.csv")
w2 = pd.read_csv("week_2_sales.csv")
f = pd.read_csv("foods.csv")
c = pd.read_csv("customers.csv")

# 문제 1번

w = pd.concat(objs = [w1, w2], keys = ["week 1", "week 2"])

# 문제 2번

# 2주 동안 매주 식당에서 식사를 했음으로 w1 과 w2 를 inner join 하면 됨.

innerJoin1 = w1.merge(w2, how = "inner", on = "Customer ID")

print(innerJoin1)

innerJoin2 = innerJoin1.merge(c, how= "left", left_on="Customer ID", right_on="ID")

print(innerJoin2.loc[:,["First Name", "Last Name"]])

# 문제 3번

# 2주동안 매주 식당에서 식사를 하고 같은 음식을 주문했음으로 w1 과 w2를 inner join 하는데 on 을 Customer ID, Food ID 로 주어 해결함.

id = ["Customer ID", "Food ID"]

# 고객 번호로 보기

innerJoin3 = w1.merge(w2, how = "inner", on = id)

print(innerJoin3)

# 고객 이름으로 보기

innerJoin4 = innerJoin3.merge(c, how= "left", left_on="Customer ID", right_on="ID")

print(innerJoin4)

# 문제 4번

# 1주차, 2주차 에만 방문한 고객 찾기 => outer join 이용

innerJoin5 = w1.merge(w2, how = "outer", on = "Customer ID",indicator = True)

print(innerJoin5)

# 문제 5번

innerJoin6 = w1.merge(c, how = "left", left_on = "Customer ID", right_on = "ID")

print(innerJoin6)