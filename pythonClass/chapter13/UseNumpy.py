import numpy as np
# a = np.array([[2, 3], [5, 2]])
# d = np.array([[1, 2, 3, 4, 5], [2, 4, 5, 6, 7], [5, 7, 8, 9, 9]])
# b = np.array([2, 3, 4, 5, 6])
#
# print(a)
# print(d)
#
# print(d[0][0])
# print(d[1, 2])
#
# print(d[1:, 3:])
#
# print(d.shape)
# print(a.shape)
# print(b.shape)
#
# d = d.astype('float64')
# d = d.astype('int64')
#
# e = np.zeros((2, 10))
# print(e)
#
# print(e.dtype)
#
# e = e.astype('int64')
# print(e.dtype)
#
# f = np.ones((2, 10))
# print(f)
#
# print(d.dtype)
# print(a.dtype)
# print(b.dtype)
#
# a = np.arange(2, 10)
# print(a)
#
# b = np.ones((2, 3))
# print(b)
#
# # 전치 행렬 2 x 3 => 3 x 2
# c = np.transpose(b)
# print(c)
#
# arr1 = np.array([[2, 3, 4], [6, 7, 8]])
# arr2 = np.array([[12, 23, 14], [36, 47, 58]])
# arr3 = np.array([100, 200, 300])
# arr4 = np.array([100, 200, 300, 400])
#
# a = arr1 + arr2
#
# b = arr1 * arr2
#
# c = arr1 / arr2
#
# d = arr1 + arr3
#
# # e = arr1 + arr4
#
# print(a)
# print(b)
# print(c)
# print(d)
# # print(e)
#
# # print(arr1.shape)
# # print(arr2. shape)
# # print(arr3.shape)
# # print(arr4.shape)
#
# # 결론 숫자 하나라도 같은게 있으면 계산 됨, 아님 안됨
#
# arr5 = np.array([[9], [3]])
#
# print(arr5.shape)
#
# a = arr1 + arr5
#
# print(a)

d = np.array([[1, 2, 3, 4, 5], [2, 4, 5, 6, 7], [5, 7, 8, 9, 9]])

d_list = [[1, 2, 3, 4, 5], [2, 4, 5, 6, 7], [5, 7, 8, 9, 9]]

# d_list[:2] = 0
d[:2] = 0
print(d)
print(d_list)