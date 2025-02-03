# 假设有一组内嵌的 JSON 数据文件 006.06.json ：

import pandas as pd

df = pd.read_json('./pandas库/006.06.json')     # 读取json内嵌文件




with pd.ExcelWriter(        # 打开excel文件
    './pandas库/006.06.xlsx',
) as writer:
    df.to_excel(writer)     # 将df写入到打开的excel文件中

print(df)