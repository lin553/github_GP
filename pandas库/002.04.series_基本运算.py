


import pandas as pd
import numpy as np  # 数学函数


series = pd.Series([1,2,3,4])
print('series: \n',series)


print('\n------------1---------------')
result = series * 2  # 所有元素乘以2
print('result: \n',result)


print('\n------------2---------------')
# 过滤
filtered_series = series[series > 2]  # 选择大于2的元素
print('filtered_series: \n',filtered_series)
print('\n series > 2: \n', series > 2)


print('\n------------3---------------')
result_sqrt = np.sqrt(series)  # 对每个元素取平方根
print('result_sqrt: \n',result_sqrt)




# ========================== 完 ===========================