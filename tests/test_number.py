from decimal import Decimal

import python_lib_for_me as pyl


def test_round_half_up_01() -> None:
    actual_values: Decimal = pyl.round_half_up(1.234, 2)
    expected_values: Decimal = Decimal("1.23")
    assert actual_values == expected_values


def test_round_half_up_02() -> None:
    actual_values: Decimal = pyl.round_half_up(1.235, 2)
    expected_values: Decimal = Decimal("1.24")
    assert actual_values == expected_values


def test_round_half_up_03() -> None:
    actual_values: Decimal = pyl.round_half_up(Decimal("1.234"), 2)
    expected_values: Decimal = Decimal("1.23")
    assert actual_values == expected_values


def test_round_half_up_04() -> None:
    actual_values: Decimal = pyl.round_half_up(Decimal("1.235"), 2)
    expected_values: Decimal = Decimal("1.24")
    assert actual_values == expected_values
