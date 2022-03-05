'''
日付モジュール
'''

import calendar
from datetime import date, datetime, timedelta
from typing import Iterator
from zoneinfo import ZoneInfo

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


def convert_timestamp_to_jst(
        src_timestamp: str,
        src_timestamp_format: str = '%Y-%m-%d %H:%M:%S%z',
        jst_timestamp_format: str = '%Y-%m-%d %H:%M:%S'
    ) -> str:
    
    '''タイムスタンプJST変換'''
    
    src_datetime: datetime = datetime.strptime(src_timestamp, src_timestamp_format)
    jst_datetime: datetime = src_datetime.astimezone(ZoneInfo('Japan'))
    jst_timestamp: str = datetime.strftime(jst_datetime, jst_timestamp_format)
    
    return jst_timestamp


def convert_timestamp_to_utc(
        src_timestamp: str,
        src_timestamp_format: str = '%Y-%m-%d %H:%M:%S%z',
        utc_timestamp_format: str = '%Y-%m-%d %H:%M:%S'
    ) -> str:
    
    '''タイムスタンプUTC変換'''
    
    src_datetime: datetime = datetime.strptime(src_timestamp, src_timestamp_format)
    utc_datetime: datetime = src_datetime.astimezone(ZoneInfo('UTC'))
    utc_timestamp: str = datetime.strftime(utc_datetime, utc_timestamp_format)
    
    return utc_timestamp
