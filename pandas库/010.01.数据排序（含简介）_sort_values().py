# Pandas 数据排序与聚合
    # 数据排序与聚合是数据分析中非常常见且重要的操作，特别是在大数据集中的数据分析时。
    # 排序帮助我们按特定标准对数据进行排列，而聚合则让我们对数据进行汇总，计算出各种统计量。

# Pandas 提供了强大的排序和聚合功能，能够帮助分析人员高效地处理数据。
# 操作	        方法	                        说明	                                        常用函数/方法
    # 排序	        sort_values(by, ascending)	    根据某列的值进行排序，ascending 控制升降序	  df.sort_values(by='column')
    # 排序	        sort_index(axis)	            根据行或列的索引进行排序	                 df.sort_index(axis=0)
    # 分组聚合	    groupby(by)	                    按照某列进行分组后，应用聚合函数	          df.groupby('column')
    # 聚合函数	    agg()	                        聚合函数，如 sum()、mean()、count() 等	     df.groupby('column').agg({'value': 'sum'})
    # 多重聚合	    agg([func1, func2])	            对同一列应用多个聚合函数	                  df.groupby('column').agg({'value': ['mean', 'sum']})
    # 分组后排序	apply(lambda x: x.sort_values(...))	在分组后进行排序	                     df.groupby('column').apply(lambda x: x.sort_values(...))
    # 透视表	    pivot_table()	                创建透视表，根据行、列进行数据汇总	



# =================================================================
# 一、数据排序（Sorting）
    # 排序是指将数据按某个列的值进行升序或降序排列。Pandas 提供了两种主要的方法来进行排序：sort_values() 和 sort_index()。

# 排序方法
    # sort_values()：根据列的值进行排序。
    # sort_index()：根据行或列的索引进行排序。

# 实例
    # 操作	        方法	                        说明	                                                    示例
    # 按值排序	    df.sort_values(by, ascending)	按照指定的列（by）排序，ascending 控制升序或降序，默认为升序	df.sort_values(by='Age', ascending=False)
    # 按索引排序	df.sort_index(axis)	            按照行或列的索引排序，axis 控制按行或列排序	                   df.sort_index(axis=0)


# =================================================================
import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'Salary': [50000, 60000, 70000, 80000]}
df = pd.DataFrame(data)

print("\n按照 'Age' 列的值进行降序排序:")
df_sorted = df.sort_values(by='Age', ascending=False)  
print(df_sorted)

print("\n按照行索引进行排序:")
df_sorted_by_index = df.sort_index(axis=0)   
print(df_sorted_by_index)

print("\n源数据：")
print(df)



# ========================== 完 ===========================