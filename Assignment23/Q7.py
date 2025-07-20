import pandas as pd 
import matplotlib.pyplot as plt

data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [85, 90, 78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82]
}
df = pd.DataFrame(data)
df['Total'] = df[['Math', 'Science', 'English']].sum(axis=1)

plt.bar(df['Name'], df['Total'], color='skyblue')
plt.xlabel('Student Name')
plt.ylabel('Total Marks')
plt.title('Total Marks of Students')
plt.show()

