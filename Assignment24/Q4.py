import pandas as pd 
import matplotlib.pyplot as plt

data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [85, 90, 78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82]
}
df = pd.DataFrame(data)


row = df[df['Name'] == 'Sagar'][['Math', 'Science', 'English']].iloc[0]
row.plot(kind='pie', autopct='%1.1f%%')
plt.title("Sagar Subject Marks")
plt.show()
