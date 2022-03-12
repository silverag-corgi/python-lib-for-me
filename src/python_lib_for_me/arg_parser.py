'''
引数解析モジュール
'''

import argparse
import sys
from logging import Logger
from typing import Any, Optional

import python_lib_for_me as pyl


class CustomArgumentParser(argparse.ArgumentParser):
    '''
    カスタム引数解析
    
    Extends:
        - argparse.ArgumentParser
    
    Overrides:
        - _print_message
    
    Notes:
        - mainパッケージのモジュールで引数を解析する際に使用する
    '''
    
    def _print_message(self, message: Any, file: Any = None) -> None:
        '''
        メッセージ出力
        
        ロガーでメッセージを出力する
        
        Args:
            message (Any): メッセージ (str)
            file (Any, optional): テキストストリーム (TextIO)
        
        Notes:
            - Help-printing methods
        '''
        
        lg: Optional[Logger] = None
        
        try:
            lg = pyl.get_logger(__name__)
            
            if file is sys.stdout:
                pyl.log_inf(lg, f'\n{message}')
            elif file is sys.stderr:
                pyl.log_err(lg, f'\n{message}')
        except Exception as e:
            raise(e)
        
        return None
