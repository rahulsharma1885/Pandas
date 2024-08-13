import pandas as pd 
data= pd.read_csv('dirtydata.csv')
x= data[['Date','Pulse']]
y=dict(x)
z= y.get('Date')
# print(x.head(5))

## wrong format

result = pd.to_datetime(data['Date'])
result1= result.dropna()
print(result1)


# print(z)
# print(type(y))
# print(type(z))
