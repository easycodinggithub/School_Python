import random as r

count = 1
user = []
lotto = list(range(1, 46))
r.shuffle(lotto)
numbers = lotto[0:7]

def checkLotto():
    result = 0
    bonusResult = 0
    for i in range(0, 6):
        for j in range(0, 7):
            if user[i] == numbers[j]:
                if j == 6:
                    bonusResult += 1
                else:
                    result += 1
    return result, bonusResult

while True:
    if len(user) >= 6:
        break
    userNum = int(input("%d번째 로또 번호 입력 : " % count))
    user.append(userNum)
    count += 1

print("당첨번호 : %s + %s" % (lotto[0:6], lotto[6]))
print("사용자 선택번호 : %s" % user)

result, bonusResult = checkLotto()

print("맞은 개수 : %d, 보너스 맞은 개수 : %d" % (result, bonusResult))

if result >= 6:
    print("1등")
elif result >= 5 and bonusResult >= 1:
    print("2등")
elif result >= 5:
    print("3등")
elif result >= 4:
    print("4등")
elif result >= 3:
    print("5등")
else:
    print("꽝")