def getIntRange(a, b):
    if a < 1 or a > 12:
        return False
    if b < 1 or b > 31:
        return False
    return True
print("날짜를 입력하세요.(월과 일)")
while True:
    month = int(input("월을 입력하세요.(1부터 12사이의 값) : "))
    if getIntRange(month, 1) != False:
        break

while True:
    day = int(input("일을 입력하세요.(1부터 31사이의 값) : "))
    if getIntRange(month, day) != False:
        break

if getIntRange(month, day):
    print("입력된 날짜는 %d월 %d일입니다." %(month, day))
