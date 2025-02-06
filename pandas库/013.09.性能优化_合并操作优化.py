



print("\n\n--------------- 9.合并操作优化 ---------------")
# 当需要将多个 DataFrame 合并时，使用 merge() 或 concat() 时需要注意优化合并操作，特别是在处理大数据集时。可以
# 使用 on 和 how 参数明确指定合并方式，避免不必要的计算。

import pandas as pd

# 使用合适的合并方式
df1 = pd.DataFrame({'ID': [1, 2, 3], 'Value': ['A', 'B', 'C']})
df2 = pd.DataFrame({'ID': [1, 2, 3], 'Value': ['X', 'Y', 'Z']})
print("源数据：\n df1:\n",df1,"\n df2:\n",df2, "\n\n", end="")

print("使用 on 参数进行合并(明确指定合并方式，避免不必要的计算):   merged_df = pd.merge(df1, df2, on='ID', how='inner')")
merged_df = pd.merge(df1, df2, on='ID', how='inner')
print(merged_df)

