import matplotlib.pyplot as plt
import random as r

plt.rc('font', family='Malgun Gothic')

score = [r.randint(1, 1000) for i in range(100)]

height = [r.randint(100, 200) for i in range(100)]

weight = [r.randint(20, 100) for i in range(100)]

plt.scatter(height, weight, s=score, c=score, cmap="rainbow", alpha=0.1)

plt.colorbar(label="체육 점수")

plt.xlabel("키")
plt.ylabel("몸무게")

plt.title("키와 몸무게의 상관관계")

plt.show()