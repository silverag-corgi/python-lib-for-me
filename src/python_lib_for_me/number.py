"""
数値モジュール
"""

from decimal import ROUND_HALF_UP, Decimal
from typing import Union


def round_half_up(
    number: Union[float, Decimal],
    num_of_digits: int = 0,
) -> Decimal:
    """
    四捨五入

    Args:
        number (Union[float, Decimal]): 数値
        num_of_digits (int, optional): 桁数

    Returns:
        Decimal: 計算結果
    """

    digit: str = "0"
    if num_of_digits > 0:
        digit = "0." + "0" * (num_of_digits - 1) + "1"

    result: Decimal = Decimal(str(number)).quantize(Decimal(digit), rounding=ROUND_HALF_UP)

    return result
