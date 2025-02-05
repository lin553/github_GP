# 缺失值处理
    # Pandas 提供了多种方法来处理缺失值（如 NaN）。常见的操作包括填充缺失值、删除缺失值等。

    # 方法	    说明
    # isna()	检查缺失值，返回布尔值
    # fillna()	填充缺失值
    # dropna()	删除包含缺失值的行或列

import pandas as pd
import numpy as np

# 示例数据
df = pd.DataFrame({
    'A': [1, 2, np.nan, 4],
    'B': [5, np.nan, 7, 8]
})
print("源数据：\n", df,"\n")
# 填充缺失值
df_filled = df.fillna(0)        # 将 “NaN” 转换为：0
print("执行完成后新数据：")
print(df_filled)




# ========================== 完 ===========================