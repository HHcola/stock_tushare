# -*- encoding: UTF-8 -*-
from db.config import stock_brief_list


class StockData:
    date = None  # 交易日期
    stock_open = None  # 开盘价
    high = None  # 最高价
    lower = None  # 最低价
    close = None  # 收盘价
    pre_close = None  # 昨收价
    change = None  # 涨跌额
    pct_chg = None  # 涨跌幅 （未复权)
    vol = None  # 成交量 （手）
    amount = None  # 成交额 （千元）

    def set_data(self,
                 date,
                 stock_open,
                 high,
                 lower,
                 close,
                 pre_close,
                 change,
                 pct_chg,
                 vol,
                 amount
                 ):
        self.date = date
        self.stock_open = stock_open
        self.high = high
        self.lower = lower
        self.close = close
        self.pre_close = pre_close
        self.change = change
        self.pct_chg = pct_chg
        self.vol = vol
        self.amount = amount

    def convert_to_list(self):
        stock_list = [None] * 10
        stock_list[0] = self.date
        stock_list[1] = self.stock_open
        stock_list[2] = self.high
        stock_list[3] = self.lower
        stock_list[4] = self.close
        stock_list[5] = self.pre_close
        stock_list[6] = self.change
        stock_list[7] = self.pct_chg
        stock_list[8] = self.vol
        stock_list[9] = self.amount
        return stock_list


class StockBrief:
    ts_code = None  # TS代码
    symbol = None  # 股票代码
    name = None  # 股票名称
    area = None  # 所在地域
    industry = None  # 所属行业
    market = None  # 市场类型 （主板/中小板/创业板/科创板）
    list_status = None  # 上市状态： L上市 D退市 P暂停上市
    list_date = None  # 上市日期

    def set_data(self,
                 ts_code,
                 symbol,
                 name,
                 area,
                 industry,
                 market,
                 list_status,
                 list_date):
        self.ts_code = ts_code
        self.symbol = symbol
        self.name = name
        self.area = area
        self.industry = industry
        self.market = market
        self.list_status = list_status
        self.list_date = list_date

    def convert_to_list(self):
        stock_list = [None] * len(stock_brief_list)
        stock_list[0] = self.ts_code
        stock_list[1] = self.symbol
        stock_list[2] = self.name
        stock_list[3] = self.area
        stock_list[4] = self.industry
        stock_list[5] = self.market
        stock_list[6] = self.list_status
        stock_list[7] = self.list_date
        return stock_list
