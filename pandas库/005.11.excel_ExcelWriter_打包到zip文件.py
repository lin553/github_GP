import pandas as pd 
import zipfile  


df = pd.DataFrame([["ABC", "XYZ"]], columns=["Foo", "Bar"])  


file_path = '005.11.xlsx'       # zf.open(file_path, "w") 中的 file_path 应该是相对于压缩文件内部的路径，而不是你的本地文件系统路径。
zip_path = './pandas库/005.11.zip'


# 将 Excel 文件打包到 zip 压缩文件中
with zipfile.ZipFile(zip_path, "w") as zf:
    with zf.open(file_path, "w") as buffer:
        with pd.ExcelWriter(buffer) as writer:
            df.to_excel(writer)