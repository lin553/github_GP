

print("\n\n--------------- 7.通过 numba 加速计算 ---------------")
# numba 是一个 JIT 编译器，可以将 Python 代码加速。通过将数据处理的代码加速，可以显著提高性能。特别是对于循环、
    # 数值计算等计算密集型操作，numba 可以极大地提高速度。

import numba
import pandas as pd


# @jit 装饰器： 这是来自 Numba 库的一个装饰器，用来标记一个函数以便通过 Numba 的即时（Just-In-Time, JIT）
             # 编译技术进行优化。JIT 编译可以在运行时将 Python 函数编译成本地机器码，从而显著提高执行速度，特别是对于包含
             # 大量数值运算的循环或函数。
@numba.jit      
def calculate_square(x):
    return x ** 2

# 使用 numba 加速计算
df = pd.DataFrame({'A': [1, 2, 3, 4]})
df['B'] = df['A'].apply(calculate_square)
print(df)


