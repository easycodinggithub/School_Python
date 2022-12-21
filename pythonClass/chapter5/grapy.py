import matplotlib.pyplot as plt

plt.rc('font', family='Malgun Gothic')
# plt.rcParams['font.family'] ='Malgun Gothic'
# plt.rcParams['axes.unicode_minus'] =False

plt.figure(dpi=200)
# plt.figure(figsize=(8, 8))

month = ["Mar", "Apr", "May", "Jun", "Jul"]

# sales = [1, 3, 5, 3, 7]
sales = [1, 5, 7, 3, 7]

# plt.plot(month, sales, color="red", label="단위:개수")
plt.bar(month, sales, color="red", label="단위:개수")

plt.legend()
# plt.legend(loc="lower right")

# plt.plot([1, 5, 7, 3, 7])

plt.xlabel("월")

plt.ylabel("매출")

# plt.title("Hello plt")
plt.title("월별 판매 실적")

plt.show()

