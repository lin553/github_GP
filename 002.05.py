import pandas as pd
import time

# 开始计时
start_time = time.time()

# 将Excel文件转换为CSV文件
excel_file_path = 'AAA_个股_涨幅排名_2025-01月_2025-01-24.xls'
csv_file_path = excel_file_path + '.csv'

# 使用 openpyxl 引擎读取 Excel 文件，并分块处理以节省内存
c_size = 10000  # 每次读取的行数
sheet_number = 0  # 假设我们处理第一个工作表
header_row = None  # 存储表头行

with pd.ExcelFile(excel_file_path, engine='openpyxl') as xls:
    for chunk in pd.read_excel(xls, sheet_name=sheet_number, chunksize=c_size):
        if header_row is None:
            header_row = chunk.columns.tolist()
            chunk.to_csv(csv_file_path, mode='w', index=False, encoding='utf-8-sig', header=True)
        else:
            # 检测并移除重复的标题行
            duplicate_header_mask = chunk.apply(lambda row: row.tolist() == header_row, axis=1)
            chunk = chunk[~duplicate_header_mask]
            chunk.to_csv(csv_file_path, mode='a', index=False, encoding='utf-8-sig', header=False)

# 结束计时并打印耗时
end_time = time.time()
elapsed_time = end_time - start_time
print(f"第一步执行完成，耗时: {elapsed_time:.2f} 秒")