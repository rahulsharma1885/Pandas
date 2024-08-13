import pandas as pd
data= pd.read_csv('dirtydata.csv')

data.drop_duplicates(inplace=True)
# data.drop_duplicates(subset='Duration', inplace=True)

print(data)

# print(data.duplicated()) # 