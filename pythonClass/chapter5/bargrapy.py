import matplotlib.pyplot as plt

sales = [1, 5, 7, 3, 7]
sales = [1, 2, 3, 3, 3, 5, 7, 7, 8, 10]

plt.hist(sales, bins=30)
plt.show()