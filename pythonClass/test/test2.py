n = 100
a = [True] * (n + 1)
m = int(n**0.5)

for i in range(2, m + 1):
    if a[i] == True:
        for j in range(i + i, n + 1, i):
            a[j] = False

prime = [i for i in range(2, n + 1) if a[i] == True]
print(prime)

for i in range(0, len(prime) - 2):
    if prime[i+1] - prime[i] == 2:
        print(prime[i], prime[i+1])

# check = [0] * 101
# for i in range( 2, 101 ):
#     if check[i] == 0:
#         print(i, end = " ")
#         for j in range(i * i, 101, i):
#             check[j] = 1
#
# print("\n")
# for i in range( 2, 99 ):
#     if check[i] == 0 and check[i+2] == 0:
#         print(i, i+2)