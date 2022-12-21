# 4. 키와 값을 가지고 있는 2개의 리스트를 합쳐서 하나의 딕셔너리로 만드는 프로그램을 작성하세요.
# ---- 실행결과
# colors = ["red", "green", "blue"]
# values = ["#FF0000", "#0080000", "#0000FF"]
# Dics = {"red" : "#FF0000", "green" : "#008000", "blue" : "#0000FF"}

colors = ["red", "green", "blue"]
values = ["#FF0000", "#0080000", "#0000FF"]
Dics = {}
for i in range(3):
    Dics[colors[i]] = values[i]
    print(colors[i], values[i])
print(Dics)