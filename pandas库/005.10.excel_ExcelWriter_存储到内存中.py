import pandas as pd 
import io

df = pd.DataFrame([["ABC", "XYZ"]], columns=["Foo", "Bar"])

buffer = io.BytesIO()     # io.BytesIO() 是 Python 标准库 io 模块中提供的一个类，它提供了一种通过内存来模拟二进制文件（bytes）操作
                                        # 的方式。这意味着你可以像操作一个常规的文件对象一样使用 BytesIO 对象来进行读写操作，但所有
                                        # 数据实际上都是存储在内存中的，而不是磁盘上的文件。

# 将 Excel 文件存储在内存中
with pd.ExcelWriter(buffer) as writer:       
    df.to_excel(writer)

print(df)
writer.close()