import pandas as pd

s = pd.Series([1, 2, 3, 4])
print('s: \n',s,'\n')

print('\n---------------0----------------')
# 获取索引
index = s.index
print('index: ', index)

print('\n---------------1----------------')
# 获取值数组
values = s.values
print('values: ', values)

print('\n---------------2----------------')
# 获取描述统计信息
print('s.describe(): \n',  s.describe())

print('\n---------------3----------------')
# 获取最大值和最小值的索引
print('s.idxmax(): ', s.idxmax())
print('s.idxmin(): ', s.idxmin())



print('\n========================================')
# 其他属性和方法
print('s.dtype: ',s.dtype)   # 数据类型
print('\n---------------5----------------')
print('s.shape: ',s.shape)   # 形状
print('\n---------------6----------------')
print('s.size: ',s.size)    # 元素个数
print('\n---------------7----------------')
print('s.head()前几个元素，默认是前 5 个: \n',s.head())  # 前几个元素，默认是前 5 个
print('\n---------------8----------------')
print('s.tail()后几个元素，默认是后 5 个: \n',s.tail())  # 后几个元素，默认是后 5 个
print('\n---------------9----------------')
print('s.sum(): ',s.sum())   # 求和
print('\n---------------10----------------')
print('s.mean()平均值: ',s.mean())  # 平均值
print('\n---------------11----------------')
print('s.std()标准差: ',s.std())   # 标准差
print('\n---------------12----------------')
print('s.min(): ',s.min())   # 最小值
print('\n---------------13----------------')
print('s.max(): ',s.max())   # 最大值



print('\n========================================')
# 使用布尔表达式：根据条件过滤 Series
print('使用布尔表达式：根据条件过滤: s > 2\n',s > 2)  # 返回一个布尔 Series，其中的元素值大于 2

print('\n---------------14----------------')
print('输出 Series 的数据类型: ',s.dtype)  # 输出 Series 的数据类型

print('\n---------------15----------------')
s = s.astype('float64')  # 将 Series 中的所有元素转换为 float64 类型
print('转换为 float64 类型: s.astype(\'float64\'): ',s.dtype)  # 输出 Series 的数据类型




# ========================== 完 ===========================