import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10.1, 0.1)

r = 10

y1 = np.sqrt(r**2 -x**2)
y2 = -np.sqrt(r**2 -x**2)

plt.plot(x, y1)
plt.plot(x, y2)
plt.show()