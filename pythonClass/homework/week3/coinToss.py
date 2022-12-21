# 3. 리스트에 동전 던지기의 결과를 저장한 결과가 아래와 같습니다.
# 가장 길게 앞면이나 뒷면이 연속해서 나왔던 위치를 찾는 코드를 작성하세요.
# 리스트 내용 : [H, T, H, H, H, T, T, H, T, H, T, T]
# ----------- 실행결과
# [1, 1, 0, 0, 1, 0, 1, 1, 1, 0]
# 최대 연속 길이 : 3

result = ['H', 'T', 'H', 'H', 'H', 'T', 'T', 'H', 'T', 'H', 'T', 'T']

# coinToss = [1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0]

# print(len(result)-1)

length = len(result)-1

coinToss = [1] * length

for i in range(length):
    if result[i] == result[i+1]:
        coinToss[i] = 0

print(coinToss)

max = 1
tempMax = 1

for j in range(len(coinToss)-1):
    if coinToss[j] == coinToss[j+1]:
        tempMax += 1
    else:
        if tempMax >= max:
            max = tempMax
        tempMax = 1
print("최대 연속 길이 : %d" % max)