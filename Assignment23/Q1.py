import pandas as pd 

data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [85, 90, 78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82]
}
df = pd.DataFrame(data)
print("Shape of Data:\n",df.shape)
print("Columns of Data:\n",df.columns.to_list())
print(" Data types:\n",df.dtypes)

