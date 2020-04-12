# -*- encoding: UTF-8 -*-

import tushare as ts
from stock_tushare import gl


def init_tushare():
    """
    初始化 stock_tushare
    :return:
    """
    ts.set_token(gl.get_token())


def get_tushare_pro():
    """
    获取tushare pro 接口
    :return:
    """
    if not gl.get_token_init():
        init_tushare()
        gl.set_token_init(True)
    return ts.pro_api()
