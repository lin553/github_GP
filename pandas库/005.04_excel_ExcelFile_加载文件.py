# ExcelFile - 加载 Excel 文件
    # ExcelFile 是一个用于读取 Excel 文件的类，它可以处理多个表单，并在不重新打开文件的情况下访问其中的数据。

# 语法格式如下：

# excel_file = pd.ExcelFile('data.xlsx')

# 常用方法：
    # 方法	                    功能描述
        # sheet_names	        返回文件中所有表单的名称列表
        # parse(sheet_name)	    解析指定表单并返回一个 DataFramea
        # close()	            关闭文件，以释放资源


# 实例
import pandas as pd

# 使用 ExcelFile 加载 Excel 文件
excel_file = pd.ExcelFile('./pandas库/005.03.xlsx')

# 查看所有表单的名称
print(excel_file.sheet_names)

# 读取指定的表单
df = excel_file.parse('Sheet2')
print(df)

# 关闭文件
excel_file.close()