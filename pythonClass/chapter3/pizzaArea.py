import math

def calculatePizzaArea(radius):
    return math.pow(radius, 2)*3.14

regularPizzaArea = int(input("20cm 피자 반지름: "))
largePizzaArea = int(input("30cm 피자 반지름: "))
print("20cm 피자 2개의 면적: %d" % (calculatePizzaArea(regularPizzaArea)*2))
print("30cm 피자 1개의 면적: %d" % (calculatePizzaArea(largePizzaArea)))
