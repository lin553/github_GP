
from datetime import date, datetime  
import pandas as pd 

df = pd.DataFrame(
    [
        [date(2014, 1, 31), date.today()],
        [datetime(1998, 5, 26, 23, 33, 4), datetime.now()],
    ],
    index=["Date", "Datetime"],
    columns=["X", "Y"],
)  

with pd.ExcelWriter(
    './pandas库/005.08.xlsx',
    date_format="YYYY-MM-DD",
    datetime_format="YYYY-MM-DD HH:MM:SS"
) as writer:
    df.to_excel(writer, sheet_name='sheet1')





df2 = pd.DataFrame(
    [
        ['fuck1', 10086],
        ['fuck2', 10010],
    ],
    index=["Fuck", "times"],
    columns=["X", "Y"],
) 

# 使用 if_sheet_exists 参数替换已存在的工作表
with pd.ExcelWriter(
    './pandas库/005.08.xlsx',
    mode="a",
    engine="openpyxl",
    if_sheet_exists="replace",
) as writer:
    df2.to_excel(writer, sheet_name="sheet1")