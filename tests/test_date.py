from datetime import date, datetime
from typing import Final

import python_lib_for_me as mylib

BASE_DATE: Final[date] = datetime.strptime('2022-02-26', '%Y-%m-%d').date()


def test_get_first_date_of_this_month() -> None:
    actual_value: date = mylib.get_first_date_of_this_month(BASE_DATE)
    expected_value: date = datetime.strptime('2022-02-01', '%Y-%m-%d').date()
    assert actual_value == expected_value


def test_get_last_date_of_this_month() -> None:
    actual_value: date = mylib.get_last_date_of_this_month(BASE_DATE)
    expected_value: date = datetime.strptime('2022-02-28', '%Y-%m-%d').date()
    assert actual_value == expected_value


def test_get_first_date_of_next_month() -> None:
    actual_value: date = mylib.get_first_date_of_next_month(BASE_DATE)
    expected_value: date = datetime.strptime('2022-03-01', '%Y-%m-%d').date()
    assert actual_value == expected_value


def test_get_last_date_of_next_month() -> None:
    actual_value: date = mylib.get_last_date_of_next_month(BASE_DATE)
    expected_value: date = datetime.strptime('2022-03-31', '%Y-%m-%d').date()
    assert actual_value == expected_value


def test_get_first_date_of_last_month() -> None:
    actual_value: date = mylib.get_first_date_of_last_month(BASE_DATE)
    expected_value: date = datetime.strptime('2022-01-01', '%Y-%m-%d').date()
    assert actual_value == expected_value


def test_get_last_date_of_last_month() -> None:
    actual_value: date = mylib.get_last_date_of_last_month(BASE_DATE)
    expected_value: date = datetime.strptime('2022-01-31', '%Y-%m-%d').date()
    assert actual_value == expected_value


def test_gen_date_range() -> None:
    start_date: date = datetime.strptime('2022-02-01', '%Y-%m-%d').date()
    end_date: date = datetime.strptime('2022-02-05', '%Y-%m-%d').date()
    actual_values: list[date] = list(mylib.gen_date_range(start_date, end_date))
    expected_values: list[date] = [
        datetime.strptime('2022-02-01', '%Y-%m-%d').date(),
        datetime.strptime('2022-02-02', '%Y-%m-%d').date(),
        datetime.strptime('2022-02-03', '%Y-%m-%d').date(),
        datetime.strptime('2022-02-04', '%Y-%m-%d').date(),
        datetime.strptime('2022-02-05', '%Y-%m-%d').date(),
    ]
    assert actual_values == expected_values
