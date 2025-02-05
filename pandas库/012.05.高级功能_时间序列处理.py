# 时间序列处理
    # Pandas 提供了强大的时间序列处理功能，包括日期解析、频率转换、日期范围生成、时间窗口操作等。




print("\n\n--------------- 1.date_range() — 生成时间序列 -------------------")
    # 参数	    说明
    # start	    起始日期
    # end	    结束日期
    # periods	生成的时间点数
    # freq	    频率（如 D 表示天，H 表示小时等）
import pandas as pd

# 生成时间序列： 使用pd.date_range函数生成一个DatetimeIndex对象
date_range = pd.date_range(
                            start='2024-01-01', # start='2024-01-01' 指定时间序列的起始日期为2024年1月1日
                            periods=5,          # periods=5 指定生成的时间序列包含5个日期
                            freq='D'            # freq='D' 指定频率为每天（'D'代表每日）
                            )
print(date_range)





print("\n\n--------------- 2.日期和时间的偏移， 使用 pd.Timedelta() 可以进行时间的加减操作 -------------------")
import pandas as pd
from datetime import date

date = pd.to_datetime(date.today())
print("today: ", date)

# 日期偏移
new_date = date + pd.Timedelta(days=10)
print("日期偏移: ",new_date)




print("\n\n\n--------------- 3.时间窗口操作（Rolling, Expanding）-------------------")
# 使用 rolling() 和 expanding() 方法进行滚动和扩展窗口操作，常用于时间序列中的移动平均等计算。
    # 方法	        说明
    # rolling()	    计算滚动窗口操作，常用于移动平均等
    # expanding()	计算扩展窗口操作，累计值

import pandas as pd

df = pd.DataFrame({'Value': [10, 20, 30, 40, 50]})
print("源数据：\n", df,"\n")

df.loc[:,'Rolling_Mean'] = df['Value'].rolling(window=3).mean()     # df中新建一列'Rolling_Mean'，用于存储 “3天滚动平均数”
print("计算 3 天滚动平均: \n", df)



# ========================== 完 ===========================