import pandas as pd


# 通过字典创建 DataFrame
df = pd.DataFrame({'Column1': [1, 2, 3], 'Column2': [4, 5, 6]})
print(df)







print('\n-------------- 1.查看数据类型：使用 dtypes 属性 ----------------')
print('type(df): \n',type(df))
print()
print('df.dtypes:\n', df.dtypes)
 


print('\n-------------- 2.转换数据类型：使用 astype 方法 ----------------')
df['Column1'] = df['Column1'].astype('float64')
print('df[\'Column1\'].astype(\'float64\'): \n',  df['Column1'].dtype)