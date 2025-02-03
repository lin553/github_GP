# 访问 DataFrame 元素
    # 访问列：使用列名作为属性或通过 .loc[]、.iloc[] 访问，也可以使用标签或位置索引

import pandas as pd


# 通过字典创建 DataFrame
df = pd.DataFrame({'Column1': [1, 2, 3], 'Column2': [4, 5, 6], 'Name':['fuck1','fuck2','fuck3']})
print(df)


print('\n-------------- 通过列名访问 ----------------')
print(df['Column1'])

print('\n-------------- 通过属性访问 ----------------')
print(df.Name)     
   
print('\n-------------- 通过 .loc[] 访问 ----------------')
print(df.loc[:, 'Column1'])

print('\n-------------- 通过 .iloc[] 访问 ----------------')
print(df.iloc[:, 0])  # 假设 'Column1' 是第一列

print('\n-------------- 访问单个元素 ----------------')
print(df['Name'][0])
# print(df[0,1])        # 这个访问：失败

print('\n-------------- 通过行标签访问 ----------------')
print(df.loc[0, 'Column1'])