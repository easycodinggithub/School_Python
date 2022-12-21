import datetime

dt_now = datetime.datetime.now()

name = input("이름 : ")
birth = input("생년월일 : ")
old = dt_now.year - int(birth[0:4])
print("나이 : %d" % old)
phone = input("전화번호 : ")

print("%s님 환영합니다." % name)
print("당신의 생년월일은 %s 입니다." % birth)
print("당신의 나이는 %s 입니다." % old)
print("당신의 전화번호는 %s 입니다." % phone)