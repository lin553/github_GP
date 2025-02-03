# DataFrame 方法
# DataFrame 的常用操作和方法如下表所示：

# 方法名称	                    功能描述
# head(n)	                    返回 DataFrame 的前 n 行数据（默认前 5 行）
# tail(n)	                    返回 DataFrame 的后 n 行数据（默认后 5 行）
# info()	                    显示 DataFrame 的简要信息，包括列名、数据类型、非空值数量等
# describe()	                返回 DataFrame 数值列的统计信息，如均值、标准差、最小值等
# shape	                        返回 DataFrame 的行数和列数（行数, 列数）
# columns	                    返回 DataFrame 的所有列名
# index	                        返回 DataFrame 的行索引
# dtypes	                    返回每一列的数值数据类型
# sort_values(by)	            按照指定列排序
# sort_index()	                按行索引排序
# dropna()	                    删除含有缺失值（NaN）的行或列
# fillna(value)	                用指定的值填充缺失值
# isnull()	                    判断缺失值，返回一个布尔值 DataFrame
# notnull()	                    判断非缺失值，返回一个布尔值 DataFrame
# loc[]	                        按标签索引选择数据
# iloc[]	                    按位置索引选择数据
# at[]	                        访问 DataFrame 中单个元素（比 loc[] 更高效）
# iat[]	                        访问 DataFrame 中单个元素（比 iloc[] 更高效）
# apply(func)	                对 DataFrame 或 Series 应用一个函数
# applymap(func)	            对 DataFrame 的每个元素应用函数（仅对 DataFrame）
# groupby(by)	                分组操作，用于按某一列分组进行汇总统计
# pivot_table()	                创建透视表
# merge()	                    合并多个 DataFrame（类似 SQL 的 JOIN 操作）
# concat()	                    按行或按列连接多个 DataFrame
# to_csv()	                    将 DataFrame 导出为 CSV 文件
# to_excel()	                将 DataFrame 导出为 Excel 文件
# to_json()	                    将 DataFrame 导出为 JSON 格式
# to_sql()                  	将 DataFrame 导出为 SQL 数据库
# query()	                    使用 SQL 风格的语法查询 DataFrame
# duplicated()	                返回布尔值 DataFrame，指示每行是否是重复的
# drop_duplicates()         	删除重复的行
# set_index()	                设置 DataFrame 的索引
# reset_index()	                重置 DataFrame 的索引
# transpose()	                转置 DataFrame（行列交换）
# =================================================================


import pandas as pd

# 创建 DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
df = pd.DataFrame(data)



# 查看前两行数据
print('\n查看前两行数据   df.head(2): \n',df.head(2))


print('\n------------------------1---------------------------')
# 查看 DataFrame 的基本信息
print('查看 DataFrame 的基本信息  df.info() : \n',df.info())


print('\n------------------------2---------------------------')
# 获取描述统计信息
print('获取描述统计信息  df.describe(): \n',df.describe())


print('\n------------------------3---------------------------')
# 按年龄排序
df_sorted = df.sort_values(by='Age', ascending=False)
print('按年龄排序: \n',df_sorted)


print('\n------------------------3---------------------------')
# 选择指定列
print('选择指定列  df[[\'Name\', \'Age\']] : \n',df[['Name', 'Age']])





print('\n------------------------4---------------------------')
# 按索引选择行
print('按索引选择行  df.iloc[1:3] : \n',df.iloc[1:3])  # 选择第二到第三行（按位置）
print('\n按索引选择行  df.iloc[0:1] : \n',df.iloc[0:1])  # 选择第0-1行（按位置）
print('\n按索引选择行  df.iloc[2] : \n',df.iloc[2])  # 选择第2行（按位置）


print('\n------------------------5---------------------------')
# 按标签选择行
print('按标签选择行  df.loc[1:2] : \n',df.loc[1:2])  # 选择第二到第三行（按标签）
print('\n按标签选择行  df.loc[0:1] : \n',df.loc[0:1])  # 选择第0-1行（按标签）
print('\n按标签选择行  df.loc[2] : \n',df.loc[2])  # 选择第2行（按标签）





print('\n------------------------6---------------------------')
# 计算分组统计（按城市分组，计算平均年龄）
print('计算分组统计（按城市分组，计算平均年龄）: \n',df.groupby('City')['Age'].mean())


print('\n------------------------7---------------------------')
# 处理缺失值（填充缺失值）
df['Age'] = df['Age'].fillna(30)
print('处理缺失值（填充缺失值）: \n', df)


print('\n------------------------7.5---------------------------')
print('添加一行，顺便看看前面添加缺失值有没效果。')
df.loc[len(df)] = ['姓名1', '', '城市1']
print(df)

print('\n------------------------8---------------------------')
# 导出为 CSV 文件
df.to_csv('./pandas库/003.02.输出数据.csv', index=False)
print('导出为 CSV 文件: ','003.02.输出数据.csv')


print('\n------------------------9---------------------------')
# 数据类型
print('数据类型: \n', df.dtypes)