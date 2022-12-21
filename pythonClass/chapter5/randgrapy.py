import matplotlib.pyplot as plt
import random as r

numbers = [r.randint(1, 9) for i in range(10)]

plt.hist(numbers, bins=10)
plt.show()