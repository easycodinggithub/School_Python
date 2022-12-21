import matplotlib.pyplot as plt

# 한글 설정
plt.rc('font', family='Malgun Gothic')

labels = ["A형", "B형", "O형", "AB형"]

values = [27.2, 20.7, 40.2, 12.0]

# plt.pie(values)

plt.pie(values, labels=labels, autopct='%.1f%%')

plt.title("혈액형 비율")

plt.show()