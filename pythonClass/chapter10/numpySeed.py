import numpy as np

np.random.seed(100)

# 시드가 설정되면 다음과 같은 문장을 수행하여 5개의 난수를 얻을 수 있다.
# 난수는 0.0에서 1.0 사이의 값으로 생성된다.

num = np.random.rand(5)

print(num)

num = np.random.rand(5, 3)

print(num)