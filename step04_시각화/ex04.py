import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

ax.set_xlim([0, 1]) # x 축의 값의 범위
ax.set_ylim([0, 2.5]) # y 축의 값의 범위
ax.set_xlabel('x-Axis', size=10)
ax.set_ylabel('y-Axis', size=10)

ax.set_title('matplotlib test', size=20)

plt.show()