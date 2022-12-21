maxNumber = int(input("찾을 소수의 갯수를 입력하세요 : "))

def findPrimayNumber(number):
    for i in range(2, number):
        if (number % i) == 0:
            return False
    return True

# for i in range(2, 100):
#     if findPrimayNumber(i):
#         print(i)

i = 2
countNumber = 0

while True:
    if countNumber >= maxNumber:
        break
    else:
        if findPrimayNumber(i):
            print(i)
            countNumber += 1
    i += 1

