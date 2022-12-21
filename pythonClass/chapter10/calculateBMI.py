import numpy as np

height = np.array([ 1.83, 1.76, 1.69, 1.86, 1.77, 1.73])
weight = np.array([ 86, 74, 59, 95, 80, 68])

bmi = weight / height**2
print(bmi)
