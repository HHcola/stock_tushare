# -*- coding: UTF-8 -*-
from stock_tushare.fetch_stock_data import FetchStock


def main():
    fetch_stock = FetchStock()
    fetch_stock.update_stock()


if __name__ == '__main__':
    main()
