失败：头文件没装，不过不想装，以后再说。
失败
失败
失败
失败


from pyecharts.charts import Line
from pyecharts import options as opts

# 数据准备
x_axis = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
y_axis = [120, 200, 150, 80, 70, 110, 130]

# 创建折线图对象
line = (
    Line()
    .add_xaxis(x_axis)
    .add_yaxis("销量", y_axis)
    .set_global_opts(title_opts=opts.TitleOpts(title="一周销售量"))
)

# 渲染图表
line.render("line_chart.html")