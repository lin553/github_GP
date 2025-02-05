# Pandas 提供了非常强大的数据操作功能，适用于复杂的数据清洗、分析、聚合和时间序列处理等任务。
    # 掌握 Pandas 的高级功能，可以大大提高数据处理和分析的效率。

# =============================================================
# 数据合并与连接
    # Pandas 提供了多个方法来合并和连接不同的 DataFrame，例如 merge()、concat() 和 join()。这些方法常用于处理多个数据集和复杂的合并任务。

# =============================================================


print("\n\n------------------- 1. merge() 数据库风格的连接 -------------------")
# merge() 方法允许根据某些列对两个 DataFrame 进行合并，类似 SQL 中的 JOIN 操作。支持内连接、外连接、左连接和右连接。
    # 参数	    说明
    # left	    左侧 DataFrame
    # right	    右侧 DataFrame
    # how	    合并方式，支持 'inner', 'outer', 'left', 'right'
    # on	    连接的列名（如果两侧列名不同，可使用 left_on 和 right_on）
    # left_on	左侧 DataFrame 的连接列
    # right_on	右侧 DataFrame 的连接列
    # suffixes	添加后缀，以区分重复的列名
import pandas as pd

# 示例数据
left = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']})
right = pd.DataFrame({'ID': [1, 2, 4], 'Age': [24, 27, 22]})
print("left:\n",left)
print("\nright:\n",right)
print()
# 使用 merge 进行内连接
result = pd.merge(
        left,      # left 和 right：这两个参数是你希望合并的源DataFrame。在实际应用中，它们应该是已经定义好的DataFrame变量。
        right, 
        on='ID',     # on='ID'：这个参数指定了一个或多个用于连接的列名。在这个例子中，'ID'是left和right两个DataFrame中共有的列，将用作合并的关键字。
        how='inner'  # how='inner'：指定连接的方式。这里使用的inner表示内连接，意味着结果DataFrame中只包含那些在left和right DataFrame中'ID'值都存在的行。除了inner，还有left、right和outer三种连接方式，分别代表左外连接、右外连接和全外连接。
        )
print("merge内连接: ")
print(result)





print("\n\n------------------- 2.concat() 沿轴连接 -------------------")
# concat() 用于将多个 DataFrame 沿指定轴（行或列）进行连接，常用于行合并（垂直连接）或列合并（水平连接）。
    # 参数	        说明
    # objs	        需要合并的 DataFrame 列表
    # axis	        合并的轴，0 表示按行合并，1 表示按列合并
    # ignore_index	是否忽略索引，重新生成索引（默认为 False）
    # keys	        为合并的对象提供层次化索引

import pandas as pd

df1 = pd.DataFrame({'A': [1, 2, 3]})
df2 = pd.DataFrame({'A': [4, 5, 6]})
print("df1: \n",df1)
print("\ndf2: \n",df2)
# 行合并
result = pd.concat([df1, df2], axis=0, ignore_index=True)   # ignore_index=True: 忽略索引，重新生成索引
                                                            # axis=0: 表示按行合并
print("\n行合并: \n")
print(result)








print("\n\n------------------- 3. join()  基于索引连接 -------------------")
# join() 方法是 Pandas 中的简化连接操作，通常用于基于索引将多个 DataFrame 连接。
    # 参数	    说明
    # other	    需要连接的另一个 DataFrame
    # how	    合并方式，支持 'left', 'right', 'outer', 'inner'
    # on	    使用的连接列，默认基于索引

# 注意事项
    # join方法默认是基于索引来连接DataFrame的。如果你想要基于某一列而不是索引来连接，可以先设置那列为索引（例如使用set_index方法），
            # 或者考虑使用merge方法，后者提供了更多的灵活性用于指定连接键。
    # 使用join时，如果两个DataFrame有相同的列名（除了用于连接的索引之外），结果DataFrame中这些列将被保留，可能导致一些混淆。在这种情况下，
            # 你可能需要重命名这些列或使用merge函数以获得更精确的控制。

import pandas as pd

left = pd.DataFrame({'A': [1, 2, 3]}, index=[1, 2, 3])
right = pd.DataFrame({'B': [4, 5, 6]}, index=[1, 2, 4])

print("left: \n", left)
print("\nright: \n", right)

# 使用 join 进行连接
result = left.join(right, how='inner')  # how='inner'：指定了连接的方式。这里的inner表示内连接，意味着只有那些在两个DataFrame的索引中都
                                                     # 存在的项才会出现在结果中。其他可用的连接方式包括：
                                                            # 'left'：左连接，保留左边DataFrame的所有索引，
                                                                    # 即使它们在右边DataFrame中没有匹配项。
                                                            # 'right'：右连接，保留右边DataFrame的所有索引，
                                                                    # 即使它们在左边DataFrame中没有匹配项。
                                                            # 'outer'：全外连接，保留两个DataFrame中的所有索引，
                                                                    # 并对没有匹配项的位置填充缺失值（NaN）。
print("\njoin连接: ")
print(result)
print("\n这里的结果只包含了left和right DataFrame中索引相同的行（即索引为2和3的行），因为使用的是how='inner'，即内连接。\n")





# ========================== 完 ===========================