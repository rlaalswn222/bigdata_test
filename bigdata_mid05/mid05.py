import numpy as np
import pandas as pd

data = pd.read_csv("seoul_ems_test.csv")

years = data.columns[1:7]

data['Check_Total'] = data[years].sum(axis = 1)

data['Total_Match'] = data['Total'] == data['Check_Total']
data['Gap'] = data['Total'] - data['Check_Total']
print('(1)')
print(data[['Region ID', 'Total', 'Check_Total', 'Total_Match']])

print('(2)')
print(data[data['Total_Match'] == False][['Region ID', 'Total', 'Check_Total', 'Gap']])