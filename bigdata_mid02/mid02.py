import numpy as np
import pandas as pd

data = pd.read_csv("kbo_baseball_test.csv")

data['Rating'] = data['Win'] / (data['Win'] + data['Draw']+ data['Lose'])
b = data.sort_values(by='Rating', ascending=False)

print("Top 5 of Winning Percentage")

for i in range(0,5):
    print("{}, {}".format(b["Team"][i], b["Rating"][i]))