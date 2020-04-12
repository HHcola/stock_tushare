# -*- encoding: UTF-8 -*-
from db.data_base import BaseStock
from log.log import LOG
from shareholders.holder_data_type import StockHolder, holder_stock_field_list


class HolderDataStocks(BaseStock):
    __table_name = 'stock_holder'
    DB_NAME = 'data/stock_holder.db'

    def __init__(self):
        super().__init__(self.DB_NAME)
        self.field_list = holder_stock_field_list
        self.get_table_field()
        self.get_table_value()
        self.create_table()

    def create_table(self):
        sql = '''CREATE TABLE IF NOT EXISTS {stock_name}
            (TS_CODE          PRIMARY KEY TEXT,
            SYMBOL         TEXT,
            NAME           TEXT,
            SIZE           FLOAT  ,
            PRICE             FLOAT ,
            CHANGE            FLOAT,
            PCT_CHANGE            FLOAT,
            STOP_LOSS            FLOAT,
             LEAVE_PRICE      FLOAT );'''.format(stock_name=self.__table_name)
        self.connect.execute(sql)
        self.commit_db()

    def insert_table(self, data):
        """
        插入数据
        :param data:
        :return:
        """
        insert_sql = '''INSERT INTO {stock_name} '''.format(stock_name=self.__table_name) + self.table_field \
                     + self.__convert_data_sql(data)

        search_data = self.search_table(data.symbol)
        if search_data is None or len(search_data) == 0:
            LOG.log('insert_table ts_code = %s' % data.symbol)
            self.connect.execute(insert_sql)
            self.connect.commit()
        else:
            # update
            LOG.log('insert_table ts_code = %s have exist' % data.ts_code)
            self.update_table(data)

    def update_table(self, data):
        update_sql = '''UPDATE  {stock_name} SET \
                        SIZE = {SIZE}, \
                        PRICE = {PRICE}, \
                        CHANGE = {CHANGE}, \
                        PCT_CHANGE = {PCT_CHANGE}, \
                        STOP_LOSS = {STOP_LOSS}, \
                        LEAVE_PRICE = {LEAVE_PRICE}  \
                        WHERE SYMBOL = {SYMBOL}}} }''' \
            .format(stock_name=self.__table_name,
                    SIZE=data.size,
                    PRICE=data.price,
                    CHANGE=data.change,
                    PCT_CHANGE=data.pct_chg,
                    STOP_LOSS=data.stop_loss,
                    LEAVE_PRICE=data.leave_price,
                    SYMBOL=data.symbol)
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

    def row_to_data(self, row):
        """
        数据组转换
        :param row:
        :return:
        """
        data = StockHolder()
        data.ts_code = row[self.field_list.index('TS_CODE')]
        data.symbol = row[self.field_list.index('SYMBOL')]
        data.name = row[self.field_list.index('NAME')]
        data.size = row[self.field_list.index('SIZE')]
        data.price = row[self.field_list.index('PRICE')]
        data.change = row[self.field_list.index('CHANGE')]
        data.pct_chg = row[self.field_list.index('PCT_CHANGE')]
        data.stop_loss = row[self.field_list.index('STOP_LOSS')]
        data.leave_price = row[self.field_list.index('LEAVE_PRICE')]
        return data

    def __convert_data_sql(self, data: StockHolder):
        return self.table_value.format(TS_CODE=data.ts_code,
                                       SYMBOL=data.symbol,
                                       NAME=data.name,
                                       SIZE=data.size,
                                       PRICE=data.price,
                                       CHANGE=data.change,
                                       PCT_CHANGE=data.pct_chg,
                                       STOP_LOSS=data.stop_loss,
                                       LEAVE_PRICE=data.leave_price
                                       )
