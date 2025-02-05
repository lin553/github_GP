import pandas as pd

print('\n--------------------- 1. 读取默认的第一个表单 ---------------------')
df = pd.read_excel('./pandas库/005.02.xlsx',skiprows=1)
print(df)


print('\n--------------------- 2.读取指定表单的内容（表单名称） ---------------------')
df = pd.read_excel('./pandas库/005.02.xlsx', sheet_name='Sheet1',skiprows=1)
print(df)


print('\n--------------------- 3.读取多个表单，返回一个字典 ---------------------')
dfs = pd.read_excel('./pandas库/005.02.xlsx', sheet_name=['Sheet1', 'Sheet2'], skiprows=1)
print(dfs)


print('\n--------------------- 4.自定义列名并跳过前两行 ---------------------')
df = pd.read_excel('./pandas库/005.02.xlsx', header=None, names=['A', 'B', 'C'], skiprows=2)
print(df)




# ========================== 完 ===========================