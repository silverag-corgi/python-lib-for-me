'''
ロガーモジュール
参照URL：https://docs.python.org/ja/3/howto/logging.html
'''

from json import load
from logging import Logger, config, getLogger
from typing import Optional, TextIO


def get_logger(module_name: str) -> Logger:
    '''ロガー取得'''
    
    try:
        log_env_config_obj: TextIO = open("./config/log_env_config.json", "r", encoding="utf-8")
        config.dictConfig(load(log_env_config_obj))
        logger: Logger = getLogger(module_name)
    except Exception as e:
        raise(e)
    
    return logger


def log_deb(logger: Logger, msg: str) -> None:
    '''ログ出力(DEBUG)'''
    
    try:
        logger.debug(msg, stacklevel=2)
    except Exception as e:
        raise(e)
    
    return None


def log_inf(logger: Logger, msg: str) -> None:
    '''ログ出力(INFO)'''
    
    try:
        logger.info(msg, stacklevel=2)
    except Exception as e:
        raise(e)
    
    return None


def log_war(logger: Logger, msg: str, exception: Optional[Exception] = None) -> None:
    '''ログ出力(WARNING)'''
    
    try:
        msg_and_err_msg: str = ''
        if exception is None:
            msg_and_err_msg = msg
        else:
            err_msg: str = str(exception).replace('\n', ' ')
            msg_and_err_msg = f'{msg}(err_msg:{err_msg})'
        logger.warning(msg_and_err_msg, stacklevel=2)
    except Exception as e:
        raise(e)
    
    return None


def log_err(logger: Logger, msg: str) -> None:
    '''ログ出力(ERROR)'''
    
    try:
        logger.error(msg, stacklevel=2)
    except Exception as e:
        raise(e)
    
    return None


def log_exc(logger: Logger, msg: str) -> None:
    '''ログ出力(EXCEPTION)'''
    
    try:
        logger.exception(msg, exc_info=True, stacklevel=2)
    except Exception as e:
        raise(e)
    
    return None
