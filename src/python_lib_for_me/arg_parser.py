"""
引数解析モジュール
"""

import argparse
import sys
from typing import Any

from typing_extensions import override

import python_lib_for_me as pyl


class CustomArgumentParser(argparse.ArgumentParser):
    """
    カスタム引数解析

    Notes:
        - mainパッケージのモジュールで引数を解析する際に使用する
    """

    @override
    def _print_message(self, message: Any, file: Any = None) -> None:
        """
        メッセージ出力

        ロガーでメッセージを出力する

        Args:
            message (Any): メッセージ (str)
            file (Any, optional): テキストストリーム (TextIO)

        Notes:
            `_print_message`は下記関数で呼び出される
            >>> # Help-printing methods
            >>> def print_usage(self, file=None):
            >>> def print_help(self, file=None):
            >>> # Exiting methods
            >>> def exit(self, status=0, message=None):
        """

        try:
            clg: pyl.CustomLogger = pyl.CustomLogger(__name__)

            if file is sys.stdout:
                clg.log_inf(f"\n{message}")
            elif file is sys.stderr:
                clg.log_err(f"\n{message}")
        except Exception as e:
            raise (e)

        return None
