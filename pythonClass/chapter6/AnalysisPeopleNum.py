import csv
import matplotlib.pyplot as plt
import warnings

import numpy as np

warnings.filterwarnings('ignore')

plt.rc('font', family='Malgun Gothic')

f1 = open('C:\csv\LOCAL_PEOPLE_DONG_202208.csv', encoding='UTF-8')
f2 = open('C:\csv\dong_code.csv', encoding='UTF-8')
people = csv.reader(f1)
dong = csv.reader(f2)
next(people)
next(dong)
people = list(people)
dong = list(dong)

dong_code1 = 11680545
dong_code2 = 11110560

month_code = 8

month = ["0시", "1시", "2시", "3시", "4시", "5시", "6시", "7시", "8시", "9시", "10시", "11시", "12시", "13시", "14시", "15시", "16시", "17시", "18시", "19시", "20시", "21시", "22시", "23시"]

month_result1 = [0 for i in range(24)]
month_result2 = [0 for i in range(24)]

for row in people:
    if int(row[2]) == dong_code1:
        for hour in range(24):
            if int(row[1]) == hour:
                month_result1[hour] += float(row[3])
    elif int(row[2]) == dong_code2:
        for hour in range(24):
            if int(row[1]) == hour:
                month_result2[hour] += float(row[3])

# 모든값 31로 나누기

for row in month_result1:
    row = row / 31

for row in month_result1:
    print(row)

plt.title("8월의 시간대별 평균인구 그래프")

# plt.figure(figsize=(12, 5))

plt.plot(month, month_result1, label="압구정동 평균 인구")
plt.plot(month, month_result2, label="평창동 평균 인구")

plt.legend()

current_values = plt.gca().get_yticks()
plt.gca().set_yticklabels(['{:.0f}'.format(x) for x in current_values])

plt.show()