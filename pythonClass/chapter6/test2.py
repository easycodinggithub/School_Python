import csv
import matplotlib.pyplot as plt
import math as m

plt.rc('font', family='Malgun Gothic')

f = open('C:\csv\card.csv', encoding='UTF-8')
data = csv.reader(f)
next(data)
data = list(data)

month = ["10월", "11월", "12월"]

sum = [0 for i in range(10, 13)]

print(sum)

for row in data:
    if row[-1] == "전표매입":
       for mon in range(10, 13):
           if int(row[0].split('-')[1]) == mon:
               sum[mon-10] += int(row[6])

# for row in data:
#     print(row)

print(sum)

plt.figure(figsize=(10, 5))

plt.bar(month, sum, label="단위:금액")

plt.legend()

plt.xlabel("월")

plt.ylabel("매출")

plt.title("월별 이용금액의 합")

# current_values = plt.gca().get_yticks()
# plt.gca().set_yticklabels(['{:,.0f}'.format(x) for x in current_values])

plt.show()