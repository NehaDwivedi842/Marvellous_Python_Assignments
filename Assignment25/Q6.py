import pandas as pd


data = {'Grade': ['A+', 'B', 'A', 'C', 'B+']}
df = pd.DataFrame(data)

replace_dict = {
    'A+': 'Excellent',
    'A': 'Very Good',
    'B+': 'Good',
    'B': 'Average',
    'C': 'Poor'
}
df['Grade'] = df['Grade'].replace(replace_dict)
print(df)
