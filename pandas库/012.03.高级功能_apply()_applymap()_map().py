# 自定义函数应用
# Pandas 提供了多种方法应用自定义函数，用于数据清洗和转换。


print("\n\n------------------ 1.apply() — 自定义函数应用到DataFrame或Series上 -------------------")
# apply() 方法允许在 DataFrame 或 Series 上应用自定义函数，支持对行或列进行操作。
    # 参数	        说明
    # func	        需要应用的函数
    # axis	        默认为 0，表示按列应用；1 表示按行应用
    # raw	        是否传递原始数据（默认为 False）
    # result_type	定义输出的类型，如 expand, reduce, broadcast

import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [10, 20, 30, 40]})
print("源数据：\n", df,"\n")

# 定义自定义函数
def custom_func(x):
    return x * 2

# 在列上应用函数
df.loc[:,'A'] = df.loc[:,'A'].apply(custom_func)
print("使用自定义函数之后：\n",df)





print("\n\n------------- 2. applymap() 或 map() — 在整个DataFrame上应用函数 --------------")
# applymap() 只能应用于 DataFrame，作用于 DataFrame 中的每个元素。
    # 参数	    说明
    # func	    需要应用的函数

import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
print("源数据：\n", df,"\n")

# 在 DataFrame 上应用自定义函数
# df = df.applymap(lambda x: x ** 2)
df = df.map(lambda x: x ** 2)       # applymap 与 map 一样
print("使用自定义函数之后：\n",df)




print("\n\n-------------- 3.map() — 应用函数到 Series 上 ----------------")
# map() 可以对 Series 中的每个元素应用一个函数或一个映射关系。
    # 参数	    说明
    # arg	    应用的函数，字典或 Series

import pandas as pd

df = pd.DataFrame({'A': ['cat', 'dog', 'rabbit']})
print("源数据：\n", df,"\n")
# 使用字典进行映射
df.loc[:,'A'] = df.loc[:,'A'].map({'cat': 'kitten', 'dog': 'puppy'})
print("使用自定义函数之后：\n",df)





# ========================== 完 ===========================