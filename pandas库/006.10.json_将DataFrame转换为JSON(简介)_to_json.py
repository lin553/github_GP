# 将 DataFrame 转换为 JSON
    # DataFrame.to_json() - 将 DataFrame 转换为 JSON 数据
    # to_json() 方法用于将 DataFrame 转换为 JSON 格式的数据，可以指定 JSON 的结构化方式。

# 语法格式：

# df.to_json(
#     path_or_buffer=None,    # 输出的文件路径或文件对象，如果是 None 则返回 JSON 字符串
#     orient=None,            # JSON 格式方式，支持 'split', 'records', 'index', 'columns', 'values'
#     date_format=None,       # 日期格式，支持 'epoch', 'iso'
#     default_handler=None,   # 自定义非标准类型的处理函数
#     lines=False,            # 是否将每行数据作为一行（适用于 'records' 或 'split'）
#     encoding='utf-8'        # 编码格式
# )

# 参数说明：
    # 参数	            说明	                                                                默认值
    # path_or_buffer	输出的文件路径或文件对象，若为 None，则返回 JSON 字符串	                   None
    # orient	        指定 JSON 格式结构，支持 split、records、index、columns、values	None     （默认是 columns）
    # date_format	    日期格式，支持 'epoch' 或 'iso' 格式	                                 None
    # default_handler	自定义处理非标准类型（如 datetime 等）的处理函数	                       None
    # lines	            是否将每行数据作为一行输出（适用于 records 或 split）	                   False
    # encoding	        输出文件的编码格式	                                                     'utf-8'
# =================================================================

import pandas as pd

# 创建 DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
})



print('\n--------------0--------------')
# 将 DataFrame 转换为 JSON 字符串
json_str = df.to_json()
print(json_str)
print(type(json_str))

print('\n--------------1--------------')
print(df.to_json())
print(type(df.to_json()))

print('\n--------------2--------------')
print(df.to_string())
print(type(df.to_string()))

print('\n--------------3--------------')
str_str = df.to_string()
print(str_str)
print(type(str_str))



print('\n--------------4--------------')
print(r"将 DataFrame 转换为 JSON 文件，指定 orient='records'")
df.to_json('./pandas库/006.10.json', orient='records', lines=True)
