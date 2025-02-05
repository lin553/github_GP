# Pandas 性能优化
    # Pandas 性能优化涉及多个方面，包括数据类型优化、避免不必要的循环、使用向量化操作、优化索引以及分块加载大数据集等方法。


# =================================================================
# 下面我们将详细介绍 Pandas 性能优化的几种方法。

    # 使用适当的数据类型
        # Pandas 中的数据类型（dtype）直接影响内存使用和计算速度。合理选择数据类型可以显著减少内存占用和加速计算。

    # 使用向量化操作而非循环
        # Pandas 的最大优势之一就是其能够利用向量化操作进行快速的批量运算。在 Pandas 中，尽量避免使用 Python 的原生循环，
        # 应该使用 Pandas 内置的函数，这样可以利用底层的优化进行快速计算。

    # 使用 apply() 和 applymap() 优化
        # Pandas 提供了 apply() 和 applymap() 方法，它们可以让你在数据框架中按行或按列应用函数，能够比循环更高效。
    
    # 使用合适的索引
        # Pandas 的索引可以提高数据的查找速度，尤其是在需要进行多次查找或数据合并时，索引可以显著提升效率。对于大数据集，
        # 确保使用适当的索引并减少不必要的索引操作可以提高性能。
 
    # 使用分块加载大数据集
        # 当数据集过大时，加载整个数据集会占用大量内存，甚至导致内存溢出。此时，可以通过分块读取数据来减小内存压力。
        # Pandas 提供了 chunksize 参数，允许在读取 CSV 或 Excel 文件时分块加载数据。
    
    # 通过 numba 加速计算
        # numba 是一个 JIT 编译器，可以将 Python 代码加速。通过将数据处理的代码加速，可以显著提高性能。特别是对于循环、
        # 数值计算等计算密集型操作，numba 可以极大地提高速度。

    # 避免链式赋值
        # 链式赋值（chained assignment）是 Pandas 中常见的性能陷阱之一。它可能导致不必要的副作用，并且通常会减慢执行速度。最好使用
        # 明确的赋值方式，避免在同一行中进行多次赋值。

    # 合并操作优化
        # 当需要将多个 DataFrame 合并时，使用 merge() 或 concat() 时需要注意优化合并操作，特别是在处理大数据集时。可以
        # 使用 on 和 how 参数明确指定合并方式，避免不必要的计算。
# =====================================================================




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




print("\n\n--------------- 2. 对字符数据使用 category 类型 ---------------")
# 对于具有重复值的字符串列，可以使用 category 类型来减少内存消耗。category 类型在内存中存储的是整数索引，而不是字符串本身。

import pandas as pd
df = pd.DataFrame({'Category': ['A', 'B', 'A', 'C', 'B', 'A']})
print("源数据: \n", df.dtypes, "\n")

print("使用 category 类型: ")
df['Category'] = df['Category'].astype('category')
print(df.dtypes)




print("\n\n--------------- 3.使用向量化操作而非循环,最大优势之一就是其能够利用向量化操作进行快速的批量运算 ---------------")
# Pandas 的最大优势之一就是其能够利用向量化操作进行快速的批量运算。在 Pandas 中，尽量避免使用 Python 的原生循环，
# 应该使用 Pandas 内置的函数，这样可以利用底层的优化进行快速计算。

import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8]})
print("源数据: \n", df, "\n")

print("使用向量化操作，避免使用循环: ")
df['C'] = df['A'] + df['B']
print(df)





print("\n\n--------------- 4.使用 apply() 和 applymap() 优化 ---------------")
# Pandas 提供了 apply() 和 applymap() 方法，它们可以让你在数据框架中按行或按列应用函数，能够比循环更高效。

import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8]})
df['C'] = df['A'] + df['B']     # 使用向量化操作，避免使用循环
print("源数据: \n", df, "\n")

print("使用 apply() 在列上应用自定义函数: ")
df['D'] = df['A'].apply(lambda x: x ** 2)
print(df)





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





print("\n\n--------------- 6.使用分块加载大数据集: chunksize 参数，允许在读取 CSV 或 Excel 文件时分块加载数据 ---------------")
# 当数据集过大时，加载整个数据集会占用大量内存，甚至导致内存溢出。此时，可以通过分块读取数据来减小内存压力。
# Pandas 提供了 。chunksize 参数，允许在读取 CSV 或 Excel 文件时分块加载数据

import pandas as pd

# # 创建索引并进行查找
# df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8]})
# print("源数据: \n", df, "\n")

# 分块读取 CSV 文件
chunksize = 10000
for chunk in pd.read_csv('./pandas库/013.01.csv', chunksize=chunksize):
    print(chunk)        # 对每个数据块进行处理




print("\n\n--------------- 7.通过 numba 加速计算 ---------------")
# numba 是一个 JIT 编译器，可以将 Python 代码加速。通过将数据处理的代码加速，可以显著提高性能。特别是对于循环、
    # 数值计算等计算密集型操作，numba 可以极大地提高速度。

import numba
import pandas as pd

@numba.jit      # 装饰器
def calculate_square(x):
    return x ** 2

# 使用 numba 加速计算
df = pd.DataFrame({'A': [1, 2, 3, 4]})
df['B'] = df['A'].apply(calculate_square)
print(df)





print("\n\n--------------- 8.避免链式赋值 ---------------")
# 链式赋值（chained assignment）是 Pandas 中常见的性能陷阱之一。它可能导致不必要的副作用，并且通常会减慢执行速度。
# 最好使用明确的赋值方式，避免在同一行中进行多次赋值。

print("df['A'][df['A'] > 2] = 0 : 链式赋值：可能引发警告并影响性能")
df['A'][df['A'] > 2] = 0        # 链式赋值：可能引发警告并影响性能

print("df.loc[df['A'] > 2, 'A'] = 0 : 正确赋值方法")
df.loc[df['A'] > 2, 'A'] = 0    # 正确赋值方法






print("\n\n--------------- 9.合并操作优化 ---------------")
# 当需要将多个 DataFrame 合并时，使用 merge() 或 concat() 时需要注意优化合并操作，特别是在处理大数据集时。可以
# 使用 on 和 how 参数明确指定合并方式，避免不必要的计算。

import pandas as pd

# 使用合适的合并方式
df1 = pd.DataFrame({'ID': [1, 2, 3], 'Value': ['A', 'B', 'C']})
df2 = pd.DataFrame({'ID': [1, 2, 3], 'Value': ['X', 'Y', 'Z']})

print("使用 on 参数进行合并(明确指定合并方式，避免不必要的计算):   merged_df = pd.merge(df1, df2, on='ID', how='inner')")
merged_df = pd.merge(df1, df2, on='ID', how='inner')
print(merged_df)