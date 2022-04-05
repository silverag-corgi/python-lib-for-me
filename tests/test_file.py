import python_lib_for_me as pyl


def test_generate_file_name() -> None:
    actual_value: str = pyl.generate_file_name('./dest/farm_report_list/temp.csv')
    expected_value: str = 'temp'
    assert actual_value == expected_value
