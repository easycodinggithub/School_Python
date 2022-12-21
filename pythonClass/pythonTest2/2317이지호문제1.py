import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_excel("raw_data.xlsx")

# 문제 1

# 조건 1

# 1

print(data.gender.dtypes)

# 2

# 빈 값 확인

print(data.gender.isnull().sum())

# max min 으로 범위 확인

print(data.gender.max())

print(data.gender.min())

# 빈값이 없고 max 가 2, min 이 1임으로 결측값이 없다.

# 3

# data.astype("string")

data2 = pd.DataFrame(data.gender)
data2["gender"].loc[data2["gender"] == 1] = "male"
data2["gender"].loc[data2["gender"] == 2] = "female"
print(data2)

# 4

male = data2[data2["gender"] == "male"].count()
female = data2[data2["gender"] == "female"].count()
print(male)
print(female)

# plt.bar("남자", male)
# plt.bar("여자", female)

# plt.show()

# 조건 2

print(data.income.dtype)

print(data.income.mean())

m = data.income.median()

data3 = data.income.fillna(m)

print(data3)

plt.hist(data3.income())

plt.show()

