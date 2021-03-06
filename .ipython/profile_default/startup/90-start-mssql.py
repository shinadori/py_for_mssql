#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# flake8: noqa
'''
@File    :   90-start-mssql.py
@Author  :   Billy Zhou
@Time    :   2021/03/12
@Version :   1.0.0
@Desc    :   None
'''


import sys
from pathlib import Path
sys.path.append("D:\pycharm\py_for_mssql") # change the path to your workspace

from sqldb.init_db import Sqldb
from sqldb.func_basic import sql_read
from sqldb.func_query import sql_query

if __name__ == '__main__':
    import logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(name)s %(levelname)s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S')
    logging.debug('start DEBUG')
    logging.debug('==========================================================')

    logging.debug('==========================================================')
    logging.debug('end DEBUG')
