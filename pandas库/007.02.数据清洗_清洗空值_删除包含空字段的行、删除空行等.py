# Pandas 清洗空值

# 如果我们要删除包含空字段的行，可以使用 dropna() 方法，语法格式如下：

# DataFrame.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)

# 参数说明：
    # axis：默认为 0，表示逢空值剔除整行，如果设置参数 axis＝1 表示逢空值去掉整列。
    # how：默认为 'any' 如果一行（或一列）里任何一个数据有出现 NA 就去掉整行，如果设置 how='all' 一行（或列）都是 NA 才去掉这整行。
    # thresh：设置需要多少非空值的数据才可以保留下来的。
    # subset：设置想要检查的列。如果是多个列，可以使用列名的 list 作为参数。
    # inplace：如果设置 True，将计算得到的值直接覆盖之前的值并返回 None，修改的是源数据。
    # 我们可以通过 isnull() 判断各个单元格是否为空。
# ==================================================================

import pandas as pd


print("\n\n-------------- 1.筛选'NUM_BEDROOMS'列的空字段行号：------------------")
df = pd.read_csv('./pandas库/007.00.csv')

print (df['NUM_BEDROOMS'])
print("\n筛选'NUM_BEDROOMS'列的空字段行号:")
print (df['NUM_BEDROOMS'].isnull())     




print('\n\n-------------- 2.指定空数据类型：------------------')
# 以上例子中我们看到 Pandas 把 n/a 和 NA 当作空数据，na 不是空数据，不符合我们要求，我们可以指定空数据类型：
df = pd.read_csv('./pandas库/007.00.csv')
print('原空数据类型:')
print (df['NUM_BEDROOMS'])      

print("\n\n指定'n/a', 'na', '--' 都是空数据类型:")
missing_values = ["n/a", "na", "--"]    # 设置空数据类型
df = pd.read_csv('./pandas库/007.00.csv', na_values = missing_values)   # 按新的空数据类型，再次读入数据
print (df['NUM_BEDROOMS'])
print (df['NUM_BEDROOMS'].isnull())



print('\n\n-------------- 3.删除包含空数据的行.dropna()方法 （原数据：df, 没有被删除；这里是新建一个删除后的新数据:new_df）------------------')
df = pd.read_csv('./pandas库/007.00.csv')
new_df = df.dropna()        # 原数据：df, 没有被删除，这里是新建一个删除后的新数据
print('new_df: ')
print(new_df.to_string())
print('\n\n df:')
print(df)


print("\n\n-------------- 4. 注意：默认情况下，dropna() 方法返回一个新的 DataFrame，不会修改源数据。如果你要修改源数据 DataFrame, 可以使用 inplace = True 参数------------------")
df = pd.read_csv('./pandas库/007.00.csv')
df.dropna(inplace = True)
print(df.to_string())


print("\n\n-------------- 5.移除指定列有空值的行 ------------------")
df = pd.read_csv('./pandas库/007.00.csv')
df.dropna(subset=['ST_NUM'], inplace = True)
print('移除 ST_NUM 列中字段值为空的行:')
print(df.to_string())


print("\n\n-------------- 6. fillna() 方法替换一些空字段 ------------------")
df = pd.read_csv('./pandas库/007.00.csv')
print(df.to_string())
print('\n使用 12345 替换空字段(NaN):')
df.fillna(12345, inplace = True)
print(df.to_string())


print("\n\n-------------- 7.指定某一个列来替换数据 ------------------")
df = pd.read_csv('./pandas库/007.00.csv')
df.loc[:,'PID'].fillna(12345, inplace = True)     # inplace = True： 直接修改源数据
print(" 'PID'列替换数据:'NaN'换成'12345' ")
print(df.to_string())






# ========================== 完 ===========================