import csv
import matplotlib.pyplot as plt

plt.rc('font', family='Malgun Gothic')

f = open('C:\csv\card.csv', encoding='UTF-8')
data = csv.reader(f)
next(data)
data = list(data)

month = ["10월", "11월", "12월"]

taxi = [0, 0, 0]

deli = [0, 0, 0]

# print(sum)

for row in data:
    if row[-1] == "전표매입":
        if "택시" in row[5]:
            for mon in range(10, 13):
                if int((row[0].split('-'))[1]) == mon:
                    taxi[mon - 10] += int(row[6])
        elif "우아한형제들" in row[5]:
            for mon in range(10, 13):
                if int((row[0].split('-'))[1]) == mon:
                    deli[mon - 10] += int(row[6])

for row in data:
    print(row)

print(sum)

plt.title("10-12 월 택시/배달음식 지출액")

plt.figure(figsize=(10, 5))

# current_values = plt.gca().get_yticks()
# plt.gca().set_yticklabels(['{:,.0f}'.format(x) for x in current_values])

plt.plot(month, taxi, label="택시 지출액")
plt.plot(month, deli, label="배달음식 지출액")

plt.legend()

plt.show()
