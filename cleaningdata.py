import pandas as pd

# def result():
#     return pd.read_csv('testpassdata.csv')

# result1=result()
# print(result1)

data= pd.read_csv('dirtydata.csv')

result= data.dropna()
result= data['Calories'].dropna()

# result1= data.fillna('rahul') # (130) # all column replace 
# result1= data['Calories'].fillna(23888) # particular column replace NaN 


print(result.to_string())
# print(result1.to_string())
    
