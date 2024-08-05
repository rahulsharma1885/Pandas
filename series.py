import pandas as pd
data= [3,4,5,6,8]
x= pd.Series(data)
print(x)
############################################
data1= [23, 56, 78, 76, 22, 78]
y= pd.Series(data1)
l= pd.Series(data1, index=['a','b','c','d','e','f'])
z= pd.Series(data1[3])
print(y)
print(l)
print(z)
######################################

data2= {'day1': 500, 'day2':100, 'day3':400}
result= pd.Series(data2)
result1= pd.Series(data2['day3'])
print(result)
print(result1)


