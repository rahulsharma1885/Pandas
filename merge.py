import pandas as pd
# data1= pd.DataFrame({'a':[1,2,3], 'b':[10,11,12,]})
# data2= pd.DataFrame({'a':[1,2,3], 'c':[10,11,12]})

# data1= pd.DataFrame({'a':[1,2,3, 4], 'b':[10,11,12,13]})
# data2= pd.DataFrame({'a':[1,2,3,5], 'c':[10,11,12,14]})

# result= pd.merge(data1, data2, on="a")
# print(result)

#################################################################################

data1= pd.DataFrame({'a':[1,2,3, 4], 'b':[10,11,12,13]})
data2= pd.DataFrame({'a':[1,2,3,5], 'c':[10,11,12,14]})

# result= pd.merge(data1, data2, how='inner', indicator=True)
result= pd.merge(data1, data2, how='outer', indicator=True)
print(result)

################################################################################

data3= pd.DataFrame({'a':[1,2,3, 4], 'b':[10,11,12,13]})
data4= pd.DataFrame({'a':[1,2,3,5], 'c':[10,11,12,14]})

# result= pd.merge(data1, data2, how='inner', indicator=True)
result2= pd.merge(data3, data4, left_index=True, right_index=True, suffixes=('name', 'python'))
print(result2)

