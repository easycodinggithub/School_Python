import csv
import operator
import warnings

import matplotlib.pyplot as plt

plt.rc('font', family='Malgun Gothic')

f = open('C:\csv\card.csv', encoding='UTF-8')
data = csv.reader(f)
next(data)
data = list(data)

sum = {}

for row in data:
    if row[-1] == "전표매입":
        sum[row[5]] = 0

for row in data:
    if row[-1] == "전표매입":
        sum[row[5]] += int(row[6])

# for k, v in sum.items():
#     print(k, v)

top = sorted(sum.items(), key=lambda x: x[1], reverse=True)[:10]

topKey = []

topValue = []

for i in top:
    # print(i[0])
    # print(i[1])
    topKey.append(i[0])
    topValue.append(i[1])

# print(topKey)
# print(topValue)

plt.figure(figsize=(500, 5))
# plt.rcParams["figure.figsize"] = (50,3)

plt.title("가뱅점별 지출액 상위 10개 가맹점")

plt.bar(topKey, topValue, label="가뱅점별 지출액")

plt.legend()

current_values = plt.gca().get_yticks()
plt.gca().set_yticklabels(['{:.0f}'.format(x) for x in current_values])

plt.show()