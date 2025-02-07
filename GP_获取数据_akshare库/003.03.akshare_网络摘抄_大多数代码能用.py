# 摘自：https://www.bookstack.cn/read/akshare/43c9e1e9f815ea0e.md


import akshare as ak
import pandas as pa


# # get_roll_yield_bar_df = ak.get_roll_yield_bar(type_method="date", var="RB", start_day="20250101", end_day="20250206", plot=True)
# get_roll_yield_bar_df = ak.get_roll_yield_bar(type_method="date", var="RB", start_day="20250101", end_day="20250206")

# print(get_roll_yield_bar_df)





# import akshare as ak
# stock_sse_summary_df = ak.stock_sse_summary()
# print(stock_sse_summary_df)





# import akshare as ak
# stock_szse_summary_df = ak.stock_szse_summary(date="20200619")
# print(stock_szse_summary_df)





# import akshare as ak
# stock_zh_a_spot_df = ak.stock_zh_a_spot()
# print(stock_zh_a_spot_df)





# import akshare as ak
# stock_zh_a_daily_hfq_df = ak.stock_zh_a_daily(symbol="sz000002", start_date='20240101', end_date='20250101', adjust="hfq")
# print(stock_zh_a_daily_hfq_df)




# import akshare as ak
# hf_sp_500_df = ak.hf_sp_500(year="2017")
# print(hf_sp_500_df)





# import akshare as ak
# amac_member_info_df = ak.amac_member_info()
# print(amac_member_info_df)








# import akshare as ak
# nlp_ownthink_df = ak.nlp_ownthink(word="人工智能", indicator="entity")
# print(nlp_ownthink_df)




# # 失败：现在网易已经不发布新冠的数据了，akshare也没有这个参数了
# import akshare as ak
# covid_19_163_df = ak.covid_19_163(indicator="数据说明")
# print(covid_19_163_df)





# import akshare as ak
# macro_bank_usa_interest_rate_se = ak.macro_bank_usa_interest_rate()





# import akshare as ak
# fx_df = ak.fx_spot_quote()
# print(fx_df)




# # 报错：1196643 异常，请通过 https://www.nfra.gov.cn/cn/view/pages/ItemDetail.html?docId=1196643 查看
# import akshare as ak
# bank_fjcf_table_detail_df = ak.bank_fjcf_table_detail(page=1)
# print(bank_fjcf_table_detail_df)





# # 加密货币数据
# import akshare as ak
# crypto_js_spot_df = ak.crypto_js_spot()
# print(crypto_js_spot_df)





# # 宏观数据
# import akshare as ak
# macro_cnbs_df = ak.macro_cnbs()
# print(macro_cnbs_df)





# # 能源数据: 碳排放
# import akshare as ak
# energy_carbon_bj_df = ak.energy_carbon_bj()
# print(energy_carbon_bj_df)