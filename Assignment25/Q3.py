from sklearn.preprocessing import LabelEncoder
import pandas as pd

data = {'City': ['Pune', 'Mumbai', 'Delhi', 'Pune', 'Delhi']}
df = pd.DataFrame(data)

le = LabelEncoder()
df['City_encoded'] = le.fit_transform(df['City'])
print(df)
