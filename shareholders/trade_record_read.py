# -*- encoding: UTF-8 -*-
import pandas as pd

from shareholders.holder_data_type import trade_record_field_list
from shareholders.trade_record import TradeRecord


class TradeRecordRead:

    def get_stock(self, ts_code):
        """
           获取持股股票详细信息
           如果date = None，则获取全部数据
           :param ts_code:
           :return:
           """
        trade_record = TradeRecord()
        return trade_record.search_table(ts_code)

    def get_stock_dataframe(self, ts_code):
        """
           获取持股股票详细信息
           如果date = None，则获取全部数据
           :param ts_code:
           :return:
           """
        trade_record = TradeRecord()
        trade_stock_list = trade_record.search_table(ts_code)
        return self.__convert_to_dataframe(trade_stock_list)

    def __convert_to_dataframe(self, stocks_list):
        if stocks_list is None:
            return None
        columns = trade_record_field_list
        return pd.DataFrame(stocks_list, columns)
