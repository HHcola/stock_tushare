# -*- coding: utf-8 -*-
import logging
import os

LOG_FILE = 'log.txt'
LOG_FORMAT = "%(message)s"


class Log:
    def __init__(self, clean=False):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter(LOG_FORMAT)

        if clean:
            if os.path.isfile(LOG_FILE):
                with open(LOG_FILE, 'w') as f:
                    pass

        fh = logging.FileHandler(LOG_FILE)
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)

        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(formatter)

        self.logger.addHandler(ch)
        self.logger.addHandler(fh)

    def log(*args):
        s = ''
        for index, i in enumerate(args):
            if index > 0:
                s += (str(i) + ' ')

        logging.debug(s)

LOG = Log(True)
