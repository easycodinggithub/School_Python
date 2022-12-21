import numpy as np

score_dic = {
    "Kim" : [99, 83, 95],
    "Lee" : [68, 45, 78],
    "Choi" : [25, 56, 69]
}

for i in score_dic.values():
    print(np.mean(i))