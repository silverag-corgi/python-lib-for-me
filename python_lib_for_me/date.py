'''
日付モジュール
'''

import calendar
from datetime import date, timedelta

from dateutil.relativedelta import relativedelta


def get_first_date_of_this_month(date: date) -> date:
    '''今月初日取得'''
    return date.replace(day=calendar.monthrange(date.year, date.month)[0])


def get_last_date_of_this_month(date: date) -> date:
    '''今月末日取得'''
    return date.replace(day=calendar.monthrange(date.year, date.month)[1])


def get_first_date_of_next_month(date: date) -> date:
    '''来月初日取得'''
    return date.replace(day=calendar.monthrange(date.year, date.month)[0]) + relativedelta(months=1)


def get_last_date_of_next_month(date: date) -> date:
    '''来月末日取得'''
    return date.replace(day=calendar.monthrange(date.year, date.month)[1]) + relativedelta(months=1)


def get_first_date_of_last_month(date: date) -> date:
    '''先月初日取得'''
    return date.replace(day=calendar.monthrange(date.year, date.month)[0]) + relativedelta(months=-1)


def get_last_date_of_last_month(date: date) -> date:
    '''先月末日取得'''
    return date.replace(day=calendar.monthrange(date.year, date.month)[1]) + relativedelta(months=-1)


def gen_date_range(start_date: date, end_date: date) -> date:
    '''日付範囲生成'''
    for count in range((end_date - start_date).days + 1):
        yield start_date + timedelta(days=count)
