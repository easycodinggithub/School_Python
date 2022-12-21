import csv
f = open('C:\csv\card.csv', encoding='UTF-8')
data = csv.reader(f)
next(data)
data = list(data)

sum = 0

for row in data:
    if row[-1] == "전표매입":
       sum += int(row[6])

print(sum)