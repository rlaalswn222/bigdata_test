import pandas as pd

df = pd.read_csv('attraction_list_1.csv', encoding="utf-8")

filter_df = df[(df["관광지별"] == "유료관광지") & (df["자치구별"] != "합계")]
filter_df = filter_df.fillna(0)
print(filter_df)