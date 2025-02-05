# 数据聚合（Aggregation）
    # 聚合是将数据按某些规则进行汇总，通常是对某些列的数据进行求和、求平均数、求最大值、求最小值等操作。Pandas提供了groupby()方法来
        # 对数据进行分组，然后应用不同的聚合函数。

# 聚合方法
    # groupby()：按某些列分组。

# 聚合函数：
    # 如 sum(), mean(), count(), min(), max(), std() 等。

# 实例
# 操作	           方法	                                说明	                                                        示例
# 按列分组并聚合	df.groupby(by).agg()	            按指定列（by）进行分组，agg() 可以传入不同的聚合函数，进行多种操作   df.groupby('Department').agg({'Salary': 'mean'})
# 多重聚合函数应用	df.groupby(by).agg([func1, func2])	可以对同一列应用多个聚合函数，返回多种聚合结果	                    df.groupby('Department').agg({'Salary': ['mean', 'sum']})


# =================================================
import pandas as pd

data = {'Department': ['HR', 'Finance', 'HR', 'IT', 'IT'],
        'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Salary': [50000, 60000, 55000, 70000, 75000]
}
df = pd.DataFrame(data)

print("\n------------ 1.按照部门分组, 并计算每个部门的平均薪资 --------------")
grouped = df.groupby('Department')['Salary'].mean()
print(grouped)


print("\n------------- 2.按照部门分组, 并计算每个部门的薪资的平均值和总和 -----------------")
grouped_multiple = df.groupby('Department').agg({'Salary': ['mean', 'sum']})
print(grouped_multiple)


print("\n-------------- 3.源数据 ---------------")
print(df)