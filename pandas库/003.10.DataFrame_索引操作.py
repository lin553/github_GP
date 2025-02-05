import pandas as pd


# 通过字典创建 DataFrame
df = pd.DataFrame({'Column1': [1, 2, 3], 'Column2': [4, 5, 6]})
print(df)







print('\n-------------- 1.重置索引：使用 .reset_index() ----------------')
df_1 = df.reset_index(drop=False)
print('df.reset_index(drop=False): \n', df_1)
df_2 = df.reset_index(drop=True)
print('\n df.reset_index(drop=True): \n', df_2)
print('\n df: \n', df)

print('\n-------------- 2.设置索引：使用 .set_index() ----------------')
print('df.set_index(\'Column1\'): \n', df.set_index('Column1'))
print('\n 原df:\n',df)



print('\n-------------- 3.DataFrame 的布尔索引:  使用布尔表达式, 根据条件过滤 DataFrame ----------------')
print('df[df[\'Column1\'] > 2]: \n',df[df['Column1'] > 2])




# ========================== 完 ===========================