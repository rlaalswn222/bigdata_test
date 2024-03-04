import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model

plt.rcParams["font.family"] = 'NanumGothic'

csv_file_path = 'student_health_3.csv'

df = pd.read_csv(csv_file_path, encoding='utf-8')

df['class'] = np.where(df['학년'].isin([1, 2, 3]), 'Class 1', 'Class 2')

class1_data = df[df['class'] == 'Class 1']
class2_data = df[df['class'] == 'Class 2']

regr_class1 = linear_model.LinearRegression()
regr_class2 = linear_model.LinearRegression()


X_train_class1 = class1_data[['학년']]
y_train_class1 = class1_data['키']
regr_class1.fit(X_train_class1, y_train_class1)

X_train_class2 = class2_data[['학년']]
y_train_class2 = class2_data['키']
regr_class2.fit(X_train_class2, y_train_class2)

# Make predictions for each class
# 각 클래스에 대한 예측을 수행합니다.
class1_predictions = regr_class1.predict(X_train_class1)
class2_predictions = regr_class2.predict(X_train_class2)

plt.scatter(X_train_class1['학년'], y_train_class1, color="black")
plt.plot(X_train_class1['학년'], class1_predictions, color="blue", linewidth=3)
plt.title('Class 1 Linear Regression')
#plt.xticks(np.arange(int(min(1.0)), int(max(6.0))+1, 1))
plt.xticks(np.arange(int(min(X_train_class1['학년'])), int(max(X_train_class1['학년']))+1, 1))
plt.xlabel('학년')
plt.ylabel('키')
plt.show()

plt.scatter(X_train_class2['학년'], y_train_class2, color="red")
plt.plot(X_train_class2['학년'], class2_predictions, color="orange", linewidth=3)
plt.title('Class 2 Linear Regression')
#plt.xticks(np.arange(min(1), max(3)+1.0, 1.0))
plt.xlabel('학년')
plt.ylabel('키')
plt.show()





