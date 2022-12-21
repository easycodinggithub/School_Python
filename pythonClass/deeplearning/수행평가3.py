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

df = pd.read_csv('water_potability.csv')

# 데이터셋 컬럼 확인

# 1. ph: pH of 1. water (0 to 14).
# 2. Hardness: Capacity of water to precipitate soap in mg/L.
# 3. Solids: Total dissolved solids in ppm.
# 4. Chloramines: Amount of Chloramines in ppm.
# 5. Sulfate: Amount of Sulfates dissolved in mg/L.
# 6. Conductivity: Electrical conductivity of water in μS/cm.
# 7. Organic_carbon: Amount of organic carbon in ppm.
# 8. Trihalomethanes: Amount of Trihalomethanes in μg/L.
# 9. Turbidity: Measure of light emiting property of water in NTU.
# 10. Potability: Indicates if water is safe for human consumption. Potable -1 and Not potable -0

# 1. ph: 1의 pH. 물(0 ~ 14).
# 2. 경도: 비누 침전물의 mg/L 용량
# 3. 고체: 총 용해 고형물(ppm)입니다.
# 4. 클로라민: 클로라민의 양(ppm)입니다.
# 5. 황산염: mg/L로 용해된 황산염의 양
# 6. 전도성: 물의 전기전도도(μS/cm)
# 7. 유기_탄소: 유기 탄소의 양(ppm)입니다.
# 8. 트리할로메탄: 트라이할로메탄의 양(μg/L).
# 9. 탁도: NTU에서 물의 발광 특성 측정.
# 10. 휴대성: 물이 사람이 먹기에 안전한지 여부를 나타냅니다. 음용 -1 및 음용 -0

print(df.columns)

print(df["Potability"].value_counts())

print(df.describe())

print(df.corr())

colormap = plt.cm.gist_heat
plt.figure(figsize=(12, 12))

sns.heatmap(df.corr(), linewidths=0.1, vmax=0.5, cmap=colormap, linecolor='white', annot=True)

plt.show()

# 색깔이 하얀색에 가까울수록 수질이 안전함, (=수치가 높을수록)

# 수질 안정성에 가장 관련이 있는 Solids(고체), Chloramines(클로라민)을 따로 떼어 수질과의 관련성 점검


# Solids 와 수질과의 관계

plt.hist(x=[df.Solids[df.Potability==0], df.Solids[df.Potability==1]], bins=30, histtype='barstacked', label=['safe', 'not safe'])

plt.xlabel("Solids")
plt.ylabel('sample')

# safe : 수질이 안전함, not safe : 수질이 안전하지 않음

plt.legend()

plt.show()

# Solids 가 높아질 수록 수질이 불안전해지는 것을 알 수 있다.


# Chloramines 와 수질과의 관계

plt.hist(x=[df.Chloramines[df.Potability==0], df.Chloramines[df.Potability==1]], bins=30, histtype='barstacked', label=['safe', 'not safe'])

plt.xlabel("Chloramines")
plt.ylabel('sample')

# safe : 수질이 안전함, not safe : 수질이 안전하지 않음

plt.legend()

plt.show()

# Chloramines 가 높아질 수록 수질이 불안전해지는 것을 알 수 있다.

x = df.iloc[:, 0:9] # 세부정보를 X로 저장

# print(X.dtypes)
X = x.astype(float)
y = df.iloc[:, 9] # 수질 안정성 여부를 y로 저장

model = Sequential()
model.add(Dense(12, input_dim=9, activation='relu', name='Dense_1'))
model.add(Dense(8, activation='relu', name='Dense_2'))
model.add(Dense(1, activation='sigmoid', name='Dense_3'))

model.summary()

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy']) # 모델 컴파일
history = model.fit(X, y, epochs=100, batch_size=5)


