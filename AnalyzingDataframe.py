import pandas as pd
data= pd.read_csv('data.csv')
result= data.head(10) #top 10 data 
result1= data.tail(10)# bottom to 20 data
print(result)
print(result1)