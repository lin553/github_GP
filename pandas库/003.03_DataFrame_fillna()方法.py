# 摘自：https://blog.csdn.net/qq_17753903/article/details/89892631

# pandas中fillna()方法，能够使用指定的方法填充NA/NaN值。

# 1.函数详解
#     函数形式：fillna(value=None, method=None, axis=None, inplace=False, limit=None, downcast=None, **kwargs)

# 参数
    # value：用于填充的空值的值。

    # method： {'backfill', 'bfill', 'pad', 'ffill', None}, default None。定义了填充空值的方法， 
    #         pad / ffill表示用前面行/列的值，填充当前行/列的空值， backfill / bfill表示用后面行/列的值，填充当前行/列的空值。

    # axis：轴。0或'index'，表示按行删除；1或'columns'，表示按列删除。

    # inplace：是否原地替换。布尔值，默认为False。如果为True，则在原DataFrame上进行操作，返回值为None。

    # limit：int， default None。如果method被指定，对于连续的空值，这段连续区域，最多填充前 limit 个空值（如果存在多段连续区域，
    #         每段最多填充前 limit 个空值）。如果method未被指定， 在该axis下，最多填充前 limit 个空值（不论空值连续区间是否间断）

    # downcast：dict, default is None，字典中的项为，为类型向下转换规则。或者为字符串“infer”，此时会在合适的等价类型之间进行向下转换，
    #         比如float64 to int64 if possible。
# =================================================================================================



import numpy as np
import pandas as pd

print('\n-------------------------- 初始数据 ---------------------------')
a = np.arange(100,dtype=float).reshape((10,10))
d = pd.DataFrame(data=a)        # d 与 a 共享内存，即：它们的数据是存储在同一个内存空间，当 a 的值改变时，d 的值也改变
print(d)

print('\n\n-------------------------- 设置NaN ---------------------------')
for i in range(len(a)):
    a[i,:i] = np.nan        # 在numpy库中：a[i, j]  这里逗号分隔行列，即：i 表示行索引，j 表示列索引。
                                        # a[i, :j]：获取第 i 行中从第0列到第 j-1 列的所有元素（不包括第 j 列）。
                                        # a[:i, j]：获取从第0行到第 i-1 行的所有行中的第 j 列的所有元素。
a[6,0] = 100.0
print(d)

print('\n\n-------------------------- 用0填补空值:  d2 = d.fillna(value=0) ---------------------------')
d2 = d.fillna(value=0)
print('d2: \n',d2)
print('\n\nd: \n', d)


