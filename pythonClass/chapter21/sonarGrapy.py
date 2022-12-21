import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense

import pandas as pd
df = pd.read_csv('./data/data/sonar3.csv', header=None)
print(df.head())

print(df[60].value_counts())

X = df.iloc[:, 0:60]
y = df.iloc[:, 60]

model = Sequential()
model.add(Dense(24, input_dim=60, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

history = model.fit(X, y, epochs=200, batch_size=10)