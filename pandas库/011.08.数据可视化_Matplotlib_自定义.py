# Matplotlib 高级自定义
    # 除了使用 Pandas 提供的 plot() 方法外，Matplotlib 还可以提供更灵活的自定义功能，例如添加标题、标签、设置图表风格、调整坐标轴等。


import pandas as pd                 # 数据处理库，用于数据操作和分析
import seaborn as sns               # 基于matplotlib的数据可视化库，这里未直接使用，但通常与matplotlib一起使用增强图形效果
import matplotlib.pyplot as plt     # Matplotlib的一个子库，提供了一套面向对象的绘图接口

# 创建一个包含年份和对应销售额的数据字典
data = {'Year': [2015, 2016, 2017, 2018, 2019],
        'Sales': [100, 150, 200, 250, 300]}


df = pd.DataFrame(data)     # 将数据字典转换为DataFrame对象，方便数据处理和分析

# 使用matplotlib绘制折线图，展示销售额随时间的变化趋势
plt.plot(
         df['Year'],    # x轴
         df['Sales'],   # y轴 
         color='blue',  # 设置线条颜色为蓝色
         marker='o'     # 数据点标记为圆形
         )  

# 自定义图表标题和坐标轴标签
plt.title('Sales Over Years')  # 设置图表标题为'Sales Over Years'
plt.xlabel('Year')             # X轴标签设为'Year'
plt.ylabel('Sales')            # Y轴标签设为'Sales'

plt.grid(True)                 # 启用网格线，使图表更易于阅读

plt.show()  # 显示图表: 调用show函数以弹出窗口形式展示绘制好的图表



# ========================== 完 ===========================