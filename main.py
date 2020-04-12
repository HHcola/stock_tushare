# -*- encoding: UTF-8 -*-

from stock_tushare.fetch_stock_data import FetchStock

fetchStock = FetchStock()
fetchStock.update_stock()
#
# stock_brief_read = StockBriefRead()
# stock_read = StockRead()
# data_list = stock_brief_read.get_stock_brief(None)
# for stock in data_list:
#     stock = stock_read.get_stock(stock.ts_code, None)


