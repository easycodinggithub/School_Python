import matplotlib.pyplot as plt
import random as r

plt.rc('font', family='Malgun Gothic')

kor = [80, 20, 50, 20, 10, 50, 60, 30, 60]
# kor = [r.randint(0, 100) for i in range(100)]

plt.boxplot(kor)

plt.show()