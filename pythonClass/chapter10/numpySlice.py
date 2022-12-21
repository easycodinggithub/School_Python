# 기본적으로 list 와 slice 방식이 같다.
import numpy as np

ages = np.array([18, 19, 25, 30, 28])

# ages 에서 20살 이상인 사람만 고르라고 하면 다음과 같은 조건식을 써준다.

y = ages > 20

yy = ages[ages > 20]

print(y)
print(yy)

# 2차원 배열을 논리인덱싱하면 => 1차원 배열로 전환됨
