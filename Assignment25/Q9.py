import pandas as pd 

data = {'Marks': [45, 67, 88, 32, 76]}
df = pd.DataFrame(data)

df['Result'] = df['Marks'].where(df['Marks'] >= 50, 'Fail')
print(df)
