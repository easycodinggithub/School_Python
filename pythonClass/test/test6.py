n = int(input())
a = [0]
a[1:] = list(map(int, input().split()))

x = min(a[1:])
y = max(a[1:])
print("최단거리 : " + str((y - x) * 2))