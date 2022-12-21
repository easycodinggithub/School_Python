import matplotlib.pyplot as plt
import random as r

plt.rc('font', family='Malgun Gothic')

height1 = [r.randint(140, 180) for i in range(100)]
weight1 = [r.randint(40, 80) for i in range(100)]
score1 = [r.randint(1, 200) for i in range(100)]
height2 = [r.randint(160, 200) for i in range(100)]
weight2 = [r.randint(50, 100) for i in range(100)]
score2 = [r.randint(1, 200) for i in range(100)]

# crimeson
# indigo

plt.scatter(height1, weight1, s=score1, color="crimson", alpha=0.7, label="그룹 1")
plt.scatter(height2, weight2, s=score2, color="indigo", alpha=0.7, label="그룹 2")

plt.legend()

plt.xlabel("키")
plt.ylabel("몸무게")

plt.title("키와 몸무게의 상관관계")

plt.show()