def bmi(h, w):
    h /= 100
    return w / (h**2)

h, w = map(int, input("키와 몸무게를 차례로 입력 : ").split())

bmi = bmi(h, w)

print("%0.2f" % bmi)

if bmi >= 25:
    print("과체중")
elif bmi >= 20:
    print("표준체중")
elif bmi < 20:
    print("저체중")