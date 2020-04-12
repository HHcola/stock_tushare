# -*- encoding: UTF-8 -*-

class GlobalVar:
    # stock_tushare token for get data
    token = "6e8383ff4a4a297e1fba22cc65a1dc2536701fbb6a48ae79621b1c4d"
    token_init = False


def get_token():
    """
    获取token
    :return:
    """
    return GlobalVar.token


def set_token_init(init):
    """
    设置是否初始化
    :param init:
    :return:
    """
    GlobalVar.token_init = init


def get_token_init():
    """
    获取是否初始化
    :return:
    """
    return GlobalVar.token_init
