import pandas as pd
data= {
    'name':["rahul", 'mohit', 'rohit'],
    'Qualification':['b.tech', 'm.tech', 'bca'],
    'city':['meerut', 'noida', 'delhi']
}

result= pd.DataFrame(data)
# result1= result.iloc[1:, [2]]
print(result)
# print(result.info())
# print(result1)