# string = list(input().split())
#
# stringCount = [0 for i in range(len(string))]
#
# for i in range(len(string)):
#     for j in range(len(string)):
#         if string[i] == string[j]:
#             stringCount[i] += 1
#
# for i in range(len(string)):
#     print("%s : %d"% (string[i], stringCount[i]))

string = list(input().split())

stringDict = {}

for i in string:
    stringDict[i] = 0

for i in string:
    stringDict[i] += 1

print(stringDict)