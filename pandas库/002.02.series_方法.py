# Series 方法
# 下面是 Series 中一些常用的方法：

# 方法名称	                功能描述
# index	                    获取 Series 的索引
# values	                获取 Series 的数据部分（返回 NumPy 数组）
# head(n)	                返回 Series 的前 n 行（默认为 5）
# tail(n)	                返回 Series 的后 n 行（默认为 5）
# dtype                 	返回 Series 中数据的类型
# shape	                    返回 Series 的形状（行数）
# describe()	            返回 Series 的统计描述（如均值、标准差、最小值等）
# isnull()	                返回一个布尔 Series，表示每个元素是否为 NaN
# notnull()	                返回一个布尔 Series，表示每个元素是否不是 NaN
# unique()	                返回 Series 中的唯一值（去重）
# value_counts()	        返回 Series 中每个唯一值的出现次数
# map(func)	                将指定函数应用于 Series 中的每个元素
# apply(func)	            将指定函数应用于 Series 中的每个元素，常用于自定义操作
# astype(dtype)	            将 Series 转换为指定的类型
# sort_values()	            对 Series 中的元素进行排序（按值排序）
# sort_index()	            对 Series 的索引进行排序
# dropna()	                删除 Series 中的缺失值（NaN）
# fillna(value)	            充 Series 中的缺失值（NaN）
# replace(to_replace, value)替换 Series 中指定的值
# cumsum()	                返回 Series 的累计求和
# cumprod()	                返回 Series 的累计乘积
# shift(periods)	        将 Series 中的元素按指定的步数进行位移
# rank()	                返回 Series 中元素的排名
# corr(other)	            计算 Series 与另一个 Series 的相关性（皮尔逊相关系数）
# cov(other)	            计算 Series 与另一个 Series 的协方差
# to_list()	                将 Series 转换为 Python 列表
# to_frame()	            将 Series 转换为 DataFrame
# iloc[]	                通过位置索引来选择数据
# loc[]	                    通过标签索引来选择数据

# =================================================================


import pandas as pd

# 创建 Series
data = [1, 2, 3, 4, 5, 6]
index = ['a', 'b', 'c', 'd', 'e', 'f']
s = pd.Series(data, index=index)

# 查看基本信息
print("\n索引s.index：", s.index)
print("\n数据s.values：", s.values)
print("\n数据类型s.dtype：", s.dtype)
print("\n前两行数据s.head(2)：\n", s.head(2))

# 使用 map 函数将每个元素加倍
s_doubled = s.map(lambda x: x * 2)
print("\n元素加倍后：\n", s_doubled)

# 计算累计和
cumsum_s = s.cumsum()
print("\n累计求和s.cumsum：\n", cumsum_s)

# 查找缺失值（这里没有缺失值，所以返回的全是 False）
print("\n缺失值判断s.isnull()：\n", s.isnull())

# 排序
sorted_s = s.sort_values()
print("\nsorted_s排序后：\n", sorted_s)




# ========================== 完 ===========================