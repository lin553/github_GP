# 提取xls或xlsx文件转换为csv文件

import pandas as pd
import time

# 开始计时
start_time = time.time()

# 将Excel文件转换为CSV文件
your_excel_file = input('要转换的excel文件(包含xlsx或xls后缀): ')
excel_file_path = your_excel_file
csv_file_path = your_excel_file + '.csv'

# 读取Excel文件
df_excel = pd.read_excel(excel_file_path, sheet_name='提取结果')

# 保存为CSV文件
df_excel.to_csv(csv_file_path, index=False, encoding='utf-8-sig')
print(f"Excel文件已转换并保存为{csv_file_path}")


# 结束计时并打印耗时
end_time = time.time()
elapsed_time = end_time - start_time
print(f"转换csv文件，执行完成，耗时: {elapsed_time:.2f} 秒")