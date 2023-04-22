"""
ロガーモジュール
参照URL：https://docs.python.org/ja/3/howto/logging.html
"""

from json import load
from logging import Logger, config, getLogger
from typing import Optional, TextIO


def get_logger(
    module_name: str,
) -> Logger:
    """
    ロガー取得

    Args:
        module_name (str): モジュール名

    Returns:
        Logger: ロガー
    """

    try:
        log_env_config_obj: TextIO = open("./config/log_env_config.json", "r", encoding="utf-8")
        config.dictConfig(load(log_env_config_obj))
        logger: Logger = getLogger(module_name)
    except Exception as e:
        raise (e)

    return logger


def log_deb(
    logger: Optional[Logger],
    msg: str,
) -> None:
    """
    ログ出力(デバッグ)

    Args:
        logger (Optional[Logger])   : ロガー
        msg (str)                   : メッセージ

    Returns:
        -
    """

    if logger is not None:
        logger.debug(msg, stacklevel=2)

    return None


def log_inf(
    logger: Optional[Logger],
    msg: str,
) -> None:
    """
    ログ出力(情報)

    Args:
        logger (Optional[Logger])   : ロガー
        msg (str)                   : メッセージ

    Returns:
        -
    """

    if logger is not None:
        logger.info(msg, stacklevel=2)

    return None


def log_war(
    logger: Optional[Logger],
    msg: str,
    exception: Optional[Exception] = None,
) -> None:
    """
    ログ出力(警告)

    Args:
        logger (Optional[Logger])                   : ロガー
        msg (str)                                   : メッセージ
        exception (Optional[Exception], optional)   : 例外

    Returns:
        -

    Notes:
        - 例外発生時にメッセージと例外情報(1行)を出力し、処理を続行する場合に使用する
    """

    msg_and_err_msg: str
    if exception is None:
        msg_and_err_msg = msg
    else:
        err_msg: str = str(exception).replace("\n", ", ")
        msg_and_err_msg = f"{msg}(err_msg:{err_msg})"

    if logger is not None:
        logger.warning(msg_and_err_msg, stacklevel=2)

    return None


def log_err(
    logger: Optional[Logger],
    msg: str,
) -> None:
    """
    ログ出力(エラー)

    Args:
        logger (Optional[Logger])   : ロガー
        msg (str)                   : メッセージ

    Returns:
        -

    Notes:
        - 例外発生時にメッセージを出力し、処理を中断する場合に使用する
    """

    if logger is not None:
        logger.error(msg, stacklevel=2)

    return None


def log_exc(
    logger: Optional[Logger],
    msg: str,
) -> None:
    """
    ログ出力(例外)

    Args:
        logger (Optional[Logger])   : ロガー
        msg (str)                   : メッセージ

    Returns:
        -

    Notes:
        - 例外発生時に処理を中断した後に、メッセージと例外情報を出力する場合に使用する
    """

    if logger is not None:
        logger.exception(msg, exc_info=True, stacklevel=2)

    return None
