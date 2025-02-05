# 多重索引（MultiIndex）
    # 可以在 DataFrame 或 Series 中处理复杂的数据结构，尤其适用于层次化的数据。通过多重索引，我们能够对数据进行分组、选择、切片以及聚合等操作。
# ============================================================================


print("\n\n-------------- 1 创建多重索引: 方法1: pd.MultiIndex.from_tuples() 使用元组来创建多重索引 ---------------")
# 可以通过 pd.MultiIndex.from_tuples()、pd.MultiIndex.from_product() 或者 set_index() 方法来创建多重索引。
    # 方法 1: pd.MultiIndex.from_tuples(): 使用元组来创建多重索引，每个元组对应一个索引层级。
        # 参数	        说明
        # tuples	    每个元组对应一个索引值
        # names	        每个索引级别的名称（可选）

import pandas as pd

index_tuples = [('A', 1), ('A', 2), ('B', 1), ('B', 2)]     # 创建元组
df = pd.DataFrame(index_tuples)
print("源数据：\n", df,"\n")

multi_index = pd.MultiIndex.from_tuples(index_tuples, names=['Letter', 'Number'])  # 创建多重索引
print("多重索引本身: \n",multi_index,"\n")
df1 = pd.DataFrame(multi_index)
print("多重索引本身转成DataFrame格式后: \n",df1,"\n")

df2 = pd.DataFrame({'Value': [10, 20, 30, 40]}, index=multi_index)   # 创建 DataFrame
print("执行完成后新数据: 已加载多重索引与value数据: ")
print(df2)




print("\n\n-------------- 2 创建多重索引: 方法 2: pd.MultiIndex.from_product() 使用多个列表的笛卡尔积来创建多重索引 ---------------")
# 使用多个列表的笛卡尔积来创建多重索引，适合用于数据维度较多的情况。
    # 参数	        说明
    # iterables	    多个列表或数组
    # names	        每个索引级别的名称（可选）

import pandas as pd

index_values = [['A', 'B'], [1, 2]]     # 创建多个列表
multi_index = pd.MultiIndex.from_product(index_values, names=['Letter', 'Number'])      # 创建多重索引
df = pd.DataFrame({'Value': [10, 20, 30, 40]}, index=multi_index)       # 创建 DataFrame
print(df)





print("\n\n-------------- 3 创建多重索引: 方法 3: 使用 set_index() 创建多重索引，适用于从已有的数据创建多重索引 ---------------")
# set_index() 方法可以将 DataFrame 的列转换为多重索引，适用于从已有的数据创建多重索引。
    # 参数	    说明
    # keys	    用作索引的列名（可以是单列或多列）

import pandas as pd

data = {
    'Letter': ['A', 'A', 'B', 'B'],
    'Number': [1, 2, 1, 2],
    'Value': [10, 20, 30, 40]
}
df = pd.DataFrame(data)
print("源数据：\n", df,"\n")

df.set_index(['Letter', 'Number'], inplace=True)    # 设置多重索引
print("执行完成后新数据：")
print(df)




print("\n\n-------------- 4.多重索引的操作: 访问多重索引数据, 使用 loc[] 选择数据 ---------------")
# 访问多重索引数据
    # 可以通过层级索引来访问数据。通过 loc[] 或 xs()（cross-section）可以方便地进行数据选择。
    # 使用 loc[] 选择数据:

import pandas as pd
data = {
    'Letter': ['A', 'A', 'B', 'B'],
    'Number': [1, 2, 1, 2],
    'Value': [10, 20, 30, 40]
}
df = pd.DataFrame(data)
print("源数据：\n", df,"\n")

df.set_index(['Letter', 'Number'], inplace=True)        # 设置多重索引
print("执行完成后新数据：")
print(df.loc['A', 1])       # 选择 'A' 类别，所有 'Number' 为 1 的数据






print("\n\n-------------- 5.多重索引的操作: 访问多重索引数据, 使用 xs() 获取交叉数据 ---------------")
# xs() 方法可以在多重索引中选择指定级别的切片。
import pandas as pd
data = {
    'Letter': ['A', 'A', 'B', 'B'],
    'Number': [1, 2, 1, 2],
    'Value': [10, 20, 30, 40]
}
df = pd.DataFrame(data)
print("源数据：\n", df,"\n")
df.set_index(['Letter', 'Number'], inplace=True)        # 设置多重索引
# 使用 xs 获取 'Number' 为 1 的所有数据
print(df.xs(1, level='Number'))




print("\n\n-------------- 6.多重索引的切片 .loc[] 方法 ---------------")
# Pandas 支持对多重索引进行切片操作，允许通过索引级别选择不同的子集。
import pandas as pd
data = {
    'Letter': ['A', 'A', 'B', 'B'],
    'Number': [1, 2, 1, 2],
    'Value': [10, 20, 30, 40]
}
df = pd.DataFrame(data)
print("源数据：\n", df,"\n")
df.set_index(['Letter', 'Number'], inplace=True)        # 设置多重索引

print("选择 Letter 为 'A' 的所有数据:")
print(df.loc['A'])






print("\n\n-------------- 7.排序多重索引 sort_index() 方法 ---------------")
# Pandas 的 sort_index() 方法支持对多重索引进行排序。
import pandas as pd
data = {
    'Letter': ['A', 'A', 'B', 'B'],
    'Number': [1, 2, 1, 2],
    'Value': [10, 20, 30, 40]
}
df = pd.DataFrame(data)
print("源数据：\n", df,"\n")
df.set_index(['Letter', 'Number'], inplace=True)        # 设置多重索引

print("按照多重索引排序:")
df_sorted = df.sort_index(level=['Letter', 'Number'], ascending=[True, False])  # ascending=[True, False]：第一个索引是升序，第二个索引是降序
print(df_sorted)





print("\n\n-------------- 8.多重索引聚合 groupby() ---------------")
# 多重索引结合 groupby() 可以进行强大的聚合操作，适用于复杂数据的统计分析。
import pandas as pd
data = {
    'Letter': ['A', 'A', 'B', 'B'],
    'Number': [1, 2, 1, 2],
    'Value': [10, 20, 30, 40]
}
df = pd.DataFrame(data)
print("源数据：\n", df,"\n")
df.set_index(['Letter', 'Number'], inplace=True)        # 设置多重索引

print("使用 groupby 对多重索引进行聚合:")
df_grouped = df.groupby(['Letter', 'Number']).sum()
print(df_grouped)






print("\n\n-------------- 9.重设索引 reset_index() 将多重索引重置为普通的列 ---------------")
# 可以使用 reset_index() 方法将多重索引重置为普通的列。
import pandas as pd
data = {
    'Letter': ['A', 'A', 'B', 'B'],
    'Number': [1, 2, 1, 2],
    'Value': [10, 20, 30, 40]
}
df = pd.DataFrame(data)
print("源数据：\n", df,"\n")

df.set_index(['Letter', 'Number'], inplace=True)        # 设置多重索引
print("设置完索引后的数据: ")
print(df,"\n")

print("重设索引: 将多重索引重置为普通的列 ")
df_reset = df.reset_index()
print(df_reset)




print("\n\n-------------- 10.多重索引中的缺失值可以通过 fillna() 或 dropna() 来处理，类似于普通索引 ---------------")
import pandas as pd
# 示例数据中引入缺失值
data = {
    'Letter': ['A', 'A', 'B', 'B'],
    'Number': [1, 2, 1, 2],
    'Value': [10, None, 30, 40]
}
df = pd.DataFrame(data)
print("源数据: “None” 被DataFrame自动格式化为 “NaN” 了 \n", df,"\n")

df.set_index(['Letter', 'Number'], inplace=True)     # 设置多重索引     
                                 # inplace：布尔值，默认为 False。如果设置为 True，则在原DataFrame上进行操作而不返回新的DataFrame
print("设置完索引后的数据: ")
print(df,"\n")

print("填充缺失值后数据：NaN 变成 0 了")
df_filled = df.fillna(0)
print(df_filled)
print()

print("重设索引: 将多重索引重置为普通的列 ")
df_reset = df_filled.reset_index()
print(df_reset)


# ========================== 完 ===========================