from datetime import date, datetime  
import pandas as pd 
import os

df1 = pd.DataFrame(
    [
        [date(2014, 1, 31), date.today()],
        [datetime(1998, 5, 26, 23, 33, 4), datetime.now()],
    ],
    index=["Date", "Datetime"],
    columns=["X", "Y"],
)  

df2 = pd.DataFrame(
    [
        ['fuck1', 10086],
        ['fuck2', 10010],
    ],
    index=["Fuck", "times"],
    columns=["X", "Y"],
) 


# 定义文件路径
file_path = './pandas库/005.09.xlsx'

# 检查文件是否存在，如果不存在则创建一个新文件
if not os.path.exists(file_path):
    # 创建一个新的Excel文件
    with pd.ExcelWriter(file_path, engine="openpyxl") as writer:
        pass  # 只是创建文件，不需要写入内容



# 向同一个工作表写入多个 DataFrame，注意 if_sheet_exists 参数需要设置为 overlay：
with pd.ExcelWriter(
    file_path,
    mode="a",
    engine="openpyxl",
    if_sheet_exists="overlay",
) as writer:
    df1.to_excel(writer, sheet_name="Sheet1")
    df2.to_excel(writer, sheet_name="Sheet1", startcol=3)


    

# ========================== 完 ===========================