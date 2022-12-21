string = input()

print(string)

count = {"digits" : 0, "spaces" : 0, "alphas" : 0}

for i in string:
    if i.isalpha():
        count["alphas"] += 1
    elif i.isdigit():
        count["digits"] += 1
    elif i.isspace():
        count["spaces"] += 1

print(count)