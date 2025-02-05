import pandas as pd

s1 = pd.Series(['Alice', 'Bob', 'Charlie'])
s2 = pd.Series([25, 30, 35])
s3 = pd.Series(['New York', 'Los Angeles', 'Chicago'])
df = pd.DataFrame({'Name': s1, 'Age': s2, 'City': s3})
print(df)

print('\n--------------- 1 ---------------')
print('形状: ',df.shape)     # 形状

print('\n--------------- 2 ---------------')
print('列名: ',df.columns)   # 列名

print('\n--------------- 3 ---------------')
print('索引: ',df.index)     # 索引

print('\n--------------- 4 ---------------')
print('前几行数据，默认是前 5 行: \n',df.head())    # 前几行数据，默认是前 5 行

print('\n--------------- 5 ---------------')
print('后几行数据，默认是后 5 行: \n',df.tail())    # 后几行数据，默认是后 5 行

print('\n--------------- 6 ---------------')
print('数据信息: \n',df.info())                   # 数据信息

print('\n--------------- 7 ---------------')
print('描述统计信息: \n',df.describe())           # 描述统计信息

print('\n--------------- 8 ---------------')
print('求平均值: \n', df['Age'].mean())           # 求平均值

print('\n--------------- 9 ---------------')
print('求和: \n', df['Age'].sum())                # 求和



# ========================== 完 ===========================