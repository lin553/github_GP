print("\n\n----------------- 1.相关性热图(Correlation Heatmap) --------------------")
# 相关性热图（Correlation Heatmap）
    # 为了更直观地呈现相关性矩阵，可以使用热图（Heatmap）来可视化各个变量之间的相关性。
    # 使用 seaborn 库绘制相关性热图是一个常见的做法。

# 示例数据
import seaborn as sns               # 导入seaborn库，用于高级数据可视化，别名为sns
import matplotlib.pyplot as plt     # 导入matplotlib.pyplot模块，用于创建图表，别名为plt
import pandas as pd                 # 导入pandas库，用于数据处理和分析，别名为pd

# 定义一个字典，包含'Height'(身高)、'Weight'(体重)和'Age'(年龄)的数据
data = {
    'Height': [150, 160, 170, 180, 190], 
    'Weight': [45, 55, 65, 75, 85], 
    'Age': [20, 25, 30, 35, 40] 
}
df = pd.DataFrame(data)     # 使用pandas的DataFrame方法将字典转换为DataFrame格式，便于数据分析
plt.figure(figsize=(8, 6))  # 创建一个图表对象，并指定图表大小（宽度8英寸，高度6英寸）

# 使用seaborn的heatmap方法绘制相关性热图。
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.4f', vmin=-1, vmax=1)     # df.corr()计算DataFrame中各列之间的相关系数矩阵；
                                                                                    # annot=True表示在单元格中显示数值；
                                                                                    # cmap='coolwarm'设置颜色方案；
                                                                                    # fmt='.2f'指定显示的数值格式保留两位小数；
                                                                                    # vmin=-1, vmax=1设定颜色条的范围从-1到1，
                                                                                                   # 代表完全负相关到完全正相关。
plt.title('Correlation Heatmap')        # 设置图表标题为'Correlation Heatmap'
plt.show()

# 说明：sns.heatmap() 绘制相关性热图，  annot=True 表示在热图上显示数值，
     # cmap='coolwarm' 设置颜色范围，   vmin=-1, vmax=1 限制颜色范围为 -1 到 1。






print("\n\n----------------- 2.可视化相关性 --------------------")
# 可视化相关性
    # 这里我们要使用 Python 的 Seaborn 库， Seaborn 是一个基于 Matplotlib 的数据可视化库，专注于统计图形的绘制，旨在简化数据可视化的过程。
    # Seaborn 提供了一些简单的高级接口，可以轻松地绘制各种统计图形，包括散点图、折线图、柱状图、热图等，而且具有良好的美学效果。

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 创建一个示例数据框
data = {'A': [1, 2, 3, 4, 5], 'B': [5, 4, 3, 2, 1]}
df = pd.DataFrame(data)

# 计算 Pearson 相关系数: 相关性矩阵
correlation_matrix = df.corr()
# 使用热图可视化 Pearson 相关系数
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")     # correlation_matrix: 计算DataFrame中各列之间的相关系数矩阵；
                                                                            # annot=True表示在单元格中显示数值；
                                                                            # cmap='coolwarm'设置颜色方案；
                                                                            # fmt='.2f'指定显示的数值格式保留两位小数；
plt.show()





# ========================== 完 ===========================