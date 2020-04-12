# -*- encoding: UTF-8 -*-
from db.data_stock_details import StockDetails
from db.data_stocks_brief import DataStocksBrief


class StockStorage:
    __stock_detail = StockDetails()

    def stock_storage(self, table, stock_list):
        """
        存储数据
        :param table:
        :param stock_list:
        :return:
        """
        for data in stock_list:
            self.__stock_detail.insert_table(table, data)
        self.__stock_detail.commit_db()


class StockBriefStorage:
    __stock_brief = DataStocksBrief()
    __stock_detail = StockDetails()

    def stock_brief_storage(self, stock_brief_list):
        """
        保存数据，并且创建表
        :param stock_brief_list:
        :return:
        """
        for brief in stock_brief_list:
            self.__stock_brief.insert_table(brief)
            self.__stock_brief.commit_db()
            self.__stock_detail.create_table(brief.ts_code)
            self.__stock_detail.commit_db()



