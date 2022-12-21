import matplotlib.pyplot as plt

plt.rc('font', family='Malgun Gothic')

kor = [80, 20, 50, 20, 10, 50, 60, 30, 60]
eng = [90, 40, 60, 40, 10, 30, 50, 70, 90]

plt.scatter(kor, eng, color="red")

plt.xlabel("국어점수")
plt.ylabel("영어점수")

plt.show()