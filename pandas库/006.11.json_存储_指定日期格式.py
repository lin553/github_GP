# 将 DataFrame 转换为 JSON 并指定日期格式

import pandas as pd

# 创建 DataFrame，包含日期数据
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Date': pd.to_datetime(['2021-01-01', '2022-02-01', '2023-03-01']),
    'Age': [25, 30, 35]
})

# 将 DataFrame 转换为 JSON，并指定日期格式为 'iso'    并存储
json_str = df.to_json('./pandas库/006.11.json', date_format='iso')

print(r'-------------------------------------')
print(json_str)