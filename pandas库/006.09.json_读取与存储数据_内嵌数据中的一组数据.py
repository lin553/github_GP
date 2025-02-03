# 这里我们需要使用到 glom 模块来处理数据套嵌，glom 模块允许我们使用符号： “.” 来访问内嵌对象的属性。
# 第一次使用我们需要安装 glom：

import pandas as pd
from glom import glom

df = pd.read_json('./pandas库/006.09.json')

data = df['students'].apply(lambda row: glom(row, 'grade.math'))    # 使用符号： “.” 来访问内嵌对象的属性。


# 写入数据到excel
df.to_excel('./pandas库/006.09.xlsx',sheet_name='sheet1')


# 向现有 Excel 文件追加内容：
with pd.ExcelWriter('./pandas库/006.09.xlsx', mode="a", engine="openpyxl",if_sheet_exists='overlay') as writer:
    data.to_excel(writer, sheet_name="sheet2")       
    # df.to_excel(writer, sheet_name="sheet1")        # 不能在同一个工作表中追加！会抛出异常


print(df)
print('-------------------------------')
print(data)