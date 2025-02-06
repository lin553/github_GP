print("\n\n--------------- 6.使用分块加载大数据集: chunksize 参数，允许在读取 CSV 或 Excel 文件时分块加载数据 ---------------")
# 当数据集过大时，加载整个数据集会占用大量内存，甚至导致内存溢出。此时，可以通过分块读取数据来减小内存压力。
# Pandas 提供了 。chunksize 参数，允许在读取 CSV 或 Excel 文件时分块加载数据

import pandas as pd

# # 创建索引并进行查找
# df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8]})
# print("源数据: \n", df, "\n")

# 分块读取 CSV 文件
chunksize = 10000
for chunk in pd.read_csv('./pandas库/013.06.csv', chunksize=chunksize):
    print(chunk)        # 对每个数据块进行处理

