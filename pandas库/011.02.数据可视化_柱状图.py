# 柱状图 (Bar Chart)
    # 柱状图用于展示不同类别之间的比较，尤其适用于离散数据。

import pandas as pd
import matplotlib.pyplot as plt

# 示例数据
data = {'Category': ['A', 'B', 'C', 'D'],
        'Value': [10, 15, 7, 12]}
df = pd.DataFrame(data)

# 使用pandas的plot方法绘制柱状图
df.plot(
    kind='bar',            # 指定图表类型为柱状图
    x='Category',          # 设置x轴为"Category"列，表示不同类别的分布
    y='Value',             # 设置y轴为"Value"列，表示每个类别的数值大小
    title='Category Values', # 设置图表标题为"Category Values"
    xlabel='Category',     # 设置x轴标签为"Category"
    ylabel='Value',        # 设置y轴标签为"Value"
    figsize=(8, 5)         # 设置图表尺寸，宽度为8英寸，高度为5英寸
)
plt.show()
