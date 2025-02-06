

print("\n\n--------------- 5.使用合适的索引 ---------------")
# Pandas 的索引可以提高数据的查找速度，尤其是在需要进行多次查找或数据合并时，索引可以显著提升效率。对于大数据集，
# 确保使用适当的索引并减少不必要的索引操作可以提高性能。

import pandas as pd
# 创建索引并进行查找
df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8]})
print("源数据: \n", df, "\n")

df.set_index('A', inplace=True)
print("索引的数据: ")
print(df, "\n")

print("通过索引快速查找: ")
print(df.loc[2])


