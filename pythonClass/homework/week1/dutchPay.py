# 2. 미국여행 중 식당에 들러서 저녁 식사를 했습니다.
# 음식비용, 팁비율, 부가세비율, 식사비용 나눌 사람의 수, 각자 내야 하는 돈과 총액을 출력하세요.
#
# 입력받을 값 : 음식비용, 팁비율, 부가세비율(<= 20%), 식사비용 나눌 사람의 수
# 출력할 값 : 음식비용, 팁비율, 부가세비율, 식사비용 나눌 사람의 수, 각자 내야 하는 돈, 음식비용 + 팁 + 부가 =  총액

allFoodPrice = int(input("음식 비용을 입력해 주세요 : "))
tipRatio = int(input("팁 비율을 입력해 주세요 : "))
surtaxRatio = int(input("부가세 비율(<= 20%)을 입력해 주세요 : "))
divideNumber = int(input("식사비용 나눌 사람의 수를 입력해 주세요 : "))

allPrice = int(allFoodPrice + (allFoodPrice * (tipRatio / 100)) + (allFoodPrice * (surtaxRatio / 100)))
oneFoodPrice = int(allPrice / divideNumber)

print("음식 비용은 %d 입니다." %(allFoodPrice))
print("팁 비율은 %d 입니다." %(tipRatio))
print("부가세 비율은 %d 입니다." %(surtaxRatio))
print("식사 비용 나눌 사람의 수는 %d 입니다." %(divideNumber))
print("각자 내야 하는 돈은 %d 입니다." %(oneFoodPrice))
print("총액은 %d 입니다." %(allPrice))

