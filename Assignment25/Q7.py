import pandas as pd 
from sklearn.preprocessing import MinMaxScaler

data = {'Age': [18, 22, 25, 30, 35]}
df = pd.DataFrame(data)

scaler = MinMaxScaler()
df['Age_scaled'] = scaler.fit_transform(df[['Age']])
print(df)

