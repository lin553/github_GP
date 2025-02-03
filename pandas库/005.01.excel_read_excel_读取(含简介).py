# Pandas Excel 文件操作
# Pandas 提供了丰富的 Excel 文件操作功能，帮助我们方便地读取和写入 .xls 和 .xlsx 文件，支持多表单、索引、列选择等复杂操作，
        # 是数据分析中必备的工具。


# 操作	                        方法	                   说明
# 读取 Excel 文件	            pd.read_excel()	           读取 Excel 文件，返回 DataFrame
# 将 DataFrame 写入 Excel	    DataFrame.to_excel()	   将 DataFrame 写入 Excel 文件
# 加载 Excel 文件	            pd.ExcelFile()	           加载 Excel 文件并访问多个表单
# 使用 ExcelWriter 写多个表单	 pd.ExcelWriter()	        写入多个 DataFrame 到同一 Excel 文件的不同表单


# pd.read_excel() -             读取 Excel 文件
                              # 方法用于从 Excel 文件中读取数据并加载为 DataFrame。它支持读取 .xls 和 .xlsx 格式的文件。

# 语法格式如下：
# import pandas 
# pandas.read_excel(io, sheet_name=0, *, header=0, names=None, index_col=None, usecols=None, dtype=None, engine=None, 
#                   converters=None, true_values=None, false_values=None, skiprows=None, nrows=None, na_values=None, 
#                   keep_default_na=True, na_filter=True, verbose=False, parse_dates=False, date_parser=<no_default>, 
#                   date_format=None, thousands=None, decimal='.', comment=None, skipfooter=0, storage_options=None, 
#                   dtype_backend=<no_default>, engine_kwargs=None)

# 参数说明：
    # io：这是必需的参数，指定了要读取的 Excel 文件的路径或文件对象。
    # sheet_name=0：指定要读取的工作表名称或索引。默认为0，即第一个工作表。
    # header=0：指定用作列名的行。默认为0，即第一行。
    # names=None：用于指定列名的列表。如果提供，将覆盖文件中的列名。
    # index_col=None：指定用作行索引的列。可以是列的名称或数字。
    # usecols=None：指定要读取的列。可以是列名的列表或列索引的列表。
    # dtype=None：指定列的数据类型。可以是字典格式，键为列名，值为数据类型。
    # engine=None：指定解析引擎。默认为None，pandas 会自动选择。
    # converters=None：用于转换数据的函数字典。
    # true_values=None：指定应该被视为布尔值True的值。
    # false_values=None：指定应该被视为布尔值False的值。
    # skiprows=None：指定要跳过的行数或要跳过的行的列表。
    # nrows=None：指定要读取的行数。
    # na_values=None：指定应该被视为缺失值的值。
    # keep_default_na=True：指定是否要将默认的缺失值（例如NaN）解析为NA。
    # na_filter=True：指定是否要将数据转换为NA。
    # verbose=False：指定是否要输出详细的进度信息。
    # parse_dates=False：指定是否要解析日期。
    # date_parser=<no_default>：用于解析日期的函数。
    # date_format=None：指定日期的格式。
    # thousands=None：指定千位分隔符。
    # decimal='.'：指定小数点字符。
    # comment=None：指定注释字符。
    # skipfooter=0：指定要跳过的文件末尾的行数。
    # storage_options=None：用于云存储的参数字典。
    # dtype_backend=<no_default>：指定数据类型后端。
    # engine_kwargs=None：传递给引擎的额外参数字典。
# =================================================================


import pandas as pd

# 读取 data.xlsx 文件
df = pd.read_excel('./pandas库/005.01.xlsx',sheet_name=0,skiprows=1)  #sheet_name=0: 读取第一个工作表。   skiprows=1：跳过第一行

# 打印读取的 DataFrame
print(df)
print('\n', type(df))