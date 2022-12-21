import matplotlib.pyplot as plt
import random as r

plt.rc('font', family='Malgun Gothic')

kor = [80, 20, 50, 20, 10, 50, 60, 30, 60]
eng = [90, 40, 60, 40, 10, 30, 50, 70, 90]

plt.boxplot([kor, eng], labels=['국어', '영어'])

plt.show()