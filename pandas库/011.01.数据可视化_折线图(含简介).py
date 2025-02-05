# Pandas 数据可视化
    # 数据可视化是数据分析中的重要环节，它帮助我们更好地理解和解释数据的模式、趋势和关系。
    # 通过图形、图表等形式，数据可视化将复杂的数字和统计信息转化为易于理解的图像，从而便于做出决策。
    # Pandas 提供了与 Matplotlib 和 Seaborn 等可视化库的集成，使得数据的可视化变得简单而高效。
    # 在 Pandas 中，数据可视化功能主要通过 DataFrame.plot() 和 Series.plot() 方法实现，这些方法实际上是对 Matplotlib 库的封装，
        # 简化了图表的绘制过程。



# =================================================================
# 图表类型	    描述	                                   方法
# 折线图	    展示数据随时间或其他连续变量的变化趋势	      df.plot(kind='line')
# 柱状图	    比较不同类别的数据	                        df.plot(kind='bar')
# 水平柱状图	比较不同类别的数据，但柱子水平排列	          df.plot(kind='barh')
# 直方图	    显示数据的分布	                            df.plot(kind='hist')
# 散点图	    展示两个数值型变量之间的关系	             df.plot(kind='scatter', x='col1', y='col2')
# 箱线图	    显示数据分布，包括中位数、四分位数等	      df.plot(kind='box')
# 密度图	    展示数据的密度分布	                        df.plot(kind='kde')
# 饼图	        显示不同部分在整体中的占比	                 df.plot(kind='pie')
# 区域图	    展示数据的累计数值	                        df.plot(kind='area')


# =================================================================
# Pandas 数据可视化的基本功能和方法可以满足大多数日常数据可视化的需求，但若要实现更复杂的可视化，可以结合 Matplotlib 和 Seaborn 使用，
    # 进行更精细的图表定制。

# 一、Pandas 数据可视化概述
    # Pandas 提供的 plot() 方法可以轻松地绘制不同类型的图表，包括折线图、柱状图、直方图、散点图等。plot() 方法有很多参数，
        # 可以定制图表的样式、颜色、标签等。

# 1. 基本的 plot() 方法
    # 参数	        说明
    # kind	        图表类型，支持 'line', 'bar', 'barh', 'hist', 'box', 'kde', 'density', 'area', 'pie' 等类型
    # x	            设置 x 轴的数据列
    # y	            设置 y 轴的数据列
    # title     	图表的标题
    # xlabel	    x 轴的标签
    # ylabel	    y 轴的标签
    # color	        设置图表的颜色
    # figsize	    设置图表的大小（宽, 高）
    # legend	    是否显示图例

# 2. 常用图表类型
    # 图表类型	    描述	                                              常用用法
    # 折线图	    用于显示随时间变化的数据趋势	                        df.plot(kind='line')
    # 柱状图	    用于显示类别之间的比较数据	                            df.plot(kind='bar')
    # 水平柱状图	与柱状图类似，但柱子是水平的	                        df.plot(kind='barh')
    # 直方图	    用于显示数据的分布（频率分布）	                        df.plot(kind='hist')
    # 散点图	    用于显示两个数值变量之间的关系	                        df.plot(kind='scatter', x='col1', y='col2')
    # 箱线图	    用于显示数据的分布、异常值及四分位数	                 df.plot(kind='box')
    # 密度图	    用于显示数据的密度分布	                                df.plot(kind='kde')
    # 饼图	        用于显示各部分占总体的比例	                            df.plot(kind='pie')
    # 区域图	    用于显示累计数值的图表（类似于折线图，但填充了颜色）	   df.plot(kind='area')
# =================================================================



print("------------ 1.折线图 (Line Plot)通常用于展示数据随时间的变化趋势 ---------------")
import pandas as pd
import matplotlib.pyplot as plt

data = {'Year': [2015, 2016, 2017, 2018, 2019, 2020],
        'Sales': [100, 150, 200, 250, 300, 350]}
df = pd.DataFrame(data)
# 使用pandas的plot方法绘制折线图
df.plot(
    kind='line',           # 指定图表类型为折线图
    x='Year',              # 设置x轴数据来源于DataFrame中的'Year'列
    y='Sales',             # 设置y轴数据来源于DataFrame中的'Sales'列
    title='Sales Over Years', # 设置图表标题为"Sales Over Years"
    xlabel='Year',         # 设置x轴标签为"Year"
    ylabel='Sales',        # 设置y轴标签为"Sales"
    figsize=(10, 6)        # 设置图表大小，宽度为10英寸，高度为6英寸
)
plt.show()





# ========================== 完 ===========================