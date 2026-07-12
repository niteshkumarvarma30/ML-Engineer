import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv'
columns = ['pregnant', 'glucose', 'diastolic', 'triceps', 'insulin', 'bmi', 'family', 'age', 'class']
df = pd.read_csv(url, names=columns)

X = df[['pregnant', 'glucose', 'diastolic', 'triceps', 'insulin', 'bmi', 'family', 'age']]
y = df['class']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

scaler = StandardScaler()
lr = LogisticRegression()

lr.fit(scaler.fit_transform(X_train), y_train)

print(dict(zip(X.columns, abs(lr.coef_[0]).round(2))))
