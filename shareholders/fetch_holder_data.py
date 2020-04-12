# -*- encoding: UTF-8 -*-
import pandas as pd

from shareholders.holder_data import HolderDataStocks
from shareholders.holder_data_type import holder_stock_field_list, StockHolder, SELL_TYPE, BUY_TYPE


def read_holder_stock():
    """
    获取当前持股
    :return:
    """
    holder_stock = HolderDataStocks()
    stocks_list = holder_stock.search_table(None)
    return __convert_to_dataframe(stocks_list)


def buy_holder_stock(stock: StockHolder):
    """
    买入股票
    :param stock:
    :return:
    """
    stock = __calc_stock_price(BUY_TYPE, stock)
    holder_stock = HolderDataStocks()
    holder_stock.insert_table(stock)


def sell_holder_stock(stock: StockHolder):
    """
    卖出股票
    :param stock:
    :return:
    """
    stock = __calc_stock_price(SELL_TYPE, stock)
    holder_stock = HolderDataStocks()
    holder_stock.insert_table(stock)


def __convert_to_dataframe(stocks_list):
    if stocks_list is None:
        return None
    columns = holder_stock_field_list
    return pd.DataFrame(stocks_list, columns)


def __calc_stock_price(stock_type, stock: StockHolder):
    """
    计算当前持股
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


