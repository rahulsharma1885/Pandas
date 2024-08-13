import pandas as pd

## Weong Data
data = pd.read_csv('dirtydata.csv')
data.loc[7, 'Duration']= 45  # 7 is row and Duration is column
# print(data)

# wrong Data Format
result = pd.read_csv('dirtydata.csv')
result['Date']= pd.to_datetime(data['Date'])
# print(result)

### remove wrong data
result = pd.read_csv('dirtydata.csv')
result['Date']= pd.to_datetime(data['Date'])
result.dropna(subset= ['Date'], inplace=True)
print(result)