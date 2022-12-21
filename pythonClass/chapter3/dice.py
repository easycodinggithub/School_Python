import random

# for i in range(1, 6):
#     for j in range(1, 6):
#         if (i+j) == 6:
#             print("첫 번째 주사위=%d 두 번째 주사위=%d" %(i, j))

while True:
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    print(dice1, dice2)
    if (dice1 + dice2) == 6:
        print("첫 번째 주사위=%d 두 번째 주사위=%d" % (dice1, dice2))
    else:
        print("합이 6이 아닙니다.")
        break