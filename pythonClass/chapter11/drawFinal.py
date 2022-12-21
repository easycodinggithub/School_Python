import numpy as np
import matplotlib.pyplot as plt

x = np.array([2, 4, 6, 8])
y = np.array([81, 93, 91, 97])

W = np.arange(-3, 3, 0.1)
B = np.arange(0, 100, 1)

# wx + b

min = 1000000

for w in W:
    for b in B:
        temp = sum((y - (w * x + b))**2)
        if min > temp:
            min = temp
            minw = w
            minb = b

print(minw, minb)

x1 = int(input())
print(minw*x1 + minb)