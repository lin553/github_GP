# 分块读取和处理CSV文件（从第二行开始，并显示计算时长）
# 去掉百分号、亿字和'--'符号


import pandas as pd
import time
def clean_column(column):
    """
    清理整个列的数据。
    去掉百分号、亿字和'--'符号。
    """
    if column.dtype == object:
        # 处理百分号
        mask_percent = column.str.contains('%', na=False)
        column[mask_percent] = pd.to_numeric(column[mask_percent].str.replace('%', ''), errors='coerce') / 100
        
        # 处理“亿”
        mask_billion = column.str.contains('亿', na=False)
        column[mask_billion] = pd.to_numeric(column[mask_billion].str.replace('亿', ''), errors='coerce') * 1e8
        
        # 处理“--”
        mask_dash = column == '--'
        column[mask_dash] = None
        
        # 尝试将整个列转换为浮点数，错误值保持原样
        column = pd.to_numeric(column, errors='coerce')
    
    return column

# 不需要清理的列名
columns_to_skip = {"名称", "所属行业", "异动类型", "细分行业"}

csv_file_path = input('要清理特殊符号的文件(含后缀csv): ')

# 开始计时
start_time = time.time()

# 分块读取CSV文件，跳过第一行（表头）
chunksize = 10000  # 每次读取的行数
chunks = []

for chunk in pd.read_csv(csv_file_path, chunksize=chunksize, skiprows=1):
    for col in chunk.columns:
        if col not in columns_to_skip:
            chunk[col] = clean_column(chunk[col])
    
    chunks.append(chunk)

# 合并所有块
df_final = pd.concat(chunks, ignore_index=True)

# 获取CSV文件的第一行作为DataFrame的列名
first_row = pd.read_csv(csv_file_path, nrows=1)
df_final.columns = first_row.columns

# 将处理后的DataFrame保存为新的CSV文件
output_csv_path = csv_file_path + '_已清理特殊符号.csv'
df_final.to_csv(output_csv_path, index=False, encoding='utf-8-sig')

print(f"数据已处理并保存到{output_csv_path}")

# 结束计时并打印耗时
end_time = time.time()
elapsed_time = end_time - start_time
print(f"第二步执行完成，耗时: {elapsed_time:.2f} 秒")