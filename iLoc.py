import pandas as pd
data= pd.read_csv('dirtydata.csv')

result= data.iloc[::, ::]
result= data.iloc[:3, :2]
# result= data.iloc[1:, 3:]
print(result)