# 从 JSON 数据读取（指定 orient 为 records）

import pandas as pd

# JSON 数据
json_data = '''
[
  {"Name": "Alice", "Age": 25, "City": "New York"},
  {"Name": "Bob", "Age": 30, "City": "Los Angeles"},
  {"Name": "Charlie", "Age": 35, "City": "Chicago"}
]
'''

# 从 JSON 字符串读取数据，指定 orient='records'  每个记录是一个字典，表示一行数据
df = pd.read_json(json_data, orient='records')

print(df)