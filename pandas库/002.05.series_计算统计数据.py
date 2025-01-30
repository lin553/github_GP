import pandas as pd

s = pd.Series([1, 2, 3, 4])
print('s: \n',s,'\n')
print('s.sum()', s.sum())  # 输出 Series 的总和
print('s.mean()',s.mean())  # 输出 Series 的平均值
print('s.max()',s.max())  # 输出 Series 的最大值
print('s.min()',s.min())  # 输出 Series 的最小值
print('s.std():标准差: ',s.std())  # 输出 Series 的标准差