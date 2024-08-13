import pandas as pd
import numpy as np

# Create a sample DataFrame with missing values
data = {
    'Time': [1, 2, 3, 4, 5],
    'Temperature': [22.1, np.nan, 23.5, np.nan, 25.0],
    'Humidity': [45, 47, np.nan, np.nan, 50]
}

df = pd.DataFrame(data)

print("Original DataFrame with Missing Values:")
print(df)

# Interpolate missing values using linear method
df1 = df.interpolate(method='linear')

print("\nDataFrame after Linear Interpolation:")
print(df1)
