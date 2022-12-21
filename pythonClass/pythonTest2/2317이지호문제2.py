import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_excel("raw_data.xlsx")

# 문제 2

print(data.birth.dtype)
print(data.birth.mean())

# 빈 값 확인

print(data.birth.isnull().sum())

# max min 으로 범위 확인

print(data.birth.max())

print(data.birth.min())

# 빈값이 없고 max 가 2, min 이 1임으로 결측값이 없다.

data4 = data[(data['birth'] >= 1900) & (data['birth'] <= 2014)]

print(data4)

plt.hist(data.birth)

plt.show()

data["age"] = 2019 - data["birth"]

print(data["age"].head())