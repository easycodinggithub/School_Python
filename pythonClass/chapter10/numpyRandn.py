import numpy as np
import matplotlib.pyplot as plt

np.random.seed(100)

# 시드가 설정되면 다음과 같은 문장을 수행하여 5개의 난수를 얻을 수 있다.
# 난수는 0.0에서 1.0 사이의 값으로 생성된다.

num = np.random.randn(5, 4)

print(num)

num = np.random.randn(5, 3)

print(num)

mu, sigma = 0, 0.1
r = np.random.normal(mu, sigma, 5)

plt.plot(r)
plt.show()