import numpy as np
scores = np.array([[99, 93, 60], [98, 82, 93], [93, 65, 81], [78, 82, 81]])

Sum, Min, Max, Mean, Std, Var = scores.sum(), scores.min(), scores.max(), scores.mean(), scores.std(), scores.var()

print(Sum, Min, Max, Std, Var)