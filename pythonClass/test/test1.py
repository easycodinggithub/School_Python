cnt = 0
leap_year = []

for year in range(2020, 2400, 1):
    if cnt < 5:
        if year % 400 == 0:
            cnt += 1
            leap_year.append(year)
        elif year % 4 == 0 and year % 100 != 0:
            cnt += 1
            leap_year.append(year)
        else:
            continue
    else:
        break

print(cnt)
print(leap_year)