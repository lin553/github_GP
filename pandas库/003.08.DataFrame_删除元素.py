import pandas as pd


# 通过字典创建 DataFrame
df = pd.DataFrame({'Column1': [1, 2, 3], 'Column2': [4, 5, 6], 'Name':['fuck1','fuck2','fuck3']})
print(df)



print('\n-------------- 1.删除列：使用 drop 方法 ----------------')
df_dropped = df.drop('Column1', axis=1)
print('df_dropped:\n',df_dropped,end='\n\n')
print('原式不变：\n',df)


print('\n-------------- 2.删除行：同样使用 drop 方法 ----------------')
df_dropped = df.drop(0)  # 删除索引为 0 的行
print('df_dropped:\n',df_dropped,end='\n\n')
print('原式不变：\n',df)