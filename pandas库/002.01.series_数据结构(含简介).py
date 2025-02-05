# 创建 Series
    # 可以使用 pd.Series() 构造函数创建一个 Series 对象，传递一个数据数组（可以是列表、NumPy 数组等）和一个可选的索引数组。

# pandas.Series(data=None, index=None, dtype=None, name=None, copy=False, fastpath=False)

# 参数说明：
    # data：Series 的数据部分，可以是列表、数组、字典、标量值等。如果不提供此参数，则创建一个空的 Series。
    # index：Series 的索引部分，用于对数据进行标记。可以是列表、数组、索引对象等。如果不提供此参数，则创建一个默认的整数索引。
    # dtype：指定 Series 的数据类型。可以是 NumPy 的数据类型，例如 np.int64、np.float64 等。如果不提供此参数，则根据数据自动推断数据类型。
    # name：Series 的名称，用于标识 Series 对象。如果提供了此参数，则创建的 Series 对象将具有指定的名称。
    # copy：是否复制数据。默认为 False，表示不复制数据。如果设置为 True，则复制输入的数据。
    # fastpath：是否启用快速路径。默认为 False。启用快速路径可能会在某些情况下提高性能。

# 注意事项：
    # Series 中的数据是有序的。
    # 可以将 Series 视为带有索引的一维数组。
    # 索引可以是唯一的，但不是必须的。
    # 数据可以是标量、列表、NumPy 数组等。
#================================================================


import pandas as pd


# 创建一个Series对象，指定名称为'A'，值分别为1, 2, 3, 4
# 默认索引为0, 1, 2, 3
series = pd.Series([1, 2, 3, 4], name='A')
# 显示Series对象
print('\n',series,'\n')


print('\n============= 1.显式地设置索引 =================')
# 如果你想要显式地设置索引，可以这样做：
custom_index = [1, 2, 3, 4]  # 自定义索引
series_with_index = pd.Series([1, 2, 3, 4], index=custom_index, name='A')
# 显示带有自定义索引的Series对象
print('自定义索引: \n', series_with_index)



print('\n============== 2.使用索引查值 ================')
a = [1, 2, 3]
myvar = pd.Series(a)
print(myvar)
print('索引[1]：',myvar[1])





print('\n============= 3.自定义索引[y] =================')
a = ["Google", "Runoob", "Wiki"]
myvar = pd.Series(a, index = ["x", "y", "z"])
print(myvar)
print('自定义索引[y]: ', myvar['y'])



print('\n========== 4.使用字典创建pd对象 ===========')
sites = {1: "value1", 2: "value2", 3: "value3"}
myvar = pd.Series(sites,name='dict')
print(myvar)



print('\n========== 5.字典对象创建pd时：指定需要数据的索引 ===========')
sites = {1: "value1", 2: "value2", 3: "value3"}
myvar = pd.Series(sites,name='dict',index=[1,2])
print(myvar)




# ========================== 完 ===========================