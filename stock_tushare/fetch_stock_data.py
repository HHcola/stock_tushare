# -*- encoding: UTF-8 -*-
import datetime

from db.data_read import StockBriefRead, StockRead
from db.data_storage import StockBriefStorage, StockStorage
from db.data_type import StockBrief, StockData
from log.log import LOG
from stock_tushare.stock_tu_share import get_tushare_pro
from util.utils import get_before_year


class FetchStock:
    def update_stock(self):
        """
        更新股票信息：
        1.stock_basic 获取基本信息,并存储
        2.更新股票详情
        :return:
        """
        stock_brief_read = StockBriefRead()
        stocks_brief = stock_brief_read.get_stock_brief(None)
        if stocks_brief is None or len(stocks_brief) == 0:
            self.__update_brief_stocks()
            stocks_brief = stock_brief_read.get_stock_brief(None)
        self.__update_daily_stocks(stocks_brief)

    def __update_brief_stocks(self):
        stock_brief_storage = StockBriefStorage()
        data = get_tushare_pro().stock_basic(exchange='',
                                             list_status='L',
                                             fields='ts_code,symbol,name,area,industry,market,list_status,list_date')
        stock_brief_list = self.__convert_basic(data)
        stock_brief_storage.stock_brief_storage(stock_brief_list)

    def __update_daily_stocks(self, stocks_brief):
        if stocks_brief is None:
            LOG.log('__update_daily_stocks error data_list is None')
            return
        self.__update_daily_stocks_thread(stocks_brief)

    def __update_daily_stocks_thread(self, stocks_brief):
        """
        更新数据
        :return:
        """
        for index, stock_brief in enumerate(stocks_brief):
            LOG.log('__update_daily_stocks_thread index %s size %s' % (index, len(stocks_brief)))
            self.__update_data_task(stock_brief)

    def __update_data_task(self, stock_brief):
        """
        更新数据
        :param stock_brief:
        :return:
        """
        #  get stock detail
        stock_storage = StockStorage()
        stock_read = StockRead()
        stock_list = stock_read.get_stock(stock_brief.ts_code, None)
        current_time = datetime.datetime.now().strftime("%Y%m%d")
        data = None
        if stock_list is None or len(stock_list) == 0:
            # start_time = stock_brief.list_date
            start_time = get_before_year(5)
            try:
                LOG.log('__update_data_task  get all data ts_code %s daily start_time %s' % (
                    stock_brief.ts_code, start_time))
                data = get_tushare_pro().daily(ts_code=stock_brief.ts_code, start_date=start_time,
                                               end_date=current_time)
            except BaseException as e:
                LOG.log('__update_data_task update data ts_code %s daily error %s' % (stock_brief.ts_code, str(e)))
        else:
            start_time = stock_list[-1].date
            if start_time is not None and start_time < current_time:
                try:
                    LOG.log('__update_data_task  ts_code %s daily start_time %s' % (stock_brief.ts_code, start_time))
                    data = get_tushare_pro().daily(ts_code=stock_brief.ts_code, start_date=start_time,
                                                   end_date=current_time)
                except BaseException as e:
                    LOG.log('__update_data_task ts_code %s daily error %s' % (stock_brief.ts_code, str(e)))
            else:
                LOG.log('__update_data_task ts_code %s daily current_time ==  start_time %s,%s' % (
                    stock_brief.ts_code, start_time, current_time))

        if data is not None:
            stock_list = self.__convert_daily(data)
            LOG.log('__update_data_task ts_code %s stock_list size %d' % (stock_brief.ts_code, len(stock_list)))

            if stock_storage is not None:
                sort_stock_list = self.sorted_list_by_date(stock_list)
                stock_storage.stock_storage(stock_brief.ts_code, sort_stock_list)
        else:
            LOG.log('__update_data_task ts_code %s have exist' % stock_brief.ts_code)

    @staticmethod
    def sorted_list_by_date(stock_list):
        return sorted(stock_list, key=lambda stock: stock.date)

    @staticmethod
    def __convert_basic(data):
        stock_brief_list = []
        for index, row in data.iterrows():
            stock_brief = StockBrief()
            stock_brief.ts_code = row['ts_code']
            stock_brief.symbol = row['symbol']
            stock_brief.name = row['name']
            stock_brief.area = row['area']
            stock_brief.industry = row['industry']
            stock_brief.market = row['market']
            stock_brief.list_status = row['list_status']
            stock_brief.list_date = row['list_date']
            stock_brief_list.append(stock_brief)
        return stock_brief_list

    @staticmethod
    def __convert_daily(data):
        stock_list = []
        for index, row in data.iterrows():
            stock_data = StockData()
            stock_data.date = row['trade_date']
            stock_data.stock_open = row['open']
            stock_data.high = row['high']
            stock_data.lower = row['low']
            stock_data.close = row['close']
            stock_data.pre_close = row['pre_close']
            stock_data.change = row['change']
            stock_data.pct_chg = row['pct_chg']
            stock_data.vol = row['vol']
            stock_data.amount = row['amount']
            stock_list.append(stock_data)
        return stock_list
