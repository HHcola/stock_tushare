# -*- encoding: UTF-8 -*-
from db.config import stock_brief_list
from db.data_base import BaseStock
from db.data_type import StockBrief
from log.log import LOG


class DataStocksBrief(BaseStock):
    __table_name = 'stock_brief'

    def __init__(self):
        super().__init__(None)
        self.field_list = stock_brief_list
        self.get_table_field()
        self.get_table_value()
        self.create_table()

    def create_table(self):
        sql = '''CREATE TABLE IF NOT EXISTS {stock_name}
            (TS_CODE  TEXT  PRIMARY KEY   NOT NULL,
            SYMBOL   TEXT,
            NAME        TEXT,
            AREA           TEXT ,
            INDUSTRY           TEXT ,
            MARKET           TEXT ,
            LIST_DATE         TEXT ,
            LIST_STATUS     TEXT);'''.format(stock_name=self.__table_name)
        self.connect.execute(sql)
        self.commit_db()

    def insert_table(self, data: StockBrief):
        """
        插入数据
        :param data:
        :return:
        """
        insert_sql = '''INSERT INTO {stock_name} '''.format(stock_name=self.__table_name) + self.table_field \
                     + self.__convert_data_sql(data)

        search_data = self.search_table(data.ts_code)
        if search_data is None or len(search_data) == 0:
            LOG.log('insert_table ts_code = %s' % data.ts_code)
            self.connect.execute(insert_sql)
            # self.connect.commit()
        else:
            LOG.log('insert_table ts_code = %s have exist' % data.ts_code)

    def delete_data(self, code):
        delete_sql = '''DELETE FROM {stock_name} '''.format(
            stock_name=self.__table_name) + ' WHERE TS_CODE = "{ts_code}"'.format(ts_code=code)
        self.connect.execute(delete_sql)
        self.connect.commit()

    def update_table(self, code):
        update_sql = '''UPDATE {stock_name} '''.format(
            stock_name=self.__table_name) + "WHERE TS_CODE = {ts_code}".format(ts_code=code)
        self.connect.execute(update_sql)
        self.connect.commit()

    def search_table(self, code):
        """
        查找数据
        :param code:
        :return:
        """
        if code is None:
            search_sql = '''SELECT * FROM {table_name}'''.format(table_name=self.__table_name)
        else:
            search_sql = '''SELECT * FROM {table_name} WHERE TS_CODE="{code}"''' \
                .format(table_name=self.__table_name, code=code)
        cursor = self.connect.execute(search_sql)
        data_list = self.convert_db_stock(cursor)
        return data_list

    def __convert_data_sql(self, data: StockBrief):
        return self.table_value.format(TS_CODE=data.ts_code,
                                       SYMBOL=data.symbol,
                                       NAME=data.name,
                                       AREA=data.area,
                                       INDUSTRY=data.industry,
                                       MARKET=data.market,
                                       LIST_DATE=data.list_date,
                                       LIST_STATUS=data.list_status
                                       )

    def row_to_data(self, row):
        """
        数据组转换
        :param row:
        :return:
        """
        data = StockBrief()
        data.ts_code = row[self.field_list.index('TS_CODE')]
        data.symbol = row[self.field_list.index('SYMBOL')]
        data.name = row[self.field_list.index('NAME')]
        data.area = row[self.field_list.index('AREA')]
        data.industry = row[self.field_list.index('INDUSTRY')]
        data.market = row[self.field_list.index('MARKET')]
        data.list_date = row[self.field_list.index('LIST_DATE')]
        data.list_status = row[self.field_list.index('LIST_STATUS')]
        return data
