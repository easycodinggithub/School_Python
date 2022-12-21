s = list(map(int, input("버섯의 점수 10개를 순서대로 입력하세요 : ").split()))

sum = 0

ss = []

for i in s:
    sum += i
    if sum == 100:
        break
    elif sum != 100:
        ss.append(sum)
        continue

print(ss)

stand1 = 100
stand2 = 100
quit = 0
while True:
    stand1 += 1
    stand2 -= 1
    for i in ss:
        if i == stand1 or i == stand2:
            final = stand1
            quit = 1
    if quit == 1:
        break

ssum = 0


print(final)
for i in s:
    ssum += i
    print("%d +"  % i,  end=" ")
    if ssum == final:
        break
print("= %d" % final)

