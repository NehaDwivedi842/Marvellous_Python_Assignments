import pandas as pd 

data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [85, 90, 78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82]
}
df = pd.DataFrame(data)

df['Gender'] = ['Male', 'Male', 'Female']
avg_marks_by_gender = df.groupby('Gender')[['Math', 'Science', 'English']].mean()
print(avg_marks_by_gender)
