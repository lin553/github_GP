import pandas as pd
import time

# 开始计时
start_time = time.time()

# 将Excel文件转换为CSV文件
excel_file_path = 'AAA_个股_涨幅排名_2025-01月_2025-01-24.xls'
csv_file_path = excel_file_path + '.csv'

# 读取Excel文件（不跳过任何行）
df_excel = pd.read_excel(excel_file_path, sheet_name='提取结果')

# 检测并移除重复的标题行
header_row = df_excel.iloc[0].tolist()
duplicate_header_mask = df_excel.apply(lambda row: row.tolist() == header_row, axis=1)
df_excel = df_excel[~duplicate_header_mask]

# # 确保保留原始的表头
# df_excel.columns = pd.read_excel(excel_file_path, sheet_name='提取结果', nrows=1).columns

# 打印所有列名以确认列名正确
print("所有列名:", df_excel.columns.tolist())

# 保存为CSV文件
df_excel.to_csv(csv_file_path, index=False, encoding='utf-8-sig')

# 结束计时并打印耗时
end_time = time.time()
elapsed_time = end_time - start_time
print(f"第一步执行完成，耗时: {elapsed_time:.2f} 秒")





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
        column[mask_billion] = pd.to_numeric(column[mask_billion].str.replace('亿', ''), errors='coerce') 
        
        # 处理“--”
        mask_dash = column == '--'
        column[mask_dash] = None
        
        # 尝试将整个列转换为浮点数，错误值保持原样
        column = pd.to_numeric(column, errors='coerce')
    
    return column

# 不需要清理的列名
columns_to_skip = {"名称", "所属行业", "异动类型", "细分行业"}

# 获取CSV文件的第一行作为DataFrame的列名
first_row = pd.read_csv(csv_file_path, nrows=1)
columns = first_row.columns.tolist()

# 打印所有列名以确认列名正确
print("所有列名:", columns)

# 确定需要清理的列
columns_to_clean = [col for col in columns if col not in columns_to_skip]

# 打印需要清理的列名
print("需要清理的列名:", columns_to_clean)

# 开始计时
start_time = time.time()

# 分块读取CSV文件，跳过第一行（表头）
chunksize = 10000  # 每次读取的行数
chunks = []

for chunk in pd.read_csv(csv_file_path, chunksize=chunksize, skiprows=1):
    for col in columns_to_clean:  # 只遍历需要清理的列
        if col in chunk.columns:  # 检查列是否存在
            try:
                print(f"正在清理列: {col}")
                chunk[col] = clean_column(chunk[col])
            except KeyError as e:
                print(f"警告: 列 '{col}' 未找到，跳过清理——1.")
        else:
            print(f"警告: 列 '{col}' 未找到，跳过清理——2.")

    chunks.append(chunk)

# 合并所有块
df_final = pd.concat(chunks, ignore_index=True)

# 将处理后的DataFrame保存为新的CSV文件
output_csv_path = csv_file_path + '_已清理特殊符号.csv'
df_final.to_csv(output_csv_path, index=False, encoding='utf-8-sig')

# 结束计时并打印耗时
end_time = time.time()
elapsed_time = end_time - start_time
print(f"第二步执行完成，耗时: {elapsed_time:.2f} 秒")




# 失败，第一步时第一行重复，第二步删除不需删除的数据