def checkLeap(year):
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False

month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

string = list(input().split(" "))

if checkLeap(int(string[0])):
    month[1] = 29
print(month[int(string[1])-1])


