"""
ロガーモジュール
参照URL：https://docs.python.org/ja/3/howto/logging.html
"""

import inspect
import json
import logging
import os
import warnings
from logging import Logger, config
from typing import Any, Final, Optional, TextIO

import python_lib_for_me as pyl

LOG_ENV_CONFIG_FILE_PATH: Final[str] = "./config/log_env_config.json"


class CustomLogger:
    """
    カスタムロガー
    """

    def __init__(
        self,
        module_name: str,
        use_default_log_env_config_file: bool = True,
    ) -> None:
        """
        コンストラクタ

        Args:
            module_name (str)                           : モジュール名
            use_default_log_env_config_file (bool)      : デフォルトのログ環境設定ファイルの使用有無

        Raises:
            OSError: ファイル読み込み失敗
        """

        try:
            # ログ環境設定ファイルパスの生成
            log_env_config_file_path: str
            if use_default_log_env_config_file is True:
                # デフォルトファイルを使用する場合
                root_path_of_this_lib: str = os.path.dirname(inspect.getfile(pyl))
                log_env_config_file_path = (
                    f"{root_path_of_this_lib}/../../{LOG_ENV_CONFIG_FILE_PATH}"
                )
            else:
                # 各自で用意したファイルを使用する場合
                log_env_config_file_path = LOG_ENV_CONFIG_FILE_PATH

            # ログ環境設定ファイルの読み込み
            with open(log_env_config_file_path, "r", encoding="utf-8") as log_env_config_file_obj:
                log_env_config_dict: dict[Any, Any] = json.load(log_env_config_file_obj)
                config.dictConfig(log_env_config_dict)

            # ロガーの生成
            self.__logger: logging.Logger = logging.getLogger(module_name)
        except Exception as e:
            raise (e)

        return None

    def log_dbg(
        self,
        msg: str,
    ) -> None:
        """
        ログ出力(デバッグ)

        Args:
            msg (str) : メッセージ

        Returns:
            -
        """

        if self.__logger is not None:
            self.__logger.debug(msg, stacklevel=2)

        return None

    def log_inf(
        self,
        msg: str,
    ) -> None:
        """
        ログ出力(情報)

        Args:
            msg (str) : メッセージ

        Returns:
            -
        """

        if self.__logger is not None:
            self.__logger.info(msg, stacklevel=2)

        return None

    def log_wrn(
        self,
        msg: str,
        exception: Optional[Exception] = None,
    ) -> None:
        """
        ログ出力(警告)

        Args:
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

        if self.__logger is not None:
            self.__logger.warning(msg_and_err_msg, stacklevel=2)

        return None

    def log_err(
        self,
        msg: str,
    ) -> None:
        """
        ログ出力(エラー)

        Args:
            msg (str) : メッセージ

        Returns:
            -

        Notes:
            - 例外発生時にメッセージを出力し、処理を中断する場合に使用する
        """

        if self.__logger is not None:
            self.__logger.error(msg, stacklevel=2)

        return None

    def log_exc(
        self,
        msg: str,
    ) -> None:
        """
        ログ出力(例外)

        Args:
            msg (str) : メッセージ

        Returns:
            -

        Notes:
            - 例外発生時に処理を中断した後に、メッセージと例外情報を出力する場合に使用する
        """

        if self.__logger is not None:
            self.__logger.exception(msg, exc_info=True, stacklevel=2)

        return None


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

    warnings.warn(
        "`get_logger()`は非推奨です。`CustomLogger#__init__()`を代わりに使用してください。",
        DeprecationWarning,
        stacklevel=2,
    )

    try:
        log_env_config_file_obj: TextIO = open(
            "./config/log_env_config.json",
            "r",
            encoding="utf-8",
        )
        log_env_config_dict: dict[Any, Any] = json.load(log_env_config_file_obj)
        config.dictConfig(log_env_config_dict)
        logger: Logger = logging.getLogger(module_name)
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

    warnings.warn(
        "`log_deb()`は非推奨です。`CustomLogger#log_dbg()`を代わりに使用してください。",
        DeprecationWarning,
        stacklevel=2,
    )

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

    warnings.warn(
        "`log_inf()`は非推奨です。`CustomLogger#log_inf()`を代わりに使用してください。",
        DeprecationWarning,
        stacklevel=2,
    )

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

    warnings.warn(
        "`log_war()`は非推奨です。`CustomLogger#log_wrn()`を代わりに使用してください。",
        DeprecationWarning,
        stacklevel=2,
    )

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

    warnings.warn(
        "`log_err()`は非推奨です。`CustomLogger#log_err()`を代わりに使用してください。",
        DeprecationWarning,
        stacklevel=2,
    )

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

    warnings.warn(
        "`log_exc()`は非推奨です。`CustomLogger#log_exc()`を代わりに使用してください。",
        DeprecationWarning,
        stacklevel=2,
    )

    if logger is not None:
        logger.exception(msg, exc_info=True, stacklevel=2)

    return None
