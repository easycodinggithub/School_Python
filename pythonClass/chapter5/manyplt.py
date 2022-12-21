import matplotlib.pyplot as plt

plt.rc('font', family='Malgun Gothic')

singer = ['A', 'B', 'C', 'D', 'E']
week1 = [42, 58, 19, 92, 84]
week2 = [53, 52, 48, 98, 73]

plt.plot(singer, week1, color="red", label="첫째 주")
plt.plot(singer, week2, color="blue", label="둘째 주")

plt.legend()

plt.title("오디션 프로그램 득표 현황")

plt.show()