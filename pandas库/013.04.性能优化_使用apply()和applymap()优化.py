

print("\n\n--------------- 4.使用 apply() 和 applymap() 优化 ---------------")
# Pandas 提供了 apply() 和 applymap() 方法，它们可以让你在数据框架中按行或按列应用函数，能够比循环更高效。

import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8]})
df['C'] = df['A'] + df['B']     # 使用向量化操作，避免使用循环
print("源数据: \n", df, "\n")

print("使用 apply() 在列上应用自定义函数: ")
df['D'] = df['A'].apply(lambda x: x ** 2)
print(df)

