import pandas as pd 
from sklearn.preprocessing import MinMaxScaler

data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [85, 90, 78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82]
}
df = pd.DataFrame(data)
scaler = MinMaxScaler()
df['Gender'] = ['Male', 'Male', 'Female']
print (df)
df_encoded = pd.get_dummies(df, columns=['Gender'])
print(df_encoded)