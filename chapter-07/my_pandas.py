import pandas as pd
from pandas import DataFrame


df = DataFrame({'sales':[100, 150, 200, 250, 200, 150, 300, 400, 500, 100, 300, 200],
'quarters':'Q1 Q2 Q3 Q4'.split() * 3})
# df.to_csv('window-functions.csv')
# df
# df = pd.read_csv('window-functions.csv')


print(df)
display(df)


