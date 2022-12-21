# 3. 패스워드를 검증하는 함수 checkPass(p)를 작성하고 테스트하세요. 패스워드는 적어도 8글자 이상이어야 합니다.
# 또 적어도 1글자의 대문자와 소문자가 들어가야 하며, 적어도 1개의 숫자가 들어가야 합니다.
# ----- 실행결과
# 패스워드를 입력하세요 : abcdefgh
# 사용할 수 없는 패스워드입니다. 다시 입력하세요!!
#
# 패스워드를 입력하세요 : abcdefG1
# 사용 가능한 패스워드 입니다.

import re

def checkPass(p):
    if len(p) < 8 or not re.findall('[a-z]', p) or not re.findall('[A-Z]', p):
        return False
    else:
        return True

while True:
    p = input("패스워드를 입력하세요 : ")
    if checkPass(p):
        print("사용 가능한 패스워드 입니다.")
    else:
        print("사용할 수 없는 패스워드입니다. 다시 입력하세요!!")