# -*- coding: UTF-8 -*-
import pandas as pd

from db.config import stock_field_list
from db.data_read import StockBriefRead, StockRead
from util.utils import get_before_date


def get_all_stock(threshold=60):
    """
    获取所有的数据，默认60天
    :param threshold:
    :return:
    """
    date = get_before_date(threshold)
    stock_brief_read = StockBriefRead()
    stocks_brief = stock_brief_read.get_stock_brief(None)

    return stocks_brief


def convert_to_dataframe(stocks_list):
    if stocks_list is None:
        return None
    list_columns = stock_field_list
    size = len(stocks_list)
    data_list = [[0] * 10 for _ in range(size)]
    for index, stock in enumerate(stocks_list):
        data_list[index] = stock.convert_to_list()
    return pd.DataFrame(data_list, columns=list_columns)
