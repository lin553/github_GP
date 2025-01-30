# 使用列表创建 Series
import pandas as pd
import numpy as np      # 数学函数

print("\n=============创建series===================")
# 直接用数组创建
s = pd.Series([1, 2, 3, 4])
print(s,'\n')

# 使用 NumPy 数组创建 Series
s = pd.Series(np.array([1, 2, 3, 4]))
print(s,'\n')

# 使用字典创建 Series
s = pd.Series({'a': 1, 'b': 2, 'c': 3, 'd': 4})
print(s,'\n')




print("\n=============基本操作===================")
# 指定索引创建 Series
s = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])

# 获取值
value = s['c']  # 获取索引为2的值
print('\n', s['a'])  # 返回索引标签 'a' 对应的元素
print('\n value = ',value)
value = s[2]        # 不建议这样用索引，原来索引是英文字母
print('\n value = ',value)

print('----------1----------')
# 获取多个值
subset = s[1:4]  # 获取索引为1到3的值
print(s)
print('subset: ',subset)

print('----------2----------')
# 使用自定义索引
value = s['b']  # 获取索引为'b'的值
print(s)
print('value = ', value)

print('----------3----------')
# 索引和值的对应关系
for index, value in s.items():
    print(f"Index: {index}, Value: {value}")

print('----------4----------')
# 使用切片语法来访问 Series 的一部分
print(s['a':'c'])  # 返回索引标签 'a' 到 'c' 之间的元素
print(s[:3])  # 返回前三个元素

print('----------5----------')
# 为特定的索引标签赋值
s['a'] = 10  # 将索引标签 'a' 对应的元素修改为 10
print(s)

print('----------6----------')
# 通过赋值给新的索引标签来添加元素
s['e'] = 5  # 在 Series 中添加一个新的元素，索引标签为 'e'
print(s)

print('----------7----------')
# 使用 del 删除指定索引标签的元素。
del s['a']  # 删除索引标签 'a' 对应的元素
print(s)

print('----------8----------')
# 使用 drop 方法删除一个或多个索引标签，并返回一个新的 Series。
s_dropped = s.drop(['b'])  # 返回一个删除了索引标签 'b' 的新 Series
print('s: \n',s)
print('\n s_dropped: \n', s_dropped)
