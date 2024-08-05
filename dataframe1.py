import pandas as pd
# data= {'cal':[200, 500, 600], 'duration':[15, 20, 14]}
# result= pd.DataFrame(data)
# print(result)

data1 = {'days': ["day1", 'day2', 'day3', 'day4', 'day5', 'day6', 'day7'], 'Avg': ['20%', '40%', '30%', '70%', '60%', '30%', '90%']}
result1 = pd.DataFrame(data1)
result2=pd.DataFrame(result1['days'])    #1D
result3=pd.DataFrame(result1[['days', 'Avg']]) #2D 
print(result1)
print(result2)
print(result3)