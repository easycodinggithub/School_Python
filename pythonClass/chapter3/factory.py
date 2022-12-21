number = int(input("정수를 입력하시오: "))
result = 1
for i in range(1, number+1):
    result *= i
print("%d!은 %d이다." % (number, result))