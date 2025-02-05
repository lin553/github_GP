# 直方图 (Histogram)：用于显示数据的分布，特别是用于描述数据的频率分布。

import pandas as pd
import matplotlib.pyplot as plt

# 示例数据
data = {'Scores': [55, 70, 85, 90, 60, 75, 80, 95, 100, 65]}
df = pd.DataFrame(data)
# 使用DataFrame的plot方法绘制直方图
df.plot(
    kind='hist',     # 指定图表类型为直方图
    y='Scores',      # 将DataFrame中的'Scores'列指定为y轴的数据，即要分析其分布的数据
    bins=5,          # 将数据划分为5个区间（柱状体），也可以根据数据的分布自行调整这个数值
    title='Scores Distribution',  # 设置图表的标题为"Scores Distribution"，表示这是分数的分布情况
    xlabel='Scores', # 设置x轴的标签为"Scores"，表示x轴展示的是分数信息
    figsize=(8, 5)   # 设置图表的尺寸大小，宽度为8英寸，高度为5英寸
)
plt.show()