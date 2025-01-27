# 提取xls或xlsx文件转换为csv文件

import pandas as pd
import time

# 开始计时
start_time = time.time()

# 将Excel文件转换为CSV文件
# excel_file_path = input('要转换的文件(含后缀xls或xlsx): ')
excel_file_path = 'AAA_个股_涨幅排名_2025-01月_2025-01-24.xls'
csv_file_path = excel_file_path + '.csv'

# 读取Excel文件（不跳过任何行）
df_excel = pd.read_excel(excel_file_path, sheet_name='提取结果')

# 检测并移除重复的标题行
header_row = df_excel.columns.tolist()
duplicate_header_mask = df_excel.apply(lambda row: row.tolist() == header_row, axis=1)
df_excel = df_excel[~duplicate_header_mask]

# 保存为CSV文件
df_excel.to_csv(csv_file_path, index=False, encoding='utf-8-sig')

# 结束计时并打印耗时
end_time = time.time()
elapsed_time = end_time - start_time
print(f"第一步执行完成，耗时: {elapsed_time:.2f} 秒")