import numpy as np
import pandas as pd

data = [290, 169, 183, 3, 227, 117, 159, 163, 240, 38, 23, 266, 96, 56, 280, 143, 246, 147, 226, 141, 290, 181, 0, 293, 260, 125, 29, 69, 184, 29, 2, 268, 202, 205, 271, 240, 151, 103, 204, 79, 154, 4, 229, 132, 138, 75, 31, 105, 62, 94, 285, 21, 289, 255, 69, 124, 178, 57, 106, 286, 52, 211, 58, 3, 147, 12, 273, 58, 246, 19]

data_array = np.array(data)
data_series = pd.Series(data)
print('(1)')
print("np average:", np.mean(data_array))
print("np variance:", np.var(data_array))
print("np standard deviation:", np.std(data_array))
print("np median:", np.median(data_array))
print("np 20%:" ,np.percentile(data_array, 20))
print("np 80%:" ,np.percentile(data_array, 80))

print("pd average:", data_series.mean())
print("pd variance:", data_series.var())
print("pd standard deviation:", data_series.std())
print("pd median:", data_series.median())
print("pd 20%:", data_series.quantile(0.20))
print("pd 80%:", data_series.quantile(0.80))

print('(2)')
print("average difference:", np.mean(data_array)-data_series.mean())
print("variance difference:", np.var(data_array)-data_series.var())
print("std difference:", np.std(data_array)-data_series.std())
print("median difference:", np.median(data_array)-data_series.median())
print("20% difference:", np.percentile(data_array, 20)-data_series.quantile(0.20))
print("80% difference:", np.percentile(data_array, 80)-data_series.quantile(0.80))
