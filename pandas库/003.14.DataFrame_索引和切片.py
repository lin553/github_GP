# DataFrame 的合并与分割

import pandas as pd

s1 = pd.Series(['Alice', 'Bob', 'Charlie'])
s2 = pd.Series([25, 30, 35])
s3 = pd.Series(['New York', 'Los Angeles', 'Chicago'])
df = pd.DataFrame({'Name': s1, 'Age': s2, 'City': s3})
print(df)
# ===============================================================================



print('\n-------------- 1.提取多列 ----------------')
print('df[[\'Name\', \'Age\']]: \n', df[['Name', 'Age']])  




print('\n-------------- 2.切片行 ----------------')
print('df[1:3]:\n',df[1:3])      


print('\n-------------- 3.提取单列 ----------------')
print('df.loc[:, \'Name\']: \n', df.loc[:, 'Name'])  




print('\n-------------- 4.标签索引提取指定行列 ----------------')
print('df.loc[1:2, [\'Name\', \'Age\']]: \n', df.loc[1:2, ['Name', 'Age']])  



print('\n-------------- 5.位置索引提取指定列 ----------------')
print('df.iloc[:, 1:]: \n', df.iloc[:, 1:])