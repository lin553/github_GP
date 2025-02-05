# 替换空单元格的常用方法是计算列的均值、中位数值或众数。
# Pandas使用 mean()、median() 和 mode() 方法计算列的均值（所有值加起来的平均值）、中位数值（排序后排在中间的数）和众数（出现频率最高的数）。


import pandas as pd

print("\n\n-------------------1.使用 mean() 方法计算列的均值并替换空单元格 ---------------------")
df = pd.read_csv('./pandas库/007.00.csv')
x = df.loc[:,"ST_NUM"].mean()
df.loc[:,"ST_NUM"].fillna(x, inplace = True)
print(df.to_string())



print("\n\n-------------------2.使用 median() 方法计算列的中位数并替换空单元格 ---------------------")
df = pd.read_csv('./pandas库/007.00.csv')
x = df.loc[:,"ST_NUM"].median()
df.loc[:,"ST_NUM"].fillna(x, inplace = True)
print(df.to_string())



print("\n\n-------------------3.使用 mode() 方法计算列的众数并替换空单元格 ---------------------")
df = pd.read_csv('./pandas库/007.00.csv')
x = df["ST_NUM"].mode()
df["ST_NUM"].fillna(x, inplace = True)
print(df.to_string())



print("\n\n------------- 4.Pandas 清洗格式错误数据:(通过包含空单元格的行，或者将列中的所有单元格转换为相同格式的数据) ---------------")
data = {
  "Date": ['2020/12/01', '2020/12/02' , '20201226'],    # 第三个日期格式错误
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print("原数据，第三个日期格式错误：")
print(df)
# 修正日期格式
df.loc[:,'Date'] = pd.to_datetime(df.loc[:,'Date'], format='mixed')
print('\n', df.to_string())



print("\n\n------------- 5.Pandas 清洗错误数据 ---------------")
person = {
  "name": ['Google', 'Runoob' , 'Taobao'],
  "age": [50, 40, 12345]    # 12345 年龄数据是错误的
}
df = pd.DataFrame(person)
df.loc[2, 'age'] = 30 # 修改数据
print(df.to_string())



print("\n\n------------- 6.Pandas 清洗错误数据(设置条件语句) ---------------")
person = {
  "name": ['Google', 'Runoob' , 'Taobao'],
  "age": [50, 200, 12345]    
}
df = pd.DataFrame(person)
for x in df.index:
  if df.loc[x, "age"] > 120:    # 将 age 大于 120 的设置为 120
    df.loc[x, "age"] = 120
print(" 将 age 大于 120 的设置为 120")
print(df.to_string())



print("\n\n------------- 7.Pandas 清洗错误数据(将错误数据的行删除) ---------------")
person = {
  "name": ['Google', 'Runoob' , 'Taobao'],
  "age": [50, 40, 12345]    # 12345 年龄数据是错误的
}
df = pd.DataFrame(person)
for x in df.index:
  if df.loc[x, "age"] > 120:
    df.drop(x, inplace = True)  # 将 age 大于 120 的删除
print(" 将 age 大于 120 的删除: ")
print(df.to_string())



print("\n\n------------- 8.Pandas 清洗重复数据（.duplicated()方法） ---------------")
# 如果我们要清洗重复数据，可以使用 duplicated() 和 drop_duplicates() 方法。
# 如果对应的数据是重复的，duplicated() 会返回 True，否则返回 False。
person = {
  "name": ['Google', 'Runoob', 'Runoob', 'Taobao'],
  "age": [50, 40, 40, 23]  
}
df = pd.DataFrame(person)
print(df)
print(".duplicated()方法清廷重复数据：如果对应的数据是重复的，duplicated() 会返回 True，否则返回 False。")
print(df.duplicated())



print("\n\n------------- 9. Pandas 删除重复数据，可以直接使用drop_duplicates() 方法---------------")
persons = {
  "name": ['Google', 'Runoob', 'Runoob', 'Taobao'],
  "age": [50, 40, 40, 23]  
}
df = pd.DataFrame(persons)
print("原数据：")
print(df)
df.drop_duplicates(inplace = True)
print("\n删除后数据：")
print(df)




# ========================== 完 ===========================