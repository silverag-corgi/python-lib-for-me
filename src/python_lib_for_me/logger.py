'''
ロガーモジュール
参照URL：https://docs.python.org/ja/3/howto/logging.html
'''

from json import load
from logging import Logger, config, getLogger
from typing import TextIO


def get_logger(name: str) -> Logger:
    '''ロガー取得'''
    
    try:
        log_env_config_obj: TextIO = open("./config/log_env_config.json", "r", encoding="utf-8")
        config.dictConfig(load(log_env_config_obj))
        lg: Logger = getLogger(name)
    except Exception as e:
        raise(e)
    
    return lg
