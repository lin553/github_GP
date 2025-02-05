# Seaborn 可视化
    # Seaborn 是基于 Matplotlib 的高级数据可视化库，提供了更漂亮、更易用的图表和更丰富的统计图表类型。
    # 在 Pandas 中，可以直接与 Seaborn 配合使用。


# =================================================================
print("\n\n----------------- 1.热力图（Heatmap）-----------------")
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
df = pd.DataFrame(data)

# 使用seaborn的heatmap函数基于数据框的相关系数矩阵生成：热图
sns.heatmap(
    df.corr(),  # 计算DataFrame数值列之间的相关系数矩阵，并作为热图的数据来源
    annot=True,  # 在每个单元格内显示具体数值（即相关系数）
    cmap='coolwarm'  # 指定颜色映射方案，这里使用的是'coolwarm'，一种从冷色调到暖色调的颜色映射
)
plt.show()



print("\n\n----------------- 2.数据集中所有数值特征之间的散点图矩阵 -----------------")
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}     # 创建数据字典
df = pd.DataFrame(data) # 将数据字典转换为DataFrame
sns.pairplot(df)    # 使用seaborn的pairplot函数绘制DataFrame中各变量的成对关系图
plt.show()