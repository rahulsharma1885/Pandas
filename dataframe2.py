import pandas as pd
data= pd.read_csv('data.csv')
data1= pd.read_json('data.js')

print(data.to_string())

print(data1.to_string())  #json_data