import pandas as pd
data= pd.read_csv('dirtydata.csv')

for i in data.index:
    if data.loc[i, 'Duration']>50:
        data.loc[i, 'Duration']=120
print(data)

# drop data 
# for i in data.index:
#     if data.loc[i, 'Duration']>50:
#         data.drop(i, inplace=True)
# print(data)
