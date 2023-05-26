"""
ロガーモジュール
参照URL：https://docs.python.org/ja/3/howto/logging.html
"""

import inspect
import logging
import os
from logging import config
from typing import Any, Final, Optional, cast

import yaml

import python_lib_for_me as pyl

LOG_ENV_CONFIG_FILE_PATH: Final[str] = "./config/log_env_config.yml"


class CustomLogger:
    """
    カスタムロガー
    """

    def __init__(
        self,
        module_name: str,
        use_default_log_env_config_file: bool = True,
        use_debug_mode: bool = False,
    ) -> None:
        """
        コンストラクタ

        Args:
            module_name (str)                       : モジュール名
            use_default_log_env_config_file (bool)  : デフォルトのログ環境設定ファイルの使用有無
            use_debug_mode (bool)                   : デバッグモード使用有無

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
                log_env_config_dict: dict[Any, Any] = cast(
                    dict, yaml.safe_load(log_env_config_file_obj)
                )
                config.dictConfig(log_env_config_dict)

            # ロガーの生成
            self.__logger: logging.Logger = logging.getLogger(module_name)

            # ログレベルの設定
            if use_debug_mode is True:
                self.__logger.setLevel(logging.DEBUG)
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
