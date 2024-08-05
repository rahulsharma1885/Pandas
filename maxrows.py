import pandas as pd

# Set the maximum number of rows to display
pd.set_option('display.max_rows', 9999)

data = pd.read_csv('data.csv')

print(pd.options.display.max_rows == 9999)
 
print(data)
