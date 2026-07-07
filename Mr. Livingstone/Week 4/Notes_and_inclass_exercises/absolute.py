import pandas as pd
import numpy as np

df = pd.read_csv('C:\\Users\\pc\\OneDrive\\Desktop\\Recess Assignments\\Kyomujuni-Edinah-recess-2.3\\Mr.Jeff\\Week 4\\Notes_and_inclass_exercises\\ecommerce_bigdata.csv')

df = df.select_dtypes(include=[np.number])

max_abs = np.max(np.abs(df), axis=0)
print(f"Maximum absolute values for each column:\n{max_abs}")

scaled_df = df / max_abs
print(f"Scaled DataFrame:\n{scaled_df.head()}")