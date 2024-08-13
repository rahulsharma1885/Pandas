import pandas as pd
# df= pd.DataFrame({"a":[4,5,6], "b":[7,8,9], "c":[10,11,12]})
# df = pd.DataFrame({"a":[2,3,4], "b":[5,6,7], "c":[8,9,10]}, index=[1,2,3])
# print(df)

#################

# creating database with multiple indexs

df= pd.DataFrame({"a":[2,3,4], "b":[5,6,7], "c":[8,9,10]}, index=pd.MultiIndex.from_tuples([('R',1),('R', 2),('s',3)], names=['rahul', 'mohit']))

print(df)