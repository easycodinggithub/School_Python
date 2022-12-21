birth = list(input().split(" "))

incite = list(str(int(birth[0]) + int(birth[1]) + int(birth[2])))

inciteNum = incite[-3]

if int(inciteNum) % 2 == 0:
    print("대박")
else:
    print("중박")
