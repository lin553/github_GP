# 从 JSON 文件/字符串加载数据
    # pd.read_json() - 读取 JSON 数据
        # read_json() 用于从 JSON 格式的数据中读取并加载为一个 DataFrame。它支持从 JSON 文件、JSON 字符串或 JSON 网址中加载数据。

# 语法格式：

import pandas as pd

path_or_buffer = './pandas库/006.01.json'

df = pd.read_json(
    path_or_buffer,      # JSON 文件路径、JSON 字符串或 URL
    orient=None,         # JSON 数据的结构方式，默认是 'columns'
    dtype=None,          # 强制指定列的数据类型
    convert_axes=True,   # 是否转换行列索引
    convert_dates=True,  # 是否将日期解析为日期类型
    # keep_default_na=True # 是否保留默认的缺失值标记  (实际运行时，此参数报错：TypeError: read_json() got an unexpected keyword argument 'keep_default_na')
)

print(df)
print('\n',df.to_string)   # to_string() 用于返回 DataFrame 类型的数据，我们也可以直接处理 JSON 字符串


# 参数说明：
    # 参数	                说明	                                                                        默认值
    # path_or_buffer	    JSON 文件的路径、JSON 字符串或 URL	                                             必需参数
    # orient	            定义 JSON 数据的格式方式。常见值有 split、records、index、columns、values。	       None（根据文件自动推断）
    # dtype	                强制指定列的数据类型	                                                         None
    # convert_axes	        是否将轴转换为合适的数据类型                                                   	  True
    # convert_dates	        是否将日期解析为日期类型	                                                     True
    # keep_default_na	    是否保留默认的缺失值标记（如 NaN）	                                              True


# 常见的 orient 参数选项:
    # orient 值	        JSON 格式示例	                                                 描述
    # split	            {"index":["a","b"],"columns":["A","B"],"data":[[1,2],[3,4]]}	使用键 index、columns 和 data 结构
    # records	        [{"A":1,"B":2},{"A":3,"B":4}]	                                每个记录是一个字典，表示一行数据
    # index	            {"a":{"A":1,"B":2},"b":{"A":3,"B":4}}	                        使用索引为键，值为字典的方式
    # columns	        {"A":{"a":1,"b":3},"B":{"a":2,"b":4}}	                        使用列名为键，值为字典的方式
    # values	        [[1,2],[3,4]]	                                                只返回数据，不包括索引和列名




# ========================== 完 ===========================