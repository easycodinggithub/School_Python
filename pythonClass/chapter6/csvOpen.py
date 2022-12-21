import csv
f = open('C:\csv\card.csv', encoding='UTF-8')
data = csv.reader(f)
next(data)
data = list(data)

# print(data)

# for i in data:
#     print(i, end="\n")

# for row in data:
#     print(row[0])

# for row in data:
#     print(row[-3])

# for row in data:
#     print(row[5], '에서', row[6], '원 사용')
#
# for row in data:
#     store = row[5]
#     payment = row[6]
#     print(store, '에서', payment, '원 사용')
#
# print(len(data))