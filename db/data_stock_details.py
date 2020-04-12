# -*- encoding: UTF-8 -*-
from db.config import stock_field_list
from db.data_base import BaseStock
from db.data_type import StockData
from log.log import LOG


class StockDetails(BaseStock):
    __table_name = None

    def __init__(self):
        super().__init__(None)
        self.field_list = stock_field_list
        self.get_table_field()
        self.get_table_value()

    def create_table(self, table_name):
        sql = '''CREATE TABLE IF NOT EXISTS '{stock_name}'
           (DATE  TEXT  PRIMARY KEY   NOT NULL,
           OPEN          FLOAT,
           HIGH          FLOAT ,
           LOWER         FLOAT ,
           CLOSE         FLOAT ,
           PRE_CLOSE      FLOAT ,
           CHANGE         FLOAT ,
           PCT_CHG        FLOAT ,
           VOL            DOUBLE ,
           AMOUNT         DOUBLE);'''.format(stock_name=table_name)
        self.connect.execute(sql)
        # self.commit_db()

    def insert_table(self, table, data: StockData):
        """
        插入数据
        :param table:
        :param data: StockData
        :return:
        """
        insert_sql = '''INSERT INTO "{stock_name}" '''.format(stock_name=table) + self.table_field \
                     + self.__convert_data_sql(data)
        search_data = self.search_table(table, data.date)
        if search_data is None or len(search_data) == 0:
            LOG.log('insert_table ts_code %s date size %s' % (table, data.date))
            self.connect.execute(insert_sql)
            # self.connect.commit()
        else:
            LOG.log('insert_table ts_code %s date size %s have exist' % (table, data.date))

    def delete_data(self, table, date):
        delete_sql = '''DELETE FROM "{stock_name}" '''.format(
            stock_name=table) + ' WHERE DATE = "{date}"'.format(date=date)
        self.connect.execute(delete_sql)
        self.connect.commit()

    def search_table(self, table_name, stock_date):
        """
        查找数据
        :param table_name:
        :param stock_date:
        :return:
        """
        if stock_date is not None:
            search_sql = '''SELECT * FROM "{table_name}" WHERE DATE={date}'''.format(table_name=table_name,
                                                                                     date=stock_date)
        else:
            search_sql = '''SELECT * FROM "{table_name}" '''.format(table_name=table_name)

        cursor = self.connect.execute(search_sql)
        data_list = self.convert_db_stock(cursor)
        return data_list

    def row_to_data(self, row):
        """
        数据组转换
        :param row:
        :return:
        """
        data = StockData()
        data.date = row[self.field_list.index('DATE')]
        data.stock_open = row[self.field_list.index('OPEN')]
        data.high = row[self.field_list.index('HIGH')]
        data.lower = row[self.field_list.index('LOWER')]
        data.close = row[self.field_list.index('CLOSE')]
        data.pre_close = row[self.field_list.index('PRE_CLOSE')]
        data.change = row[self.field_list.index('CHANGE')]
        data.pct_chg = row[self.field_list.index('PCT_CHG')]
        data.vol = row[self.field_list.index('VOL')]
        data.amount = row[self.field_list.index('AMOUNT')]
        return data

    def __convert_data_sql(self, data: StockData):
        return self.table_value.format(DATE=data.date,
                                       OPEN=data.stock_open,
                                       HIGH=data.high,
                                       LOWER=data.lower,
                                       CLOSE=data.close,
                                       PRE_CLOSE=data.pct_chg,
                                       CHANGE=data.change,
                                       PCT_CHG=data.pct_chg,
                                       VOL=data.vol,
                                       AMOUNT=data.amount
                                       )
