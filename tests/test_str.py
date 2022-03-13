import python_lib_for_me as pyl


def test_generate_str_list_from_csv() -> None:
    actual_values: list[str] = pyl.generate_str_list_from_csv('str01, str02, str03')
    expected_values: list[str] = ['str01', 'str02', 'str03']
    assert actual_values == expected_values
