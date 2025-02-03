# 从 JSON 字符串加载数据

import pandas as pd

# JSON 字符串
json_data = '''
[
  {"Name": "Alice",     "Age": 25,      "City": "New York"},
  {"Name": "Bob",       "Age": 30,      "City": "Los Angeles"},
  {"Name": "Charlie",   "Age": 35,      "City": "Chicago"}
]
'''

# 从 JSON 字符串读取数据
df = pd.read_json(json_data)

print(df)