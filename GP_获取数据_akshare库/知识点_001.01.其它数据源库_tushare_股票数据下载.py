失败： 因为要先到它公司（tushare）官网注册，要积分。据说积分不是免费的。
失败
失败
失败


# 1.导入各种库（pandas、tushare、matplotlib库等）
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
import tushare as ts
import os
import tushare as ts
ts.set_token('密匙')    # 这个要到它公司官网注册买
pro = ts.pro_api()




#  2.设置导入数据格式、日期等，股票数据为前复权
def get_data(code,start,end):
    df=pro.daily(ts_code=code,autype='qfq',start_date=start,end_date=end)
    print(df)
    df.index = pd.to_datetime(df.trade_date)
    #设置把日期作为索引
    #df['ma'] = 0.0  # Backtrader需要用到
    #df['openinterest'] = 0.0  # Backtrader需要用到
    #定义两个新的列ma和openinterest
    df = df[['open', 'high', 'low', 'close', 'vol']]
    #重新设置df取值，并返回df
    return df


#  3.下载股票数据，且用csv保存，保存至指定位置
def acquire_code():   #只下载一只股票数据，且只用CSV保存   未来可以有自己的数据库
    inp_code =input("请输入股票代码:\n")
    inp_start = input("请输入开始时间:'\n'")
    inp_end = input("请输入结束时间:'\n'")
    df = get_data(inp_code,inp_start,inp_end)
    print(df.info())
    #输出统计各列的数据量
    print("—"*30)
    #分割线
    print(df.describe())
    #输出常用统计参数
    df.sort_index(inplace=True)
    #把股票数据按照时间正序排列
    path = os.path.join(os.path.join(os.getcwd(),
        "./GP_获取数据/股票数据下载/"), inp_code + ".csv")
    #os.path地址拼接，''数据地址''为文件保存路径
    # path = os.path.join(os.path.join(os.getcwd(),"数据地址"),inp_code+"_30M.csv")
    df.to_csv(path)




# 4.运行函数，爬取股票数据
acquire_code()



