# 摘自：https://www.runoob.com/pandas/pandas-stock.html
# 2025-2-6



# Pandas 股票数据分析
    # 在股票数据分析中，pandas 是一个非常强大的工具，可以帮助我们处理和分析股票市场的数据。
    # 在本章节我们使用 yfinance（雅虎财经库）下载历史股票数据，并进行各种分析，包括数据清洗、可视化、技术指标计算等。
    # yfinance 是一个 Python 库，可以轻松地从雅虎财经（Yahoo Finance）获取股票、基金、加密货币等资产的历史和实时数据。
    # 通过 pandas，我们可以将这些数据存储为 DataFrame 并进行后续的分析。

        # 数据清洗：处理缺失值、删除不必要的列等。
        # 数据可视化：绘制股票的时间序列图、移动平均线、RSI 等。
        # 技术指标计算：如移动平均线（SMA）、相对强弱指数（RSI）等。
        # 日收益率与累计收益率分析：帮助评估股票的短期和长期表现。
        # 波动率分析：衡量股票的价格波动性。
# ===============================================================
# 这个无法使用，因为雅虎已经关闭中国区服务了

# import yfinance as yf

# # 获取茅台（600519.SS）的股票数据，日期范围从 2020-01-01 到 2021-01-01
# stock_data = yf.download('600519.SS', start='2020-01-01', end='2021-01-01')

# # 查看数据的前几行
# print(stock_data.head())
# =================================================================




# # ----------------------------------------------------------------
# # 以下代码执行半天无回复，应该也不能用了，因为不是官方源。
# from yahoofinancials import YahooFinancials

# # 初始化对象
# yf = YahooFinancials('AAPL')

# # 获取历史收盘价
# try:
#     historical_data = yf.get_historical_price_data(start_date = '2025-2-4', end_date ='2025-2-5',time_interval = 'daily' )
#     if not historical_data['AAPL']['prices']:
#         print("No data found for the given date range.")
#     else:
#         print(historical_data)
# except Exception as e:
#     print(f"An error occurred: {e}")
# # ----------------------------------------------------------------