import time
from typing import Callable, Optional
from selenium.common.exceptions import TimeoutException


def wait_until(valid: Callable[[], bool], timeout: int = 20, timeout_message: Optional[str] = None,
               interval: float = 1, raise_exception: bool = True):
    """
    Wait until validation function pass
    :param valid: function to be used for validation. It should return True if validation passed, or False otherwise
    :param timeout: optional maximum time for validation to pass
    :param timeout_message: optional message to be thrown within TimeoutException
    :param interval: optional time used as interval between checking validation
    :raises TimeoutException: validation block doesn't pass until timeout
    :param raise_exception: optional flag if exception have to be raised
    """
    end_time = time.time() + timeout
    while time.time() < end_time:
        if not valid():
            time.sleep(interval)
        else:
            return
    if timeout_message is None:
        timeout_message = f'{valid.__name__} is False after {timeout} seconds"'
    if raise_exception:
        raise TimeoutException(timeout_message)
