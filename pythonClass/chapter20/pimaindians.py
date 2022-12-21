from keras.models import Sequential
from keras.layers import Dense

# pandas 라이브러리를 불러옵니다.
import pandas as pd

# 피마 인디언 당뇨병 데이터셋을 불러옵니다.

df = pd.read_csv('./data/data/pima-indians-diabetes3.csv')

X = df.iloc[:, 0:8] # 세부 정보를 X로 지정합니다.
y = df.iloc[:, 8] # 당뇨병 여부를 y로 지정합니다.

model = Sequential()

model.add(Dense(12, input_dim=8, activation='relu', name='Dense_1'))
model.add(Dense(8, activation='relu', name='Dense_2'))
model.add(Dense(1, activation='sigmoid', name='Dense_3'))
model.summary()

# 모델을 컴파일합니다.
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# 모델을 실행합니다.
history = model.fit(X, y, epochs=100, batch_size=5)