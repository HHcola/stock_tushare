# -*- encoding: UTF-8 -*-
import logging

import pandas as pd

from db.config import stock_field_list
from db.data_stock_details import StockDetails
from db.data_stocks_brief import DataStocksBrief


class StockRead:
    __stock_detail = StockDetails()

    def get_stock(self, code, date):
        """
        获取股票详细信息
        如果date = None，则获取全部数据
        :param code:
        :param date:
        :return:
        """
        if code is None:
            logging.warning('get_stock code id None')
            return
        return self.__stock_detail.search_table(code, date)

    def get_stock_dataframe(self, code, date):
        """
        获取股票详细信息
        如果date = None，则获取全部数据
        :param code:
        :param date:
        :return:
        """
        if code is None:
            logging.warning('get_stock code id None')
            return
        stock_list = self.__stock_detail.search_table(code, date)
        return self.__convert_to_dataframe(stock_list)

    def __convert_to_dataframe(self, stocks_list):
        if stocks_list is None:
            return None
        columns = stock_field_list
        return pd.DataFrame(stocks_list, columns)


class StockBriefRead:
    __stock_brief = DataStocksBrief()

    def get_stock_brief(self, code):
        """
        获取股票基础信息
        如果code == None，则获取全部
        :param code:
        :return:
        """
        return self.__stock_brief.search_table(code)
