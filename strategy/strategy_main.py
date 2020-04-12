# -*- coding: UTF-8 -*-
import os

import datetime
import pandas as pd

from db.config import stock_brief_list
from db.data_read import StockRead
from log.log import LOG
from strategy.strategy_type import StrategyType
from strategy.trategy_data import get_all_stock, convert_to_dataframe
from strategy.turtle.turtle_strategy import TurtleStrategy

SAVE_FILE_NAME = "../data/trategy.cvs"


def main():
    run_strategy()


def run_strategy():
    stocks_brief = get_all_stock()
    if stocks_brief is None:
        LOG.log('run_strategy get_all_stock empty')
        return

    stock_detail_read = StockRead()
    strategy = get_strategy(StrategyType.TURTLE)

    strategy_data = pd.DataFrame(columns=stock_brief_list)
    data_list = [[0] * len(stock_brief_list) for _ in range(1)]
    date = None
    for brief in stocks_brief:
        stock_list = None
        if brief.market == "主板":
            stock_list = stock_detail_read.get_stock(brief.ts_code, None)
        if stock_list is not None:
            data_frame = convert_to_dataframe(stock_list)
            ret = strategy.enter(data_frame)
            if date is None:
                date = data_frame.data.iloc[0]['DATE']
            if ret:
                LOG.log('stock can enter %s name %s' % (brief.ts_code, brief.name))
                brief_list = brief.convert_to_list()
                data_list[0] = brief_list
                data = pd.DataFrame(data_list, columns=stock_brief_list)
                strategy_data = strategy_data.append(data, ignore_index=True)

    file_path = get_save_file(date)
    if os.path.exists(file_path):
        os.remove(file_path)
    strategy_data.to_csv(file_path)


def get_save_file(date):
    basedir = os.path.dirname(os.path.dirname(__file__))
    if date is not None:
        current_time = date
    else:
        current_time = datetime.datetime.now().strftime("%Y%m%d")
    LOG.log('BaseStock basedir %s ' % basedir)
    return basedir + '/data/trategy_' + current_time + '.cvs'


def get_strategy(strategy_type):
    if strategy_type == StrategyType.TURTLE:
        return TurtleStrategy()

if __name__ == '__main__':
    main()
