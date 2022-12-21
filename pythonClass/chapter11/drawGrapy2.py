import numpy as np
import matplotlib.pyplot as plt

# x = np.arange(-1, 1.1, 0.1)
#
# y = x*x + 2
#
# plt.plot(x, y)
# plt.show()

x = np.arange(0, 101, 1)

y = np.sqrt(x)

plt.plot(x, y)
plt.show()