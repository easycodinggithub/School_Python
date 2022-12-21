import sys
sys.setrecursionlimit(1000)

def checkStemp(k, n, c):
    if k < n:
        return c
    return checkStemp((k-n)+1, n, c+1)


k, n = map(int, (input().split()))

if k < 1 or k > 2000 or n < 1 or n > 1000:
    print("입력값이 잘못되었습니다.")

# k : 내가 가지고 있는 도장
# n : 카페에서 요구하는 도장 개수

print(checkStemp(k, n, 0))