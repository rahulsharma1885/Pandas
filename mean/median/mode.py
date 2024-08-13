import pandas as pd

# data_with_nan = pd.DataFrame({
#     'A': [20, 20, 30, None, 50],
#     'B': [5, None, 25, 35, 45]
# })
# result= data_with_nan.mean()
# print(result)


data = pd.read_csv('dirtydata.csv')

### mean
result= data.mean()
result= data['Calories'].mean() # all values divided by number of values


#### median

# result3= data.median()

result2= pd.DataFrame([10,20, 30, 40])
result3= result2.median()

# print(round(result3))
# print(data)

#### mode
# result4= data.mode()
result4= data['Maxpulse'].mode()[0]
print(result4)
 