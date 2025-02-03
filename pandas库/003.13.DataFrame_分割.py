# DataFrame 的合并与分割

import pandas as pd

# 通过字典创建 DataFrame
df = pd.DataFrame({'Column1': [1, 2, 3], 'Column2': [4, 5, 6], 'Column3': [7, 8, 9]})
print('df: \n', df)
# ===============================================================================



print('\n-------------- 1.分割：使用 pivot: 长格式转宽格式 ----------------')
df_pivot = df.pivot(index='Column1', columns='Column2', values='Column3')   # 将原来3*3的矩阵分割成：对角方阵， 即： 
                                                                                                                # 行：index
                                                                                                                # 列：columns
                                                                                                                # 行：values
print("df.pivot(index='Column1', columns='Column2', values='Column3')  \n即：将矩阵分割成对角方阵：\n\n",df_pivot)



print('\n\n-------------- 2.分割：使用 melt: 宽格式转长格式 ----------------')
df_melt = df.melt(id_vars='Column1', value_vars=['Column2', 'Column3'])
print('df.melt(id_vars=\'Column1\', value_vars=[\'Column2\', \'Column3\']): \n\n', df_melt)