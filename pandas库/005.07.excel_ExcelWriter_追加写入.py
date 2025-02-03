
from datetime import date, datetime  
import pandas as pd 

# print(date.today())
# print(datetime.now())


df = pd.DataFrame(
    [
        [date(2014, 1, 31), date.today()],
        [datetime(1998, 5, 26, 23, 33, 4), datetime.now()],
    ],
    index=["Date", "Datetime"],
    columns=["X", "Y"],
)  

with pd.ExcelWriter(
    './pandas库/005.07.xlsx',
    date_format="YYYY-MM-DD",
    datetime_format="YYYY-MM-DD HH:MM:SS"
) as writer:
    df.to_excel(writer, sheet_name='sheet1')


# 向现有 Excel 文件追加内容：
with pd.ExcelWriter('./pandas库/005.07.xlsx', mode="a", engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name="sheet2")       
    # df.to_excel(writer, sheet_name="sheet1")        # 不能在同一个工作表中追加！会抛出异常
    