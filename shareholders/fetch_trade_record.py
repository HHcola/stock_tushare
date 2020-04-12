# -*- encoding: UTF-8 -*-
from shareholders.fetch_holder_data import buy_holder_stock, sell_holder_stock
from shareholders.holder_data_type import record_to_holder, TradeRecordData
from shareholders.trade_record import TradeRecord


def buy_record_stock(data: TradeRecordData):
    """
    股票买入
    :param data:
    :return:
    """
    trade_record = TradeRecord()
    trade_record.insert_table(data)
    stock_holder = record_to_holder(data)
    buy_holder_stock(stock_holder)


def sell_record_stock(data: TradeRecordData):
    """
    股票卖出
    :param data:
    :return:
    """
    trade_record = TradeRecord()
    trade_record.insert_table(data)
    stock_holder = record_to_holder(data)
    sell_holder_stock(stock_holder)


def __calc_stock_stop_loss(stock_type, stock: TradeRecordData):
    """
    计算当前持股的止损点
    :param stock_type: 1 买入；2. 卖出
    :param stock:
    :return:
    """
    holder_stock = HolderDataStocks()
    stocks_list = holder_stock.search_table(stock.symbol)
    if stocks_list is None or len(stocks_list) == 0:
        return stock
    else:
        stock_holder = stocks_list[0]
        if stock_type == BUY_TYPE:
            stock_holder.price = (stock_holder.size * stock_holder.price + stock.size * stock.price) / (
                stock_holder.size + stock.size)
            stock_holder.size += stock.size
            return stock_holder
        elif stock_type == SELL_TYPE:
            stock_holder.price = (stock_holder.size * stock_holder.price - stock.size * stock.price) / (
                stock_holder.size - stock.size)
            stock_holder.size -= stock.size
            return stock_holder
        else:
            return None
