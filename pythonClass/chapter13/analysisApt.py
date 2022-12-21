import pandas as pd
df = pd.read_csv('apt.csv', encoding='cp949')

# print(df.head(10))
# print(df.tail(10))

# print(df.시군구)
# print(df['시군구'])

# print(df.전용면적 > 80)

# print(df[df.전용면적 > 80])
# print(df.거래금액[df.전용면적 > 80])
# print(df.거래금액[(df.전용면적 > 80) & (df.거래금액 < 15000)])
# print(df.거래금액[(df.전용면적 > 80) | (df.거래금액 < 15000)])
# print(df.loc[:10, ['단지명', '거래금액']])
# print(df.loc[:, ['단지명', '거래금액']][df.거래금액 > 40000])
# df['단가'] = df.거래금액 / df.전용면적
# print(df.head())

# print(df.sort_values(by = '거래금액').loc[:, ['전용면적', '시군구']])
# print(df.sort_values(by = '거래금액', ascending= False).loc[:, ['전용면적', '시군구']])

# print(df[df.거래금액 > 40000].sort_values(by="전용면적", ascending=False).loc[:, ["거래금액", "전용면적", "시군구"]])

# print(df[df.시군구.str.find('강릉') > -1])
# dff = df[df.시군구.str.find('강릉') > -1]
# dff.mean()