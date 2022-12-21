a = [0]
a[1:] = list(map(int, input().split()))

s = 0
formula = ""
for x in a[1:]:
    s += x
    formula = formula + str(x)
    if s < 100:
        res = s
        formula = formula + " + "
    else:
        if 100 - res >= s - 100:
            res = s
            formula = formula + " = "
        break

print(formula + str(res))