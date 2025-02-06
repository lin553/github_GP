# 失败： 注册后送100积分，实际上积分不够，无论下什么都不够：权限的具体详情访问：https://tushare.pro/document/1?doc_id=108

from datetime import datetime, date
import pandas as pd
import tushare as ts    # 导入tushare

# 初始化pro接口
pro = ts.pro_api('322f1ec7f4ada251a792288afebac64ca7f31d0caeb51af0c93fcfb2')

# 拉取数据
df = pro.stock_basic(**{
    "ts_code": "",
    "name": "",
    "exchange": "",
    "market": "",
    "is_hs": "",
    "list_status": "",
    "limit": "",
    "offset": ""
}, fields=[
    "ts_code",
    "symbol",
    "name",
    "area",
    "industry",
    "cnspell",
    "market",
    "list_date",
    "act_name",
    "act_ent_type",
    "fullname",
    "enname",
    "exchange",
    "curr_type",
    "list_status",
    "delist_date",
    "is_hs"
])

print(df)
data = pd.DataFrame(df)
data.to_csv("./pandas库/股票数据下载/", datetime.now(), ".csv")

