# Pandas CSV 文件
    # CSV（Comma-Separated Values，逗号分隔值，有时也称为字符分隔值，因为分隔字符也可以不是逗号），其文件以纯文本形式存储表格数据（数字和文本）。
    # CSV 是一种通用的、相对简单的文件格式，被用户、商业和科学广泛应用。


# =================================================================
# Pandas 可以很方便的处理 CSV 文件，常用方法有：

# 方法名称	            功能描述	                              常用参数
# pd.read_csv()	        从 CSV 文件读取数据并加载为 DataFrame	   filepath_or_buffer (路径或文件对象)，sep (分隔符)，header (行标题)，
                                                                # names (自定义列名)，dtype (数据类型)，index_col (索引列)

# DataFrame.to_csv()	将 DataFrame 写入到 CSV 文件	           path_or_buffer (目标路径或文件对象)，sep (分隔符)，
                                                                # index (是否写入索引)，columns (指定列)，header (是否写入列名)，
                                                                # mode (写入模式)



# =================================================================
# 本文以 nba.csv 为例，你可以下载 nba.csv 或打开 nba.csv 查看。

# pd.read_csv() - 读取 CSV 文件
# read_csv() 是从 CSV 文件中读取数据的主要方法，将数据加载为一个 DataFrame。


# =================================================================
# read_csv 常用参数:

# 参数	                说明	                                                              默认值
# filepath_or_buffer	CSV 文件的路径或文件对象（支持 URL、文件路径、文件对象等）	              必需参数
# sep	                定义字段分隔符，默认是逗号（,），可以改为其他字符，如制表符（\t）	       ','
# header	            指定行号作为列标题，默认为 0（表示第一行），或者设置为 None 没有标题	   0
# names	                自定义列名，传入列名列表	                                            None
# index_col         	用作行索引的列的列号或列名	                                            None
# usecols	            读取指定的列，可以是列的名称或列的索引	                                 None
# dtype	                强制将列转换为指定的数据类型	                                        None
# skiprows	            跳过文件开头的指定行数，或者传入一个行号的列表	                          None
# nrows	                读取前 N 行数据	                                                       None
# na_values         	指定哪些值应视为缺失值（NaN）	                                        None
# skipfooter        	跳过文件结尾的指定行数	                                                0
# encoding	            文件的编码格式（如 utf-8，latin1 等）	                                None


# =================================================================

import pandas as pd

print('\n----------- 使用自定义参数方法读取csv文件 ---------------')
# 读取 CSV 文件，并自定义列名和分隔符
df = pd.read_csv('./pandas库/004.01.csv', sep=',', header=0, names=['自定义段名_1', '自定义段名_2', '自定义段名_3'], 
                 dtype={'Name': str, 'Age': float, 'City':str})
print(df.to_string())
print('\n', df.dtypes)

print('\n----------- 使用默认参数方法读取csv文件 ---------------')
df = pd.read_csv('./pandas库/004.01.csv')
print(df.to_string())       # to_string() 用于返回 DataFrame 类型的数据，
                                        # 如果不使用该函数，则输出结果为数据的前面 5 行和末尾 5 行，中间部分以 ... 代替。


print('\n\n\n================ 读取空文件 ==================')
print('\n----------- 使用自定义参数方法读取csv文件 ---------------')
df = pd.read_csv('./pandas库/004.01_空文件.csv', sep=',', header=0, names=['自定义段名_1', '自定义段名_2', '自定义段名_3'], 
                 dtype={'Name': str, 'Age': float, 'City':str})
print(df.to_string())
print('\n', df.dtypes)


print('\n------------- 使用默认参数方法读取csv文件 -------------------')
print('因以下方法读取空文件会抛出异常, 注释掉了')
# df = pd.read_csv('./pandas库/004.01_空文件.csv')
# print(df.to_string())