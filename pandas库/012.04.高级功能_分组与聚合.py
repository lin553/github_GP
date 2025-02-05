# 分组与聚合
    # Pandas 中的 groupby() 方法非常强大，可以用于分组聚合、转换数据和过滤数据。通过 groupby()，
        # 可以将数据根据某些条件分组，进行聚合运算，如求和、均值、计数等。




print("\n\n----------------- 1.groupby() — 数据分组 ------------------")
    # 参数	    说明
    # by	    按照哪个列或索引分组
    # axis	    分组的轴，默认为 0，即按行进行分组
    # level	    按照索引的级别进行分组（适用于 MultiIndex）

import pandas as pd

df = pd.DataFrame({
    'Category': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Value': [10, 20, 30, 40, 50, 60]
})
print("源数据：\n", df,"\n")

# 按照 Category 列进行分组并计算每组的总和
grouped = df.groupby('Category')['Value'].sum()
print("新数据: 列进行分组并计算每组的总和: \n", grouped)





print("\n\n--------------- 2. 聚合操作（agg()）-------------------")
# agg() 用于执行复杂的聚合操作，可以传入多个函数来同时计算多个聚合值。
    # 参数	    说明
    # func	    聚合函数，可以是字符串或自定义函数
import pandas as pd

df = pd.DataFrame({
    'Category': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Value': [10, 20, 30, 40, 50, 60]
})
print("源数据：\n", df,"\n")

# 使用 agg() 来进行多个聚合操作
grouped = df.groupby('Category')['Value'].agg(["sum", "min", "max"])
print("新数据:  \n", grouped)



# ========================== 完 ===========================