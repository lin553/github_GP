import pandas as pd


# 通过字典创建 DataFrame
df = pd.DataFrame({'Column1': [1, 2, 3], 'Column2': [4, 5, 6]})
print(df)





print('\n-------------- 1.描述性统计：使用 .describe() 查看数值列的统计摘要 ----------------')
print('df.describe(): \n', df.describe())



print('\n-------------- 2.计算统计数据：使用聚合函数如 .sum()、.mean()、.max() 等。 ----------------')
print('df[\'Column1\'].sum(): ',df['Column1'].sum())
print()
print('df.mean(): \n',df.mean())