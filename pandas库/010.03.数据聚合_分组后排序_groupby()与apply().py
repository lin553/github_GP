# 分组后的排序
    # 聚合后的数据可以进一步按某列的值进行排序，这样可以找出特定组中最重要的值。       	                                                    	                             
    # 方法:	df.groupby(by).apply(lambda x: x.sort_values(by='col'))	    
    # 说明: 在每个分组内部按照某列的值进行排序。	
    # 示例: df.groupby('Department').apply(lambda x: x.sort_values(by='Salary', ascending=False))    其中：ascending=False 是降序
# ===============================================================

import pandas as pd

data = {'Department': ['HR', 'Finance', 'HR', 'IT', 'IT'],
        'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Salary': [50000, 60000, 55000, 70000, 75000]
}
df = pd.DataFrame(data)

print("\n-------------- 1.按照部门分组后, 按薪资降序排序 -----------------: ")
grouped_sorted = df.groupby('Department').apply(lambda x: x.sort_values(by='Salary', ascending=False))
print(grouped_sorted)


print("\n--------------- 2.源数据 -----------------: ")
print(df)