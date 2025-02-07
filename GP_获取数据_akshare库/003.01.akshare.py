# 摘自：https://zhuanlan.zhihu.com/p/678521592
# 2025-2-7


from datetime import datetime, time




print("\n\n------------------ 1.获取个股日线行情数据 ------------------")
import akshare as ak

stock_data = ak.stock_zh_a_daily(symbol="sz000001", start_date="2025-01-01", end_date=datetime.now())
print(stock_data)





print("\n\n------------------ 2.获取基金数据: 报错：AttributeError: module 'akshare' has no attribute 'fund_em_open_fund_info' ------------------")
# # # import akshare as ak
# # # # 获取基金净值数据
# # # fund_data = ak.fund_em_open_fund_info(fund="000001", start_date="2025-01-01", end_date=datetime.now())
# # # print(fund_data)
# # # # AttributeError: module 'akshare' has no attribute 'fund_em_open_fund_info'



print("\n\n------------------ 3.获取期货日线行情数据：报错：AttributeError: module 'akshare' has no attribute 'futures_zh_daily' ------------------")
# # # import akshare as ak

# # # futures_data = ak.futures_zh_daily(symbol="cu2103", start_date="2025-01-01", end_date=datetime.now())
# # # print(futures_data)





print("\n\n------------------ 4.获取外汇汇率数据：报错：AttributeError: module 'akshare' has no attribute 'forex_ak_m1' ------------------")
# # # import akshare as ak

# # # exchange_rate_data = ak.forex_ak_m1()
# # # print(exchange_rate_data)






print("\n\n------------------ 5.数据可视化: 示例：绘制股票价格走势图 ------------------")
import akshare as ak
import matplotlib.pyplot as plt

# 获取股票日线行情数据
sym_1 = 'sz000001'
stock_data = ak.stock_zh_a_daily(symbol=sym_1, start_date="2025-01-01", end_date=datetime.now())

# 绘制股票价格走势图
plt.plot(stock_data["date"], stock_data["close"])
plt.xlabel("Date")
plt.ylabel("Close Price")
plt.title("Stock Price Trend: " + sym_1)
plt.show()




print("\n\n------------------ 6.数据分析: 计算股票收益率 ------------------")
import akshare as ak

# 获取股票日线行情数据
stock_data = ak.stock_zh_a_daily(symbol="sz000001", start_date="2025-01-01", end_date=datetime.now())

# 计算股票收益率
stock_data["return"] = stock_data["close"].pct_change()
print(stock_data["return"].describe())






# # =================================================================
# # 实际应用场景
#     # 当在博客文章中讨论Akshare的实际应用场景时，可以为每个场景提供详细的示例代码。以下是一些实际应用场景以及相应的示例代码：

print("\n\n------------------ 7.量化交易策略开发: 使用Akshare获取股票数据并开发简单的均线策略 ------------------")
import akshare as ak
import pandas as pd

# 获取股票日线行情数据
stock_data = ak.stock_zh_a_daily(symbol="sz000001", start_date="2025-01-01", end_date=datetime.now())

# 计算5日和20日均线
stock_data["ma5"] = stock_data["close"].rolling(window=5).mean()
stock_data["ma20"] = stock_data["close"].rolling(window=20).mean()

# 生成买入信号（ma5向上穿越ma20）
stock_data["buy_signal"] = (stock_data["ma5"] > stock_data["ma20"]) & (stock_data["ma5"].shift(1) <= stock_data["ma20"].shift(1))

# 生成卖出信号（ma5向下穿越ma20）
stock_data["sell_signal"] = (stock_data["ma5"] < stock_data["ma20"]) & (stock_data["ma5"].shift(1) >= stock_data["ma20"].shift(1))

# 打印交易信号
signals = stock_data[["date", "buy_signal", "sell_signal"]]
print(signals)






print("\n\n------------------ 8.金融市场研究: 使用Akshare获取不同市场的历史数据并进行比较分析: 报错：TypeError: stock_zh_index_daily() got an unexpected keyword argument 'index' ------------------")
# import akshare as ak
# import matplotlib.pyplot as plt

# # 获取A股指数数据
# a_share_data = ak.stock_zh_index_daily(index="000001", start_date="2025-01-01", end_date=datetime.now())
# # 获取美股指数数据
# us_stock_data = ak.stock_us_daily(symbol="DJI", start_date="2025-01-01", end_date=datetime.now())

# # 绘制A股和美股指数比较图
# plt.figure(figsize=(12, 6))
# plt.plot(a_share_data["date"], a_share_data["close"], label="A股指数")
# plt.plot(us_stock_data["date"], us_stock_data["close"], label="美股指数")
# plt.xlabel("Date")
# plt.ylabel("Close Price")
# plt.title("A股和美股指数比较")
# plt.legend()
# plt.show()





print("\n\n------------------ 9.投资组合管理: 使用Akshare跟踪不同资产的表现并生成投资组合报告:报错：ttributeError: module 'akshare' has no attribute 'fund_em_open_fund_info' ------------------")
# import akshare as ak

# # 获取股票、基金和期货数据
# stock_data = ak.stock_zh_a_daily(symbol="sz000001", start_date="2022-01-01", end_date="2022-12-31")
# fund_data = ak.fund_em_open_fund_info(fund="000001", start_date="2022-01-01", end_date="2022-12-31")
# futures_data = ak.futures_zh_daily(symbol="cu2103", start_date="2022-01-01", end_date="2022-12-31")

# # 计算不同资产的年度收益率
# stock_return = (stock_data["close"].iloc[-1] - stock_data["close"].iloc[0]) / stock_data["close"].iloc[0]
# fund_return = (fund_data["unit_nav"].iloc[-1] - fund_data["unit_nav"].iloc[0]) / fund_data["unit_nav"].iloc[0]
# futures_return = (futures_data["close"].iloc[-1] - futures_data["close"].iloc[0]) / futures_data["close"].iloc[0]

# # 打印投资组合报告
# print("股票收益率：", stock_return)
# print("基金收益率：", fund_return)
# print("期货收益率：", futures_return)





print("\n\n------------------ 10.金融数据报告: 使用Akshare生成股票收益率报告和可视化图表 ------------------")
import akshare as ak
import pandas as pd
import matplotlib.pyplot as plt

# 获取股票日线行情数据
stock_data = ak.stock_zh_a_daily(symbol="sz000001", start_date="2022-01-01", end_date="2022-12-31")

# 计算股票收益率
stock_data["return"] = stock_data["close"].pct_change()

# 生成收益率报告
return_report = stock_data["return"].describe()

# 绘制收益率分布图
plt.figure(figsize=(10, 6))
plt.hist(stock_data["return"].dropna(), bins=30, alpha=0.7)
plt.xlabel("Return")
plt.ylabel("Frequency")
plt.title("Stock Return Distribution")
plt.show()

# 打印收益率报告
print(return_report)





print("\n\n------------------ 11.数据挖掘和预测: 使用Akshare获取历史数据并进行股票价格预测 ------------------")
import akshare as ak
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# 获取股票日线行情数据
stock_data = ak.stock_zh_a_daily(symbol="sz000001", start_date="2020-01-01", end_date="2021-12-31")

# 选择用于预测的特征（以日期为基础进行编码）
stock_data["date"] = pd.to_datetime(stock_data["date"])
stock_data["day_of_year"] = stock_data["date"].dt.dayofyear
X = stock_data[["day_of_year"]].values
y = stock_data["close"].values

# 训练线性回归模型
model = LinearRegression()
model.fit(X, y)

# 预测未来30天的股价
future_dates = pd.date_range(start="2023-01-01", periods=30, inclusive="right")
future_day_of_year = future_dates.dayofyear.values.reshape(-1, 1)
future_predictions = model.predict(future_day_of_year)

# 绘制股价预测图
plt.figure(figsize=(12, 6))
plt.plot(stock_data["date"], stock_data["close"], label="历史股价")
plt.plot(future_dates, future_predictions, label="预测股价", linestyle = "--")
plt.xlabel("Date")
plt.ylabel("Close Price")
plt.title("Stock Price Prediction")
plt.legend()
plt.show()



# =================================================================
# 完