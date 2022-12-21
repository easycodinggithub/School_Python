# 행정동명 행정동코드 위도 경도
# 압구정동 11680545 37.530734 127.028461
# 혜화동 11110650 37.587817 127.001745
# 평창동 11110560 37.613029 126.974485
# 이태원1동 11170650 37.532612 126.990182
# 한남동 11170685 37.537541 127.005165
# 능동 11215780 37.550578 127.081722
# 성북동 11290525 37.597248 126.992899
# 신사동 11680510 37.523807 127.026492
# 청담동 11680565 37.524399 127.050457
# 삼성1동 11680580 37.514315 127.062824

# 1. 위의 10개 동의 시간대별 총생활인구의 평균을 구하여 꺽은 선 그래프에 10개 동의 그래프를 그립니다.
#
# 그래프의 경우 친절한 정보가 많이 포함되어야 합니다. ^^

# 2. 위의 정보와 서울시 생활인구 데이터를 이용하여 지도에 결과를 표시합니다.
# 마커를 표시하되, 오후 6시 기준 가장 평균이 높은 동의 경우 아이콘의 색상이 Red, 평균이 높은 쪽에 속할 수록 아이콘의 색상이 Red에 가까운 색으로 표시하고,
# 가장 평균이 가장 낮은 동의 경우 아이콘 색상이 Blue, 평균이 낮은 쪽에 속할 수록 Blue에 가까운 색으로 표시하도록 합니다.
#
# 아이콘은 10개 동이 모두 서로 다른 모양이어야 합니다.
#
# 마커에 마우스가 올라가면 해당동 이름이 뜨면 됩니다.
#
# --------- 해당 과제에 대해 궁금한 점이 있으면 즉시 문의하시기 바랍니다.

import csv
import matplotlib.pyplot as plt
import folium as fm

plt.rc('font', family='Malgun Gothic')

f = open('C:\csv\LOCAL_PEOPLE_DONG_202208.csv', encoding='UTF-8')

people = csv.reader(f)
next(people)
people = list(people)

map_data = {
    11680545: [37.530734, 127.028461], # 압구정동
    11110650: [37.587817, 127.001745], # 혜화동
    11110560: [37.613029, 126.974485], # 평창동
    11170650: [37.532612, 126.990182], # 이태원1동
    11170685: [37.537541, 127.005165], # 한남동
    11215780: [37.550578, 127.081722], # 능동
    11290525: [37.597248, 126.992899], # 성북동
    11680510: [37.523807, 127.026492], # 신사동
    11680565: [37.524399, 127.050457], # 청담동
    11680580: [37.514315, 127.062824] # 삼성1동
}

name = {
    11680545: "압구정동",
    11110650: "혜화동",
    11110560: "평창동",
    11170650: "이태원1동",
    11170685: "한남동",
    11215780: "능동",
    11290525: "성북동",
    11680510: "신사동",
    11680565: "청담동",
    11680580: "삼성1동"
}

# 기준점
map_y = fm.Map([37.52860, 126.93431], zoom_start=10)

# 기준 시간
standard_time = 6

result = {
    11680545: 0,  # 압구정동
    11110650: 0,  # 혜화동
    11110560: 0,  # 평창동
    11170650: 0,  # 이태원1동
    11170685: 0,  # 한남동
    11215780: 0,  # 능동
    11290525: 0,  # 성북동
    11680510: 0,  # 신사동
    11680565: 0,  # 청담동
    11680580: 0,  # 삼성1동
}

icon = ["glyphicon-tree-deciduous", "glyphicon-globe", "glyphicon-facetime-video", "glyphicon-headphones", "glyphicon-cloud", "glyphicon-user", "glyphicon-heart", "glyphicon-tint", "glyphicon-plane", "glyphicon-leaf"]

icon_color = ["#FF0000", "#FF3333", "#FF6666", "#FF9999", "#FFCCCC", "#BFBFFF", "#8080FF", "#4040FF", "#0000FF", "#000099"]

# colors = ["darkred", 'red', "lightred", 'pink', 'orange', 'beige', 'cadetblue', 'lightblue', 'blue', 'darkblue']

for key, value in result.items():
    for row in people:
        time = int(row[1])
        dong = int(row[2])
        total = float(row[3])
        if time == standard_time and dong == key:
            result[key] += total

rank = sorted(result.items(), key=lambda x: x[1], reverse=True)

for i in range(10):
    code = rank[i][0]
    print(name[code])
    fm.Marker(
        [map_data[code][0], map_data[code][1]], tooltip=name[code],
        icon=fm.Icon(color="white", icon_color=icon_color[i], icon=icon[i], prefix="glyphicon")
    ).add_to(map_y)

map_y.save('index.html')


