import matplotlib.pyplot as plt
import random as r

plt.rcParams['axes.unicode_minus'] = False

plt.rc('font', family='Malgun Gothic')

singer = ['A', 'B', 'C', 'D', 'E']
week1 = [42, 58, 19, 92, 84]

for i in range(len(week1)):
    week1[i] = -(week1[i])

week2 = [53, 52, 48, 98, 73]

plt.barh(range(5), week1, color="red", label="첫째 주")
plt.barh(range(5), week2, color="blue", label="둘째 주")

plt.legend()

plt.title("오디션 프로그램 득표 현황")

plt.show()