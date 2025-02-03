import pandas as pd


# 通过字典创建 DataFrame
df = pd.DataFrame({'Column1': [1, 2, 3], 'Column2': [4, 5, 6], 'Name':['fuck1','fuck2','fuck3']})
print(df)



print('\n-------------- 1.直接对列进行赋值 ----------------')
df['Column1'] = [10, 11, 12]
print(df)


print('\n-------------- 2.添加新列，给新列赋值 ----------------')
df['NewColumn'] = [100, 200, 300]
print(df)


print('\n-------------- 3.添加新行：使用 loc 方法 ----------------')
df.loc[3] = [13, 14, 15, 16]
print(df)


print('\n-------------- 4.添加新行：使用 append(已经被标记为弃用) 方法 ----------------')
# new_row = {'Column1': 13, 'Column2': 14, 'Name':'fuck4', 'NewColumn': 16}
# df = df.append(new_row, ignore_index=True)        #append() 方法在 pandas 版本 1.4.0 中已经被标记为弃用，并将在未来的版本中被移除，
                                                    # 官方推荐使用 concat() 作为替代方法来进行数据的合并操作

# print(df)

print('\n-------------- 5.添加新行：使用 concat 方法 ----------------')
# concat() 方法用于合并两个或多个 DataFrame，当你想要添加一行到另一个 DataFrame 时，可以将新行作为一个新的 DataFrame，然后使用 concat()：
new_row = pd.DataFrame([[4, 7]], columns=['A', 'B'])  # 创建一个只包含新行的DataFrame
df = pd.concat([df, new_row], ignore_index=True)  # 将新行添加到原始DataFrame
                                                  # ignore_index 是 Pandas 中一些方法的一个参数，比如 pd.concat()、DataFrame.groupby().apply() 等。
                                                        # 这个参数决定了在执行这些操作后是否忽略原有的索引，创建一个新的默认整数索引（从 0 开始递增）。
                                                        # 参数解释
                                                            # ignore_index=False（默认值）：保持原有的索引。这意味着输出的数据结构会保留输入数据的索引。
                                                            # ignore_index=True：忽略原有的索引，并用一个全新的、连续的整数索引替换它。
print(df)