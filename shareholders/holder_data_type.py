# -*- encoding: UTF-8 -*-

BUY_TYPE = 1
SELL_TYPE = 2

holder_stock_field_list = ['TS_CODE',  # 股票
                           'SYMBOL',  # 股票代码
                           'NAME',  # 股票名称
                           'SIZE',  # 持股数量
                           'PRICE',  # 价格
                           'CHANGE',  # 跌涨幅
                           'PCT_CHANGE',  # 跌涨幅
                           'STOP_LOSS',  # 止损价
                           'LEAVE_PRICE',  # 离市价
                           ]

trade_record_field_list = ['TS_CODE',  # 股票
                           'SYMBOL',  # 股票代码
                           'NAME',  # 股票名称
                           'SIZE',  # 持股数量
                           'PRICE',  # 价格
                           'TYPE',  # 类型：买入：1，卖出：2
                           'CHANGE',  # 跌涨幅
                           'PCT_CHANGE',  # 跌涨幅
                           'STOP_LOSS',  # 止损价
                           'LEAVE_PRICE',  # 离市价
                           'DATE'  # 交易日期
                           ]


class StockHolder:
    """
    持股情况
    """
    ts_code = None
    symbol = None
    name = None
    size = None
    price = None
    change = None
    pct_chg = None  # 涨跌幅
    stop_loss = None  # 整体止损点
    leave_price = None  # 整体离市价

    def set_data(self,
                 ts_code,
                 symbol,
                 name,
                 size,
                 price,
                 change,
                 pct_chg,
                 stop_loss,
                 leave_price):
        self.ts_code = ts_code
        self.symbol = symbol
        self.name = name
        self.size = size
        self.price = price
        self.change = change
        self.pct_chg = pct_chg
        self.stop_loss = stop_loss
        self.leave_price = leave_price


class TradeRecordData:
    """
    交易记录(流水)
    """
    ts_code = None
    symbol = None
    name = None
    size = None  # 买入数量
    price = None  # 买入价
    type = None  # 类型：买入：1， 卖出：2
    change = None  # 涨跌额
    pct_chg = None  # 涨跌幅
    stop_loss = None  # 止损价
    leave_price = None  # 离市价
    date = None

    def set_data(self,
                 ts_code,
                 symbol,
                 name,
                 size,
                 price,
                 trade_type,
                 change,
                 pct_chg,
                 stop_loss,
                 leave_price,
                 date):
        self.ts_code = ts_code
        self.symbol = symbol
        self.name = name
        self.size = size
        self.price = price
        self.type = trade_type
        self.change = change
        self.pct_chg = pct_chg
        self.stop_loss = stop_loss
        self.leave_price = leave_price
        self.date = date


def record_to_holder(data: TradeRecordData):
    if data is None:
        return
    holder_data = StockHolder()
    holder_data.ts_code = data.ts_code
    holder_data.symbol = data.symbol
    holder_data.name = data.name
    holder_data.price = data.price
    return holder_data
