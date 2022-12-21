import pandas as pd
from scipy import stats

df2 = pd.read_csv('survey.csv')

print(df2.head())

male = df2.income[df2.sex == 'm']
female = df2.income[df2.sex == 'f']

ttest_result = stats.ttest_ind(male, female)

print(ttest_result)

if ttest_result[1] > .05:
    print('p-value는 %f로 95%% 수준에서 유의하지 않음' % ttest_result[1])
else:
    print('p-value는 %f로 95%% 수준에서 유의함' % ttest_result[1])
