import numpy as np
import pandas as pd 
import openpyxl
print(openpyxl.__version__)


# 创建一个包含NaN和无穷大值的DataFrame
df = pd.DataFrame([
    [123, np.nan, 567],
    [456, 789, np.inf],
    [-np.inf, 100, 200]
], columns=["Foo", "Bar", 'abc'])

# 在追加模式下，engine_kwargs 会传递给 openpyxl 的 load_workbook
with pd.ExcelWriter(
    "./pandas库/005.13.xlsm",
    # "./pandas库/005.13.xlsx",   # .xlsx后缀本来就没有vba代码   
    engine="openpyxl",
    mode="a",                           # 设置模式为 'a'（追加），意味着如果文件已存在，则在现有文件中添加新内容而不是覆盖(实际执行时，已存在就报错)
    engine_kwargs={"keep_vba": True}    # 向 openpyxl 引擎传递额外参数，这里指定保留 VBA 宏代码(实际执行时，无法保留sheet1中的vba代码)
) as writer:
    df.to_excel(writer, sheet_name="Sheet2")


# 失败