import pandas as pd

# 通过字典创建 DataFrame
df = pd.DataFrame({'Column1': [1, 2, 3], 'Column2': [4, 5, 6]})
print('通过字典创建 DataFrame: \n', df)


print('\n-------------------------- 从列表的列表创建：外层列表代表行，内层列表代表列 ---------------------------')
df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=['Column1', 'Column2', 'Column3'])
print(df)


print('\n-------------------------- 从 NumPy 数组创建：提供一个二维 NumPy 数组 ---------------------------')
import numpy as np
df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(df)


print('\n-------------------------- 从 Series 创建 DataFrame：通过 pd.Series() 创建 ---------------------------')
s1 = pd.Series(['Alice', 'Bob', 'Charlie'])
s2 = pd.Series([25, 30, 35])
s3 = pd.Series(['New York', 'Los Angeles', 'Chicago'])
df = pd.DataFrame({'Name': s1, 'Age': s2, 'City': s3})
print(df)




# ========================== 完 ===========================