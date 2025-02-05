# 散点图 (Scatter Plot)：图用于展示两个数值变量之间的关系。

import pandas as pd
import matplotlib.pyplot as plt

# 示例数据
data = {'Height': [150, 160, 170, 180, 190],
        'Weight': [50, 60, 70, 80, 90]}
df = pd.DataFrame(data)

# 使用DataFrame的plot方法绘制散点图
df.plot(
    kind='scatter',  # 指定图表类型为散点图
    x='Height',      # 将DataFrame中的'Height'列指定为x轴的数据
    y='Weight',      # 将DataFrame中的'Weight'列指定为y轴的数据
    title='Height vs Weight',  # 设置图表的标题为"Height vs Weight"
    xlabel='Height (cm)',      # 设置x轴的标签为"Height (cm)"，表示单位是厘米
    ylabel='Weight (kg)',      # 设置y轴的标签为"Weight (kg)"，表示单位是千克
    figsize=(8, 5)   # 设置图表的尺寸大小，宽度为8英寸，高度为5英寸
)
plt.show()