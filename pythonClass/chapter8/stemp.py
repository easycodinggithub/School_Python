def checkStemp(k, n):
    coffee = 0
    while k >= n:
       coffee += 1 # 커피 1잔 사기
       k -= n # 쿠폰 n 장 반납
       k += 1 # 커피 1잔 샀으니 쿠폰 1개 득템
    return coffee

k, n = input().split(" ")

k = int(k)
n = int(n)

if k < 1 or k > 2000 or n < 1 or n > 1000:
    print("입력값이 잘못되었습니다.")

# k : 내가 가지고 있는 도장
# n : 카페에서 요구하는 도장 개수

print(checkStemp(k, n))