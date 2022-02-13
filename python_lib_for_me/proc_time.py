import time
from logging import Logger
from typing import Any, Callable, Optional

from python_lib_for_me import logger


def measure_proc_time(function_object: Callable) -> Any:
    
    '''
    処理時間計測デコレータ
    
    Summary:
        処理時間を計測するデコレータ。
    
    Args:
        function_object (Callable): 関数オブジェクト
    
    Returns:
        Any: 関数オブジェクトの処理結果
    
    Example:
        - @マークを使用して呼び出す\n
        @python_lib_for_me.measure_proc_time\n
        def foobar(var):\n
        - 関数として呼び出す\n
        python_lib_for_me.measure_proc_time(foobar)(var)\n
    '''
    
    def wrapper(*args, **kargs) -> Any:
        lg: Optional[Logger] = None
        
        try:
            # ロガー取得
            lg = logger.get_logger(__name__)
            
            # 開始時間設定
            start_time: float = time.perf_counter()
            
            # 処理実行
            result: Any = function_object(*args, **kargs)
            
            # 処理時間計算
            end_time: float = time.perf_counter()
            proc_time: float = end_time - start_time
            lg.info(f'{function_object.__name__}：{proc_time:.05f}秒')
        except Exception as e:
            raise(e)
        
        return result
    
    return wrapper
