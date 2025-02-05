# DataFrame 的合并与分割

import pandas as pd

# 通过字典创建 DataFrame
df1 = pd.DataFrame({'Column1': [1, 2, 3], 'Column2': [4, 5, 6]})
print('df1: \n', df1)

s1 = pd.Series(['Alice', 'Bob', 'Charlie'])
s2 = pd.Series([25, 30, 35])
s3 = pd.Series(['New York', 'Los Angeles', 'Chicago'])
s4 = pd.Series([1, 2, 3])
df2 = pd.DataFrame({'Name':s1, 'Age':s2, 'City':s3, 'Column1':s4})
print('\n df2: \n', df2)
# ===============================================================================




print('\n-------------- 1.合并：使用 concat 方法：纵向合并 ----------------')
print('pd.concat([df1, df2], ignore_index=True): \n', pd.concat([df1, df2], ignore_index=True))     
                            #ignore_index 是 Pandas 中一些方法的一个参数，比如 pd.concat()、DataFrame.groupby().apply() 等。
                                # 这个参数决定了在执行这些操作后是否忽略原有的索引，创建一个新的默认整数索引（从 0 开始递增）。
                                    # 参数解释
                                        # ignore_index=False（默认值）：保持原有的索引。这意味着输出的数据结构会保留输入数据的索引。
                                        # ignore_index=True：忽略原有的索引，并用一个全新的、连续的整数索引替换它。


print('\n-------------- 2.合并：使用 merge 方法：横向合并 ----------------')
print('pd.merge(df1, df2, on=\'Column1\'): \n', pd.merge(df1, df2, on='Column1'))  # df1 与 df2 要有同一列 “Column1” , 否则报错。





# ========================== 完 ===========================