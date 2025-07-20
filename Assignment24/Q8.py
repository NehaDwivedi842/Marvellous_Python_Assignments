import pandas as pd 
import matplotlib.pyplot as plt

data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [85, 90, 78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82]
}
df = pd.DataFrame(data)


plt.hist(df['Math'], edgecolor='black')
plt.title('Histogram of Math Marks')
plt.xlabel('Math Score (Normalized)')
plt.show()
