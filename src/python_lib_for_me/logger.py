'''
ロガーモジュール
参照URL：https://docs.python.org/ja/3/howto/logging.html
'''

from json import load
from logging import Logger, config, getLogger
from typing import Optional, TextIO


def get_logger(module_name: str) -> Logger:
    '''
    ロガー取得
    
    Args:
        module_name (str): モジュール名
    
    Returns:
        Logger: ロガー
    '''
    
    try:
        log_env_config_obj: TextIO = open("./config/log_env_config.json", "r", encoding="utf-8")
        config.dictConfig(load(log_env_config_obj))
        logger: Logger = getLogger(module_name)
    except Exception as e:
        raise(e)
    
    return logger


def log_deb(logger: Logger, msg: str) -> None:
    '''
    ログ出力(DEBUG)
    
    Args:
        logger (Logger) : ロガー
        msg (str)       : メッセージ
    
    Returns:
        -
    '''
    
    try:
        logger.debug(msg, stacklevel=2)
    except Exception as e:
        raise(e)
    
    return None


def log_inf(logger: Logger, msg: str) -> None:
    '''
    ログ出力(INFO)
    
    Args:
        logger (Logger) : ロガー
        msg (str)       : メッセージ
    
    Returns:
        -
    '''
    
    try:
        logger.info(msg, stacklevel=2)
    except Exception as e:
        raise(e)
    
    return None


def log_war(logger: Logger, msg: str, exception: Optional[Exception] = None) -> None:
    '''
    ログ出力(WARNING)
    
    Args:
        logger (Logger)                             : ロガー
        msg (str)                                   : メッセージ
        exception (Optional[Exception], optional)   : 例外
    
    Returns:
        -
    
    Notes:
        - 例外発生時にメッセージと例外情報(1行)を出力し、処理を続行する場合に使用する
    '''
    
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
    '''
    ログ出力(ERROR)
    
    Args:
        logger (Logger) : ロガー
        msg (str)       : メッセージ
    
    Returns:
        -
    
    Notes:
        - 例外発生時にメッセージを出力し、処理を中断する場合に使用する
    '''
    
    try:
        logger.error(msg, stacklevel=2)
    except Exception as e:
        raise(e)
    
    return None


def log_exc(logger: Logger, msg: str) -> None:
    '''
    ログ出力(EXCEPTION)
    
    Args:
        logger (Logger) : ロガー
        msg (str)       : メッセージ
    
    Returns:
        -
    
    Notes:
        - 例外発生時に処理を中断した後に、メッセージと例外情報を出力する場合に使用する
    '''
    
    try:
        logger.exception(msg, exc_info=True, stacklevel=2)
    except Exception as e:
        raise(e)
    
    return None
