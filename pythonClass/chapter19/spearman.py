import pandas as pd
from scipy import stats
import statsmodels.formula.api as smf

df2 = pd.read_csv('survey.csv')

# corr = df2.corr()
#
# print(corr)

# corr2 = df2.corr(method='spearman')
#
# print(corr2)
#
# print(df2.income.corrd(df2.stress))

model = smf.ols(formula = 'jobSatisfaction~English', data = df2)

result = model.fit()

print(result.summary())

model2 = smf.ols(formula='jobSatisfaction~English + stress + income', data = df2)

result = model2.fit()

print(result.summary())