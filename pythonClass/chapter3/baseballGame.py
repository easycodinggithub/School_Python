import random as r

s = 0
b = 0

def check():
    s = 0
    b = 0
    for j in range(0, 3):
        for i in range(0, 3):
            if user[j] == computer[i] and j == i:
                s += 1
            elif user[j] == computer[i]:
                b += 1
    return s, b

numbers = list(range(1, 10))
r.shuffle(numbers)
computer = numbers[0:3]

while True:
    user = list(map(int, input().split()))
    s, b = check()
    print("%ds %db" % (s, b))
    if s >= 3:
        print("정답")
        break