import pandas as pd 
import numpy as np

data2 = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [np.nan, 76, 88],
    'Science': [91, np.nan, 85]
}
df2 = pd.DataFrame(data2)

# Fill missing values with column mean
df2_filled = df2.fillna(df2.mean(numeric_only=True))
print(df2_filled)
