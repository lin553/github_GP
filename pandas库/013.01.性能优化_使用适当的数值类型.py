print("\n\n--------------- 1. 使用适当的数值类型 ---------------")
# Pandas 默认的数值类型是 int64 和 float64，但对于大部分数据，这可能会浪费内存。可以使用更小的类型，如 int8, int16, float32 等。
    # 方法	        说明
    # astype()	    用于转换列的数据类型
    # downcast	    将数据类型降级，例如将 int64 降级为 int32 或 int16

import pandas as pd

df = pd.DataFrame({'A': [100, 200, 300, 400], 'B': [1000, 2000, 3000, 4000]})
print("源数据: \n", df.dtypes, "\n")

print("将列数据类型转换为较小的数据类型: ")
df['A'] = df['A'].astype('int16')
df['B'] = df['B'].astype('int32')
print(df.dtypes)

