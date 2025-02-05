# DataFrame.to_excel() - 将 DataFrame 写入 Excel 文件
    # to_excel() 方法用于将 DataFrame 写入 Excel 文件，支持 .xls 和 .xlsx 格式。

# 语法格式如下：
# DataFrame.to_excel(excel_writer, *, sheet_name='Sheet1', na_rep='', float_format=None, columns=None, header=True, 
                    # index=True, index_label=None, startrow=0, startcol=0, engine=None, merge_cells=True, inf_rep='inf',
                    # freeze_panes=None, storage_options=None, engine_kwargs=None)

# 参数说明：
    # excel_writer：这是必需的参数，指定了要写入的 Excel 文件路径或文件对象。
    # sheet_name='Sheet1'：指定写入的工作表名称，默认为 'Sheet1'。
    # na_rep=''：指定在 Excel 文件中表示缺失值（NaN）的字符串，默认为空字符串。
    # float_format=None：指定浮点数的格式。如果为 None，则使用 Excel 的默认格式。
    # columns=None：指定要写入的列。如果为 None，则写入所有列。
    # header=True：指定是否写入列名作为第一行。如果为 False，则不写入列名。
    # index=True：指定是否写入索引作为第一列。如果为 False，则不写入索引。
    # index_label=None：指定索引列的标签。如果为 None，则不写入索引标签。
    # startrow=0：指定开始写入的行号，默认从第0行开始。
    # startcol=0：指定开始写入的列号，默认从第0列开始。
    # engine=None：指定写入 Excel 文件时使用的引擎，默认为 None，pandas 会自动选择。
    # merge_cells=True：指定是否合并单元格。如果为 True，则合并具有相同值的单元格。
    # inf_rep='inf'：指定在 Excel 文件中表示无穷大值的字符串，默认为 'inf'。
    # freeze_panes=None：指定冻结窗格的位置。如果为 None，则不冻结窗格。
    # storage_options=None：用于云存储的参数字典。
    # engine_kwargs=None：传递给引擎的额外参数字典。
# =================================================================



import pandas as pd

# 创建一个简单的 DataFrame
df = pd.DataFrame({
'Name': ['Alice', 'Bob', 'Charlie'],
'Age': [25, 30, 35],
'City': ['New York', 'Los Angeles', 'Chicago']
})

# 将 DataFrame 写入 Excel 文件，写入 'Sheet1' 表单
df.to_excel('./pandas库/005.03.xlsx', sheet_name='Sheet1', index=False)

# 写入多个表单，使用 ExcelWriter
with pd.ExcelWriter('./pandas库/005.03.xlsx') as writer:    
    df.to_excel(writer, sheet_name='Sheet2', index=False)
    df.to_excel(writer, sheet_name='Sheet3', index=False)





# ========================== 完 ===========================