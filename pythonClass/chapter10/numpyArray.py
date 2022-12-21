import numpy as np

z = np.zeros((2, 10))

o = np.ones((2, 10))

print(z, o)

# 숫자가 같은게 있으면 무조건 계산 됨
# 만약 같은게 없으면 무조건 계산 안됨

# ex
# (2, 3) 과 (2, ) 는 계산 됨

# sample1 = np.array([1, 2, 3])
#
# sample2 = np.array([1, 2], [3, 4])
#
# print(sample1 + sample2)

sample1 = np.array([[1, 2, 3], [4, 5, 6]])

sample2 = np.array([[1, 2, 7], [3, 4, 8], [3, 5, 7]])

print(sample1 + sample2)
