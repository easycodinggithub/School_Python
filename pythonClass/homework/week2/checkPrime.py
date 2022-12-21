# 4. 주어진 정수가 소수인지를 검사하는 함수 testPrime(n)을 작성하고 이 함수를 호출하여 2부터 100사이의 소수를 출력하세요.
# ------- 실행결과
# 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53  59 61 67 71 73 79 83 89 97

def testPrime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True

for i in range(2, 101):
    if testPrime(i):
        print(i, end=" ")