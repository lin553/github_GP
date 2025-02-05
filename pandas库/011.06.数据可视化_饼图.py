# 饼图 (Pie Chart): 用于展示各部分占总体的比例。

import pandas as pd
import matplotlib.pyplot as plt

# 示例数据
data = {'Category': ['A', 'B', 'C', 'D'],
        'Value': [10, 15, 7, 12]}
df = pd.DataFrame(data)

# 使用DataFrame的plot方法绘制饼图
df.plot(
    kind='pie',  # 指定图表类型为饼图，用于展示各分类的比例关系
    y='Value',   # 设置y轴的数据列，即用来表示每个分类对应的数值大小，'Value'是数值列的名称
    labels=df['Category'],  # 设置饼图各部分的标签，从DataFrame的'Category'列获取标签文本
    autopct='%1.1f%%',  # 显示百分比格式，这里设置为保留一位小数的百分比形式
    title='Category Proportions',  # 设置图表的标题为"Category Proportions"，意为各类别的比例
    figsize=(8, 5)  # 设置图表的尺寸大小，宽度为8英寸，高度为5英寸，但请注意：对于饼图来说，通常指定一个正方形的尺寸效果会更好
)
plt.show()