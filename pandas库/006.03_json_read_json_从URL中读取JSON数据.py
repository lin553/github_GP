# 从 URL 中读取 JSON 数据

import pandas as pd

URL = 'https://static.jyshare.com/download/sites.json'
df = pd.read_json(URL)
print(df)