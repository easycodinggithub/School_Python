# 1. BMI(Body Mass Index)는 체중(kg)을 신장(m)의 제곱으로 나눈 값으로 체지방 축적을 잘 반영하기 때문에 비만도 판정에 많이 사용됩니다.
# 사용자로부터 이름과 신장과 체중(cm)로 입력받아서 BMI 값과 저체중, 표준, 과체중, 비만 중 어떤 상태에 해당하는지 출력하는 프로그램을 작성하세요.
#
# BMI Chart : BMI < 18.50(저체중) / BMI 18.50 ~ 24.99(표준) / BMI 24.99 ~ 29.99(과체중) / BMI > 30 (비만)
#
# -----실행결과
# 이름은 무엇입니까? : 우효림
# 몸무게를 kg 단위로 입력하세요. : 85.0
# 키를 cm 단위로 입력하세요 : 183
# 우효림의 BMI는 25.38 (소수점 둘째 자리에서 반올림하여 출력)이며, 현재 우효림의 상태는 과체중입니다.
# ----------------------


name = input("이름은 무엇입니까? : ")
weight = float(input("몸무게를 kg 단위로 입력하세요. : "))
height = float(input("키를 cm 단위로 입력하세요 : "))
bmi = float(weight / (math.pow(height/100, 2)))
stat = "표준"

if bmi > 30:
    stat = "비만"
elif bmi > 24.99:
    stat = "과체중"
elif bmi > 18.50:
    stat = "표준"
else:
    stat = "저체중"

print("%s의 BMI는 %.2f 이며, 현재 %s의 상태는 %s입니다." % (name, bmi, name, stat))
