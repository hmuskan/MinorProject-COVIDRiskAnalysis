import pandas as pd

list = ['District name', 'Age_Group_0_29', 'Age_Group_30_49', 'Age_Group_50']
df1 = pd.read_csv('districts.csv')
df2 = pd.read_csv('india-districts-census-2011.csv', usecols=list)
df3 = pd.merge(df1,df2, how='inner',left_on='District',right_on='District name')
df3.to_csv('output.csv')

