def findSquare(n):
    for j in range(1, 10):
        if n == j*j:
            return 1
    return 0

numbers = list(map(int, input().split()))

sum = 0

for i in numbers:
    if i <= 0 or i >= 100:
        break
    sum += findSquare(i)
print(sum)