# 在使用 pandas 的 ExcelWriter 写入 Excel 文件时，你可以通过指定不同的引擎来控制文件的生成方式。常见的引擎包括 "openpyxl"、
        # "xlsxwriter" 等。当你选择 "xlsxwriter" 作为引擎时，可以通过 engine_kwargs 参数向该引擎传递额外的配置选项。

# engine_kwargs={"options": {"nan_inf_to_errors": True}} 解释
    # engine_kwargs: 这是一个字典参数，用于向所选引擎传递关键字参数。不同的引擎支持的参数不同。
    # "options": 当你使用 "xlsxwriter" 引擎时，可以通过 "options" 键传递一个字典给 XlsxWriter 库，以设置一些全局选项或行为。
    # "nan_inf_to_errors": True: 这是传递给 XlsxWriter 的一个特定选项。它指示 XlsxWriter 在遇到 NaN（Not a Number）、
                                # 无穷大（Infinity）等特殊浮点值时，将它们视为错误，并在 Excel 中显示为错误值（例如 #NUM!），
                                # 而不是默认的行为（通常会将这些值转换为 Excel 中的 #DIV/0! 或者简单的空白单元格）。
# =================================================================
import numpy as np
import pandas as pd 
from xlsxwriter import Workbook


# 创建一个包含NaN和无穷大值的DataFrame
df = pd.DataFrame([
    [123, np.nan, 567],
    [456, 789, np.inf],
    [-np.inf, 100, 200]
], columns=["Foo", "Bar", 'abc'])


with pd.ExcelWriter(
    './pandas库/005.12.xlsx',       # "path_to_file.xlsx" 是要写入的目标文件路径
    engine="xlsxwriter",            # engine="xlsxwriter" 指定了使用 "xlsxwriter" 作为处理 Excel 文件的引擎。
    engine_kwargs={"options": {"nan_inf_to_errors": True}}  # 向底层引擎传递额外的参数:  向 "xlsxwriter" 引擎传递了一个选项，
                                                                                    # 使得所有在 DataFrame 中出现的 NaN 或者
                                                                                    # 无穷大值，在写入 Excel 文件时被视为错误，
                                                                                    # 并以 Excel 错误的形式展示（如 #NUM!）。
) as writer:
    df.to_excel(writer, index=False)




# 本程序无效：失败