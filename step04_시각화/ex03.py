import matplotlib.pyplot as plt

fig = plt.figure()
# ax1 = fig.add_subplot(1, 2, 1)
# ax2 = fig.add_subplot(1, 2, 2)
#
# plt.show()

# 문제. 창을 가로 2, 세로2로 나누어서
# 왼쪽 상단과 오른쪽 하단에 axes 를 배치하시오

ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 4)

plt.show()

