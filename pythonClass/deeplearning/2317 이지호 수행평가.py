import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# row 생략 없이 출력
# pd.set_option('display.max_rows', 10000)
# col 생략 없이 출력
# pd.set_option('display.max_columns', 1000)

# 수질 안정성 데이터셋을 불러옵니다.

df = pd.read_csv('diabetes-dataset.csv')

# 데이터셋 컬럼 확인

# Pregnancies : 임신
# Glucose : 포도당
# BloodPressure : 혈압
# SkinThickness : 피부 두께
# Insulin : 인슐린
# BMI : BMI
# DiabetesPedigreeFunction : 당뇨병혈통 함수
# Age : 나이
# Outcome : 결과

print(df.columns)

print(df["Outcome"].value_counts())

print(df.describe())

print(df.corr())

colormap = plt.cm.gist_heat
plt.figure(figsize=(12, 12))

sns.heatmap(df.corr(), linewidths=0.1, vmax=0.5, cmap=colormap, linecolor='white', annot=True)

plt.show()

# 색깔이 하얀색에 가까울수록 당뇨병에 결릴 확률이 증가함 (=수치가 높을수록)

# 당뇨병에 가장 관련이 있는 Glucose(포도당), BMI을 따로 떼어 당뇨병과의 관련성 점검


# Glucose 과 당뇨병과의 관계

plt.hist(x=[df.Glucose[df.Outcome==0], df.Glucose[df.Outcome==1]], bins=30, histtype='barstacked', label=['normal', 'Diabetes'])

plt.xlabel("Glucose")
plt.ylabel('sample')

# normal : 정상, Diabetes : 당뇨병

plt.legend()

plt.show()

# Glucose 이 높아질 수록 당뇨병이 걸릴 확률이 증가하는 것을 알 수 있다.

# BMI 와 당뇨병과의 관계

plt.hist(x=[df.BMI[df.Outcome==0], df.BMI[df.Outcome==1]], bins=30, histtype='barstacked', label=['normal', 'Diabetes'])

plt.xlabel("BMI")
plt.ylabel('sample')

# normal : 정상, Diabetes : 당뇨병

plt.legend()

plt.show()

# BMI 가 높아질 수록 당뇨병이 걸릴 확률이 증가하는 것을 알 수 있다.

X = df.iloc[:, 0:8] # 세부정보를 X로 저장
y = df.iloc[:, 8] # 당뇨병 여부를 y로 저장

model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu', name='Dense_1'))
model.add(Dense(8, activation='relu', name='Dense_2'))
model.add(Dense(1, activation='sigmoid', name='Dense_3'))

model.summary()

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy']) # 모델 컴파일
history = model.fit(X, y, epochs=100, batch_size=5)


