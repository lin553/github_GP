# to_csv 常用参数:

# 参数	            说明	                                                        默认值
# path_or_buffer	CSV 文件的路径或文件对象（支持文件路径、文件对象）	                必需参数
# sep	            定义字段分隔符，默认是逗号（,），可以改为其他字符，如制表符（\t）	 ','
# index	            是否写入行索引，默认 True 表示写入索引	                          True
# columns	        指定写入的列，可以是列的名称列表	                              None
# header	        是否写入列名，默认 True 表示写入列名，设置为 False 表示不写列名	    True
# mode	            写入文件的模式，默认是 w（写模式），可以设置为 a（追加模式）	    'w'
# encoding	        文件的编码格式，如 utf-8，latin1 等	                             None
# line_terminator	定义行结束符，默认为 \n	                                         None
# quoting	        设置如何对文件中的数据进行引号处理（0-3，具体引用方式可查文档）	     None
# quotechar	        设置用于引用的字符，默认为双引号 "	                              '"'
# date_format	    自定义日期格式，如果列包含日期数据，则可以使用此参数指定日期格式	 None
# doublequote	    如果为 True，则在写入时会将包含引号的文本使用双引号括起来	        True
# ====================================================================


import pandas as pd


data = {'Name':['Google', 'Runoob', 'Wiki'], 'Age':[10, 12, 13], 'City':['New York', 'Angeles', 'Chicago'] }
df = pd.DataFrame(data)

# 默认覆盖旧文件
df.to_csv('./pandas库/004.02.csv', index=False, header=True, columns=['Name', 'Age', 'City'], mode='a')   # header=True: 写入字段名
                                                                                                          # index=False: 不写入索引号
                                                                                                          # columns： 字段名
                                                                                                          # mode='a': 追加模式
print(df)   # 已经去掉重复行了