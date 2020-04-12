# -*- encoding: UTF-8 -*-
import os
from abc import ABCMeta
from abc import abstractmethod
import sqlite3 as db

from log.log import LOG


class BaseStock(metaclass=ABCMeta):
    """
    抽象基类
    """
    DB_NAME = '../data/stock.db'
    connect = None
    table_field = None
    table_value = None
    field_list = None

    def __init__(self, db_name):
        if db_name is not None:
            self.DB_NAME = db_name
        else:
            basedir = os.path.dirname(os.path.dirname(__file__))
            LOG.log('BaseStock basedir %s ' % basedir)
            self.DB_NAME = basedir + '/data/stock.db'
        self.open_db()

    def __del__(self):
        self.close_db()

    @abstractmethod
    def create_table(self):
        raise NotImplementedError('create_table is not implemented')

    @abstractmethod
    def insert_table(self):
        raise NotImplementedError('create_table is not implemented')

    @abstractmethod
    def row_to_data(self, row):
        raise NotImplementedError('row_to_data is not implemented')

    def open_db(self):
        """
        打开数据库
        :return:
        """
        self.connect = db.connect(self.DB_NAME)

    def close_db(self):
        if self.connect is not None:
            self.connect.close()

    def commit_db(self):
        if self.connect is not None:
            self.connect.commit()

    def get_table_field(self):
        self.table_field = '('
        for index, value in enumerate(self.field_list):
            self.table_field += value
            if index < len(self.field_list) - 1:
                self.table_field += ','
        self.table_field += ')'

    def get_table_value(self):
        self.table_value = " VALUES ("
        for index, value in enumerate(self.field_list):
            self.table_value += "'{"
            self.table_value += value
            self.table_value += "}'"
            if index < len(self.field_list) - 1:
                self.table_value += ','
        self.table_value += ")"

    def convert_db_stock(self, cursor):
        data_list = []
        for row in cursor:
            data_list.append(self.row_to_data(row))
        return data_list


