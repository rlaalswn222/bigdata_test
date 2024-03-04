import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = 'NanumGothic'

csv_file_path = 'student_health_2.csv'

df = pd.read_csv(csv_file_path, encoding='utf-8')

grade_counts = df['학년'].value_counts().sort_index()

# 학년 별 학생 수
plt.bar(grade_counts.index, grade_counts.values, color='lightpink')
plt.xlabel('학년')
plt.ylabel('학생 수')
plt.title('각 학년 별 학생 수')
plt.xticks(grade_counts.index, ['1학년', '2학년', '3학년', '4학년', '5학년', '6학년'])

plt.show()

#학년 별 평균 키
average_height_per_grade = df.groupby('학년')['키'].describe()[['mean']].sort_index()

plt.bar(average_height_per_grade.index, average_height_per_grade['mean'], color='red' )
plt.xlabel('학년')
plt.ylabel('평균 키')
plt.title('학년 별 평균 키')
plt.show()

#학년 별 평균 몸무게
average_weight_per_grade = df.groupby('학년')['몸무게'].describe()[['mean']].sort_index()
plt.bar(average_weight_per_grade.index, average_weight_per_grade['mean'], color='orange' )
plt.xlabel('학년')
plt.ylabel('평균 몸무게')
plt.title('학년 별 평균 몸무게')
plt.show()

#학년 별 평균 수축기 혈압
average_systolic_blood_pressure_per_grade = df.groupby('학년')['수축기'].describe()[['mean']].sort_index()
plt.bar(average_systolic_blood_pressure_per_grade.index, average_systolic_blood_pressure_per_grade['mean'], color='yellow' )
plt.xlabel('학년')
plt.ylabel('평균 수축기 혈압')
plt.title('학년 별 평균 수축기 혈압')
plt.xticks(np.arange(min(average_systolic_blood_pressure_per_grade.index), max(average_systolic_blood_pressure_per_grade.index)+1.0, 1.0))
plt.show()

#학년 별 평균 이완기 혈압
average_diastolic_blood_pressure_per_grade = df.groupby('학년')['이완기'].describe()[['mean']].sort_index()
plt.bar(average_diastolic_blood_pressure_per_grade.index, average_diastolic_blood_pressure_per_grade['mean'], color='lightgreen' )
plt.xlabel('학년')
plt.ylabel('평균 이완기 혈압')
plt.title('학년 별 평균 이완기 혈압')
plt.xticks(np.arange(min(average_diastolic_blood_pressure_per_grade.index), max(average_diastolic_blood_pressure_per_grade.index)+1.0, 1.0))
plt.show()