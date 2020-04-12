# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod

class Strategy(metaclass=ABCMeta):
    @abstractmethod
    def enter(self, data_frame):
        """
        入市
        :return:
        """
        raise NotImplementedError('enter is not implemented')

    @abstractmethod
    def leave(self, ts_code):
        """
        离市
        :param ts_code: 股票代码
        :return:
        """
        raise NotImplementedError('leave is not implemented')

    @abstractmethod
    def stop_loss(self, ts_code):
        """
        止损
        :param ts_code:
        :return:
        """
        raise NotImplementedError('stop_loss is not implemented')

    @abstractmethod
    def position(self, ts_code):
        """
        建立头寸
        :param ts_code
        :return:
        """
        raise NotImplementedError('position is not implemented')

