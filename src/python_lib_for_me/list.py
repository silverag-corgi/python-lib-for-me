"""
リストモジュール
"""


def split_list(
    elements: list,
    num_of_elements: int,
) -> list[list]:
    """
    リスト分割

    Args:
        elements (list)         : 要素リスト
        num_of_elements (int)   : 分割単位の要素数

    Returns:
        list[list]: 分割結果リスト
    """

    items_list: list[list] = [
        elements[index : index + num_of_elements]
        for index in range(0, len(elements), num_of_elements)
    ]

    return items_list
