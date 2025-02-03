import pandas as pd
import json

# 使用 Python JSON 模块载入数据
with open('./pandas库/006.08.json','r') as f:
    data = json.loads(f.read())
    
df = pd.json_normalize(
    data, 
    record_path =['students'], 
    meta=[
        'school_name',
        'class',
        ['info', 'president'], 
        ['info', 'address'],
        ['info', 'contacts', 'tel'],
        ['info', 'contacts', 'email']
    ]
)

df.to_excel('./pandas库/006.08.xlsx')
print(df)