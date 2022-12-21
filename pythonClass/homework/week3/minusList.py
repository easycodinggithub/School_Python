# 5. set1, set2의 2개의 세트가 주어져 있습니다. set1 또는 set2, 어느 한쪽에만 있는 요소들을 추출하는 프로그램을 작성하세요.
# set1 = {10, 20, 30, 40, 50, 60}
# set2 = {30, 40, 50, 60, 70, 80}
# 어느 한쪽에만 있는 요소들 = {10, 20, 70, 80}

set1 = {10, 20, 30, 40, 50, 60}
set2 = {30, 40, 50, 60, 70, 80}

# print(set1 - set2)
# print(set1.difference(set2))
#
# print(set2 - set1)
# print(set2.difference(set1))

print(set1 ^ set2)
# print(set2 ^ set1)