# -*- coding: UTF-8 -*-
import datetime


def is_weekday():
    return datetime.datetime.today().weekday() < 5


def get_before_year(before_year):
    """
    获取N年前
    :param before_year:
    :return:
    """
    now = datetime.datetime.now()
    year = int(now.year) - before_year
    current_time = datetime.datetime.now().strftime("%m%d")
    return str(year) + current_time


def get_before_date(before_day):
    """
    获取N天前的日期
    :param before_day:
    :return:
    """
    today = datetime.datetime.now()
    # 计算偏移量
    offset = datetime.timedelta(days=-before_day)
    # 获取想要的日期的时间
    re_date = (today + offset).strftime('%Y%m%d')
    return re_date
