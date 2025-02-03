# 这时我们就需要使用到 json_normalize() 方法将内嵌的数据完整的解析出来

import pandas as pd
import json


with open('./pandas库/006.06.json','r') as f:       # 用只读的方式打开文件
    data = json.loads(f.read())                     # 使用 Python JSON 模块载入数据

# 展平数据（即：完整解析内嵌数据, 只有内嵌数据）
df_nested_list = pd.json_normalize(data, record_path =['students'])
print('内嵌数据：\n', df_nested_list)


print('\n=================================================================')
# 显示结果还没有包含 school_name 和 class 元素，如果需要展示出来可以使用 meta 参数来显示这些元数据
# 展平数据
df_nested_list = pd.json_normalize(
    data,
    meta=['school_name', 'class'],
    record_path =['students']
)
print('所有数据：\n', df_nested_list)