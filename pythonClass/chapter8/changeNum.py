def reverse(listNum):
    return list(reversed(listNum))

NumStr = list(input())

rNumStr = reverse(NumStr)

NumInt = int("".join(s for s in NumStr))

rNumInt = int("".join(s for s in rNumStr))

result = NumInt + rNumInt

rResult = reverse(str(result))

print(result)
print(rResult)

finalResult = int("".join(s for s in rResult))

if result == finalResult:
    print("YES")
else:
    print("NO")

