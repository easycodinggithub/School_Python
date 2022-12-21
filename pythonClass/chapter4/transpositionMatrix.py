# origin = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
origin = [[i, i+1, i+2] for i in range(1, 10, 3)]
print(origin)
new = []
for i in range(3):
    new += [[origin[j][i] for j in range(3)]]
print(new)
