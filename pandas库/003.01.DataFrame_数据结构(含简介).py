# Pandas 数据结构 - DataFrame
    # DataFrame 是 Pandas 中的另一个核心数据结构，类似于一个二维的表格或数据库中的数据表。
    # DataFrame 是一个表格型的数据结构，它含有一组有序的列，每列可以是不同的值类型（数值、字符串、布尔型值）。
    # DataFrame 既有行索引也有列索引，它可以被看做由 Series 组成的字典（共同用一个索引）。
    # DataFrame 提供了各种功能来进行数据访问、筛选、分割、合并、重塑、聚合以及转换等操作。
    # DataFrame 是一个非常灵活且强大的数据结构，广泛用于数据分析、清洗、转换、可视化等任务。

# DataFrame 特点：
    # 二维结构： DataFrame 是一个二维表格，可以被看作是一个 Excel 电子表格或 SQL 表，具有行和列。可以将其视为多个 Series 对象组成的字典。
    # 列的数据类型： 不同的列可以包含不同的数据类型，例如整数、浮点数、字符串或 Python 对象等。
    # 索引：DataFrame 可以拥有行索引和列索引，类似于 Excel 中的行号和列标。
    # 大小可变：可以添加和删除列，类似于 Python 中的字典。
    # 自动对齐：在进行算术运算或数据对齐操作时，DataFrame 会自动对齐索引。
    # 处理缺失数据：DataFrame 可以包含缺失数据，Pandas 使用 NaN（Not a Number）来表示。
    # 数据操作：支持数据切片、索引、子集分割等操作。
    # 时间序列支持：DataFrame 对时间序列数据有特别的支持，可以轻松地进行时间数据的切片、索引和操作。
    # 丰富的数据访问功能：通过 .loc、.iloc 和 .query() 方法，可以灵活地访问和筛选数据。
    # 灵活的数据处理功能：包括数据合并、重塑、透视、分组和聚合等。
    # 数据可视化：虽然 DataFrame 本身不是可视化工具，但它可以与 Matplotlib 或 Seaborn 等可视化库结合使用，进行数据可视化。
    # 高效的数据输入输出：可以方便地读取和写入数据，支持多种格式，如 CSV、Excel、SQL 数据库和 HDF5 格式。
    # 描述性统计：提供了一系列方法来计算描述性统计数据，如 .describe()、.mean()、.sum() 等。
    # 灵活的数据对齐和集成：可以轻松地与其他 DataFrame 或 Series 对象进行合并、连接或更新操作。
    # 转换功能：可以对数据集中的值进行转换，例如使用 .apply() 方法应用自定义函数。
    # 滚动窗口和时间序列分析：支持对数据集进行滚动窗口统计和时间序列分析。


# =================================================================
# DataFrame 构造方法如下：
# pandas.DataFrame(data=None, index=None, columns=None, dtype=None, copy=False)

# 参数说明：
    # data：DataFrame 的数据部分，可以是字典、二维数组、Series、DataFrame 或其他可转换为 DataFrame 的对象。如果不提供此参数，则创建一个空的 DataFrame。
    # index：DataFrame 的行索引，用于标识每行数据。可以是列表、数组、索引对象等。如果不提供此参数，则创建一个默认的整数索引。
    # columns：DataFrame 的列索引，用于标识每列数据。可以是列表、数组、索引对象等。如果不提供此参数，则创建一个默认的整数索引。
    # dtype：指定 DataFrame 的数据类型。可以是 NumPy 的数据类型，例如 np.int64、np.float64 等。如果不提供此参数，则根据数据自动推断数据类型。
    # copy：是否复制数据。默认为 False，表示不复制数据。如果设置为 True，则复制输入的数据。
          #  当你创建 DataFrame 时不复制数据（即 copy=False），DataFrame 和原始数据对象之间共享相同的数据存储。
          # 这意味着如果你后续修改了 DataFrame 中的数据，可能会无意中修改原始数据源。这对于调试和维护代码来说是一个潜在的风险。



# =================================================================
# 注意事项
    # DataFrame 是一种灵活的数据结构，可以容纳不同数据类型的列。
    # 列名和行索引可以是字符串、整数等。
    # DataFrame 可以通过多种方式进行数据选择、过滤、修改和分析。
    # 通过对 DataFrame 的操作，可以进行数据清洗、转换、分析和可视化等工作。


# =================================================================




import pandas as pd
import numpy as np


print('\n---------------------1.使用列表创建------------------------')
# 使用列表创建
data = [['Google', 10], ['Runoob', 12], ['Wiki', 13]]
# 创建DataFrame
df = pd.DataFrame(data, columns=['Site', 'Age'])
# 使用astype方法设置每列的数据类型
df['Site'] = df['Site'].astype(str)
df['Age'] = df['Age'].astype(float)
print(df)
print('\n df.dtypes: \n',df.dtypes)

print('\n---------------------2.使用字典创建------------------------')
# 使用字典创建
data = {'Site':['Google', 'Runoob', 'Wiki'], 'Age':[10, 12, 13]}
df = pd.DataFrame(data)
print(df)
print('\n df.dtypes: \n',df.dtypes)



print('\n---------------------3.使用 ndarrays 创建------------------------')
"""
    以下实例使用 ndarrays 创建，ndarray 的长度必须相同， 如果传递了 index，则索引的长度应等于数组的长度。
    如果没有传递索引，则默认情况下，索引将是range(n)，其中n是数组长度。
    ndarrays 可以参考：NumPy Ndarray 对象
"""

# 创建一个包含网站和年龄的二维ndarray
ndarray_data = np.array([
    ['Google', 10],
    ['Runoob', 12],
    ['Wiki', 13]
])
# 使用DataFrame构造函数创建数据帧
df = pd.DataFrame(ndarray_data, columns=['Site', 'Age'])
# 打印数据帧
print(df)



print('\n---------------------4.使用字典创建------------------------')
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)
print ('含空值：NaN\n', df)




print('\n---------------------5.loc 属性-----------------------')
# Pandas 可以使用 loc 属性返回指定行的数据，如果没有设置索引，第一行索引为 0，第二行索引为 1，以此类推：
# 注意：返回结果其实就是一个 Pandas Series 数据。
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
# 数据载入到 DataFrame 对象
df = pd.DataFrame(data)
# 返回第一行
print('df.loc[0]:第一行:\n',df.loc[0], '\n')
# 返回第二行
print('df.loc[1]:第二行:\n',df.loc[1], '\n')




print('\n---------------------6.loc 属性：返回多行数据，使用 [[ ... ]] 格式，... 为各行的索引，以逗号隔开：-----------------------')
# 注意：返回结果其实就是一个 Pandas DataFrame 数据。
data = {
  "calories": [420, 380, 390,360,250,500],
  "duration": [50, 40, 45, 60, 55, 35]
}
# 数据载入到 DataFrame 对象
df = pd.DataFrame(data)
# 返回第一行和第二行
print('df.loc[[0, 1]]:返回第一行和第二行: \n',df.loc[[0, 1]],'\n')



print('\n---------------------7.指定索引值-----------------------')
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df)
print('\n df.loc[\'day1\']: 返回指定索引行: \n', df.loc['day1'])