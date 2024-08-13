import pandas as pd
result = pd.read_json('data.js')
result1 = pd.read_csv('q.csv')

print(result.head(3))
print(type(result))
print("*************")
print(result1.head(3))
print(type(result1))
