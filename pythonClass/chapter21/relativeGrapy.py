import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 아이리스 데이터를 불러옵니다.
df = pd.read_csv('./data/data/iris3.csv')

# sns.pairplot(df, hue='species')

# plt.show()

# df.head() # 첫 다섯 줄을 봅니다.

X = df.iloc[:, 0:4]
y = df.iloc[:, 4]

print(X[0:5])
print(y[0:5])

y = pd.get_dummies(y)

print(y[0:5])

# 모델 설정
model = Sequential()
model.add(Dense(12, input_dim=4, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(3, activation='softmax'))
model.summary()

# 모델 컴파일
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# 모델 실행
history = model.fit(X, y, epochs=50, batch_size=5)