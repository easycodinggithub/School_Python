def calculate(a, b, c):
    sum = a * b * c
    return sum

a, b, c = map(int, input().split())

sum = calculate(a, b, c)

countNum = {}

for i in range(10):
    countNum[str(i)] = 0

sumList = list(str(sum))

for i in sumList:
    countNum[i] += 1

for k, v in countNum.items():
    print("%s : %s" %(k, v))