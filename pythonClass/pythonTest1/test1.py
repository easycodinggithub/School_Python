year = 2020

yearList = []

while len(yearList) < 5:
    if year % 400 == 0:
        yearList.append(year)
    elif year % 4 == 0 and year % 100 != 0:
        yearList.append(year)
    year += 1

for i in yearList:
    print(i, end=" ")

