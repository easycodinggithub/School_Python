def calculate(a, b, c):
    sum = a*b*c
    return sum
a, b, c = map(int, input().split())

countUseNum = [ 0 for i in range(10) ]

sum = calculate(a, b, c)

sumList = []

for i in str(sum):
    sumList.append(i)

print(sumList)

for i in sumList:
    countUseNum[int(i)] += 1

for i in range(10):
    print("%d : %d" %(i, countUseNum[i]))

