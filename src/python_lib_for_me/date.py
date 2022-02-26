'''
日付モジュール
'''

import calendar
from datetime import date, timedelta
from typing import Iterator

from dateutil.relativedelta import relativedelta


def get_first_date_of_this_month(base_date: date) -> date:
    '''今月初日取得'''
    base_date_by_month: date = base_date + relativedelta(months=0)
    base_date_by_month_day: date = base_date_by_month.replace(
            day=1
        )
    
    return base_date_by_month_day


def get_last_date_of_this_month(base_date: date) -> date:
    '''今月末日取得'''
    base_date_by_month: date = base_date + relativedelta(months=0)
    base_date_by_month_day: date = base_date_by_month.replace(
            day=calendar.monthrange(base_date_by_month.year, base_date_by_month.month)[1]
        )
    
    return base_date_by_month_day


def get_first_date_of_next_month(base_date: date) -> date:
    '''来月初日取得'''
    base_date_by_month: date = base_date + relativedelta(months=1)
    base_date_by_month_day: date = base_date_by_month.replace(
            day=1
        )
    
    return base_date_by_month_day


def get_last_date_of_next_month(base_date: date) -> date:
    '''来月末日取得'''
    base_date_by_month: date = base_date + relativedelta(months=1)
    base_date_by_month_day: date = base_date_by_month.replace(
            day=calendar.monthrange(base_date_by_month.year, base_date_by_month.month)[1]
        )
    
    return base_date_by_month_day


def get_first_date_of_last_month(base_date: date) -> date:
    '''先月初日取得'''
    base_date_by_month: date = base_date + relativedelta(months=-1)
    base_date_by_month_day: date = base_date_by_month.replace(
            day=1
        )
    
    return base_date_by_month_day


def get_last_date_of_last_month(base_date: date) -> date:
    '''先月末日取得'''
    base_date_by_month: date = base_date + relativedelta(months=-1)
    base_date_by_month_day: date = base_date_by_month.replace(
            day=calendar.monthrange(base_date_by_month.year, base_date_by_month.month)[1]
        )
    
    return base_date_by_month_day


def gen_date_range(start_date: date, end_date: date) -> Iterator[date]:
    '''日付範囲生成'''
    for count in range((end_date - start_date).days + 1):
        yield start_date + timedelta(days=count)
