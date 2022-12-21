import matplotlib.pyplot as plt
import random as r

plt.rc('font', family='Malgun Gothic')

height = [r.randint(100, 200) for i in range(100)]

weight = [r.randint(20, 100) for i in range(100)]

plt.scatter(height, weight, c=weight, cmap="RdPu")

plt.colorbar(label="키")

plt.xlabel("키")
plt.ylabel("몸무게")

plt.title("키와 몸무게의 상관관계")

plt.show()