# -*- coding: UTF-8 -*-
import logging

from db.data_read import StockRead
from shareholders.holder_data_type import BUY_TYPE
from shareholders.trade_record_read import TradeRecordRead
from strategy.strategy_base import Strategy


class TurtleStrategy(Strategy):
    def enter(self, data_frame):

        """
        入市
        策略1:20日为基础的偏短线系统
        策略2:50日为基础的偏短线系统
        :param data_frame:
        :return:
        """
        threshold = 20
        max_price = 0
        data = data_frame.iloc[:threshold:-1]  # choose data by date
        if len(data) < threshold:
            return False
        for index, row in data.iterrows():  # find the max price
            if row['CLOSE'] > max_price:
                max_price = float(row['HIGH'])
                # max_price = float(row['CLOSE'])

        last_close = data.iloc[0]['CLOSE']  # get last data
        if last_close >= max_price:
            return True
        return False

    def position(self, ts_code):
        """
        头寸规模
        :param ts_code:
        :return:
        """
        pass

    def stop_loss(self, ts_code):
        """
        止损：%2为最大止损，账户总额的2%，就是价格波动的2N
        :param ts_code:
        :return:
        """
        # 计算ts_code 账户总额
        trade_read = TradeRecordRead()
        data = trade_read.get_stock_dataframe(ts_code)
        total_cost = None
        total_size = None
        for index, row in data.iterrows():  # find the max price
            if row['TYPE'] == BUY_TYPE:
                total_size += row['SIZE']
                total_cost += float(row['SIZE']) * float(row['PRICE'])

        # 现在的市值
        stock_read = StockRead()
        stock_data = stock_read.get_stock_dataframe(ts_code)
        close_price = stock_data[0]['CLOSE']
        cost = total_size * close_price

        # 计算损失
        if cost > total_cost:
            return False
        else:
            gap = total_cost - cost
            change = gap * 100 / total_cost
            if change > 2:
                return True
            else:
                return False






    def leave(self, ts_code):
        """
            离市:
            策略1：多头头寸为10日最低值
            策略2：多头头寸为20日最低值
            :param ts_code:
            :return:
            """
        threshold = 10
        stock_read = StockRead()
        data = stock_read.get_stock_dataframe(ts_code)
        min_price = 9999
        data = data.loc[threshold]
        if len(data) < threshold:
            logging.debug("样本小于{1}天...\n".format(threshold))
            return False
        for index, row in data.iterrows():
            if row['close'] < min_price:
                min_price = float(row['CLOSE'])

        last_close = data.iloc[-1]['CLOSE']
        if last_close <= min_price:
            return True
        return False



