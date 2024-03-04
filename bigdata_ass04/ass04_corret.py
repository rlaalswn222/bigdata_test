import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

plt.rcParams["font.family"] = 'NanumGothic'
csv_file_path = 'student_health_3.csv'
x = pd.read_csv("student_health_3.csv", encoding='utf-8')

year = x["학년"]
year = year.replace([1, 2, 3], 1)
year = year.replace([4, 5, 6], 2)
input_data = np.array([x["이완기"], x["수축기"],x["키"],x["몸무게"]]).T
n_neighbors=5

X_train, X_test, y_train, y_test = train_test_split(input_data, year, random_state=42)

knn = KNeighborsClassifier(n_neighbors)
knn.fit(X_train, y_train)
print(knn.score(X_test, y_test))
print(knn.predict([[80,100,140,60]]))

logicr = LogisticRegression()
logicr.fit(X_train, y_train)
print(logicr.score(X_test, y_test))
print(logicr.predict([[80,100,140,60]]))