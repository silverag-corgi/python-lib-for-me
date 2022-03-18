import python_lib_for_me as pyl


def test_split_list() -> None:
    elements: list[str] = \
        ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10']
    actual_values: list[list[str]] = pyl.split_list(elements, 3)
    expected_values: list[list[str]] = \
        [['01', '02', '03'], ['04', '05', '06'], ['07', '08', '09'], ['10']]
    assert actual_values == expected_values
