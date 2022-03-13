'''
文字列モジュール
'''


def generate_str_list_from_csv(str_of_csv_format: str) -> list[str]:
    '''
    文字列リスト生成
    
    Args:
        str_of_csv_format (str): CSV形式の文字列
    
    Returns:
        list[str]: 文字列リスト
    '''
    
    str_list: list[str] = str_of_csv_format.split(',')
    for index, value in enumerate(str_list, start=0):
        str_list[index] = value.strip()
    
    return str_list
