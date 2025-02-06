print("\n\n--------------- 2. 对字符数据使用 category 类型 ---------------")
# 对于具有重复值的字符串列，可以使用 category 类型来减少内存消耗。category 类型在内存中存储的是整数索引，而不是字符串本身。

import pandas as pd
df = pd.DataFrame({'Category': ['A', 'B', 'A', 'C', 'B', 'A']})
print("源数据: \n", df.dtypes, "\n")

print("使用 category 类型: ")
df['Category'] = df['Category'].astype('category')
print(df.dtypes)

