"""
ファイルモジュール
"""

import os


def generate_file_name(
    file_path: str,
) -> str:
    """ファイル名生成"""
    file_name: str = os.path.splitext(os.path.basename(file_path))[0]
    return file_name
