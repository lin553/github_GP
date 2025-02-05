# 透视表与交叉表
    # Pandas 提供了 pivot_table() 方法来创建透视表，和 crosstab() 方法来计算交叉表。透视表和交叉表都非常适合数据的汇总和重新排列。





print("\n\n------------------- 1. pivot_table() — 创建透视表 ---------------------")
    # 参数	        说明
    # data	        输入的数据
    # values	    要汇总的列
    # index	        用作行索引的列
    # columns	    用作列索引的列
    # aggfunc	    聚合函数，默认为 mean，可以是 sum, count 等
    # fill_value	填充缺失值

import pandas as pd

data = {'Date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04'],
        'Category': ['A', 'B', 'A', 'B'],
        'Sales': [100, 150, 200, 250]}
df = pd.DataFrame(data)
print(df)
print()

# 创建透视表
pivot_table = pd.pivot_table(df, values='Sales', index='Date', columns='Category', aggfunc='sum', fill_value=0)

# 使用pandas库中的pivot_table函数创建一个透视表
    # pivot_table将会是一个新的DataFrame，它以'Date'为行，'Category'为列，
    # 并且在相应的交叉点上显示了对应日期和类别的销售额总和。如果某个交叉点没有原始数据，则用0填充。
pivot_table = pd.pivot_table(
    df,                 # 源DataFrame，包含需要分析的数据
    values='Sales',     # 指定用于聚合计算的列名，在这里为'Sales'（销售额）
    index='Date',       # 指定作为透视表 行 标签的列，这里使用'Date'（日期），意味着每种日期将对应一行       
    columns='Category', # 指定作为透视表 列 标签的列，这里使用'Category'（类别），意味着每个类别将对应一列
    aggfunc='sum',      # 指定聚合函数，这里使用'sum'表示对给定的'Date'和'Category'组合求销售额的总和
    fill_value=0        # 对于没有数据的单元格，使用该值进行填充。这里设置为0，意味着任何缺失的销售数据将被视为0
)
print(pivot_table)







print("\n\n------------------- 2.crosstab() — 创建交叉表 ---------------------")
    # 参数	    说明
    # index	    行标签
    # columns	列标签
    # values	用于计算的数据（可选）
    # aggfunc	聚合函数，默认 count
import pandas as pd

# 示例数据
data = {'Category': ['A', 'B', 'A', 'B', 'A', 'B'],
        'Region': ['North', 'South', 'North', 'South', 'West', 'East']}
df = pd.DataFrame(data)
print(df)
print()

# 创建交叉表：基于df，统计每个'Category'与'Region'组合出现的频数
# 第一个参数df['Category']指定行分类变量；第二个参数df['Region']指定列分类变量，结果表格展示不同类别和区域组合的计数
cross_table = pd.crosstab(df['Category'], df['Region'])  

print(cross_table)




# ========================== 完 ===========================