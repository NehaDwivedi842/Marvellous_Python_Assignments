from sklearn.model_selection import train_test_split
import pandas as pd

data = {'Age': [22, 25, 47, 52, 46, 56], 'Purchased': [0, 1, 1, 0, 1, 0]}
df = pd.DataFrame(data)

X_train, X_test, y_train, y_test = train_test_split(df[['Age']], df['Purchased'], test_size=0.3, random_state=1)
print(X_train, y_train)
