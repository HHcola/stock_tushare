# -*- encoding: UTF-8 -*-

class GlobalVar:
    # stock_tushare token for get data
    token = "cd45e85f67ffbe46872faaaff51afb60fd71479d179dc21a970eb0d6"
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
