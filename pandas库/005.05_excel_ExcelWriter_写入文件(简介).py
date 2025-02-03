# ExcelWriter - 写入 Excel 文件
    # ExcelWriter 是 pandas 提供的一个类，用于将 DataFrame 或 Series 对象写入 Excel 文件。使用 ExcelWriter，你可以在一个 Excel 文件中
                # 写入多个工作表，并且可以更灵活地控制写入过程。

# 语法格式如下：

# pandas.ExcelWriter(path, engine=None, date_format=None, datetime_format=None, mode='w', storage_options=None, 
                    # if_sheet_exists=None, engine_kwargs=None)


# 参数说明：
    # path：这是必需的参数，指定了要写入的 Excel 文件的路径、URL 或文件对象。可以是本地文件路径、远程存储路径（如 S3）、
            # URL 链接或已打开的文件对象。
    # engine：这是一个可选参数，用于指定写入 Excel 文件的引擎。如果为 None，则 pandas 会自动选择一个可用的引擎（默认优先选择 openpyxl，
            # 如果不可用则选择其他可用引擎）。常见的引擎包括 'openpyxl'（用于 .xlsx 文件）、'xlsxwriter'（提供高级格式化和图表功能）、
            # 'odf'（用于 OpenDocument 格式如 .ods）等。
    # date_format：这是一个可选参数，指定写入 Excel 文件中日期的格式字符串，例如 "YYYY-MM-DD"。
    # datetime_format：这是一个可选参数，指定写入 Excel 文件中日期时间对象的格式字符串，例如 "YYYY-MM-DD HH:MM:SS"。
    # mode：这是一个可选参数，默认为 'w'，表示写入模式。如果设置为 'a'，则表示追加模式，向现有文件中添加数据（仅支持部分引擎，如 openpyxl）。
    # storage_options：这是一个可选参数，用于指定与存储后端连接的额外选项，例如认证信息、访问权限等，适用于写入远程存储（如 S3、GCS）。
    # if_sheet_exists：这是一个可选参数，默认为 'error'，指定如果工作表已经存在时的行为。选项包括 'error'（抛出错误）、
            # 'new'（创建一个新工作表）、'replace'（替换现有工作表的内容）、'overlay'（在现有工作表上覆盖写入）。
    # engine_kwargs：这是一个可选参数，用于传递给引擎的其他关键字参数。这些参数会传递给相应引擎的函数，例如 xlsxwriter.Workbook(file, 
            # **engine_kwargs) 或 openpyxl.Workbook(**engine_kwargs) 等。



# =================================================================
# # 创建 ExcelWriter 对象，
# # 这里，ExcelWriter 被用作上下文管理器，确保文件在操作完成后正确关闭。
# with ExcelWriter('output.xlsx') as writer:
#     df.to_excel(writer, sheet_name='Sheet1')   # 写入excel到硬盘 



# =================================================================
# 写入多个工作表：
    # 你可以使用同一个 ExcelWriter 对象将不同的 DataFrame 写入同一个 Excel 文件的不同工作表。

# 实例
# df1 = pd.DataFrame([["AAA", "BBB"]], columns=["Spam", "Egg"])  
# df2 = pd.DataFrame([["ABC", "XYZ"]], columns=["Foo", "Bar"])  
# with pd.ExcelWriter("path_to_file.xlsx") as writer:
#     df1.to_excel(writer, sheet_name="Sheet1")  
#     df2.to_excel(writer, sheet_name="Sheet2")


