import time
from typing import Callable, TypeVar, Optional
import random

from ..exceptions import TTDError, RateLimitError, ServerError

T = TypeVar('T')

class RetryHandler:
    def __init__(
        self, 
        max_retries: int = 3,
        base_delay: float = 1.0,
        max_delay: float = 60.0,
        jitter: bool = True
    ):
        self.max_retries = max_retries
        self.base_delay = base_delay
        self.max_delay = max_delay
        self.jitter = jitter

    def calculate_delay(self, retry_count: int, retry_after: Optional[float] = None) -> float:
        if retry_after:
            return retry_after
            
        delay = min(
            self.max_delay,
            self.base_delay * (2 ** retry_count)
        )
        
        if self.jitter:
            delay = random.uniform(0, delay)
            
        return delay

    def execute(self, func: Callable[[], T]) -> T:
        last_exception = None
        
        for retry_count in range(self.max_retries + 1):
            try:
                return func()
            except RateLimitError as e:
                last_exception = e
                delay = self.calculate_delay(retry_count, e.retry_after)
                time.sleep(delay)
                continue
            except ServerError as e:
                last_exception = e
                delay = self.calculate_delay(retry_count)
                time.sleep(delay)
                continue
            except TTDError:
                raise
                
        raise last_exception