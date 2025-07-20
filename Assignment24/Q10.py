import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [85, 90, 78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82]
}
df = pd.DataFrame(data)

sns.boxplot(x=df['English'])
plt.title('Boxplot of English Marks')
plt.show()