# 透视表
    # 透视表（Pivot Table）是一个特殊的聚合方式，可以让我们通过行、列和聚合函数对数据进行快速汇总，类似于 Excel 中的透视表。

# 实例
   	        	                                        	                                                                    
    # 操作:     创建透视表			        
    # 方法:     df.pivot_table(values, index, columns, aggfunc)
    # 说明:     用指定的列进行行、列分类汇总，values 是需要聚合的值，aggfunc 是聚合函数
    # 示例      df.pivot_table(values='Salary', index='Department', aggfunc='mean')
# =========================================================================


import pandas as pd

data = {'Department': ['HR', 'Finance', 'HR', 'IT', 'IT'],
        'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Salary': [50000, 60000, 55000, 70000, 75000]
}
df = pd.DataFrame(data)

print("\n-------------- 1.使用 pivot_table 计算每个部门的薪资平均值 ---------------")
pivot_table = df.pivot_table(values='Salary', index='Department', aggfunc='mean')
print(pivot_table)

print("\n---------------- 2.源数据 -----------------")
print(df)