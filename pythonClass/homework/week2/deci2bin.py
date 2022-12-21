# 5. 사용자가 입력한 10진수를 2진수 문자열로 변환하는 함수 deci2bin(n)을 작성하고 테스트하세요.
# ------- 실행결과
# 10진수 : 32
# 2진수 : 100000

def deci2bin(n):
    nList = bin(n)
    return nList[2:]

n = int(input("10진수 : "))
print(deci2bin(n))
