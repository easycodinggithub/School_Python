def bigger(a, b):
    if a > b:
        return a
    else:
        return b

def oddEven(n):
    if n % 2 == 0:
        return "짝수"
    else:
        return "홀수"

a, b = map(int, input().split())

print(oddEven(bigger(a, b)))