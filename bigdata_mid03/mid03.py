import pandas as pd
import numpy as np

df1_data = np.ones((6, 7))

df1 = pd.DataFrame(df1_data, index=list('abcdef'), columns=list('ABCDEFG'))

df2_data = np.ones((7, 6))

df2 = pd.DataFrame(df2_data, index=list('abcdefg'), columns=list('ABCDEF'))

df3 = df1 + df2

df3.iloc[0:5 , 0:5] = np.nan
df3.iloc[0:3, 0:3] = 3.0
df3.loc['a', 'A'] =np.nan
print(df3)


