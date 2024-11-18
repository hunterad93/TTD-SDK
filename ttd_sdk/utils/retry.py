import time
from typing import Callable, TypeVar
import random
import logging

from ..exceptions import TTDError, RateLimitError, ServerError

T = TypeVar('T')
logger = logging.getLogger(__name__)

class RetryHandler:
    def __init__(
        self, 
        max_retries: int = 3,
        base_delay: float = 66.0,
        min_delay: float = 30.0,
        jitter: bool = True
    ):
        self.max_retries = max_retries
        self.base_delay = base_delay
        self.min_delay = min_delay
        self.jitter = jitter

    def calculate_delay(self, retry_after: float, retry_count: int) -> float:
        """Calculate delay with optional jitter"""
        delay = max(retry_after, self.min_delay)
        
        if self.jitter:
            # Small jitter range (10%) to avoid thundering herd
            delay = random.uniform(delay * 0.9, delay * 1.1)
        
        return delay

    def execute(self, func: Callable[[], T]) -> T:
        last_exception = None
        
        for retry_count in range(self.max_retries + 1):
            try:
                return func()
            except RateLimitError as e:
                last_exception = e
                retry_after = e.retry_after  # Will always return a float (defaults to 60.0)
                delay = self.calculate_delay(retry_after, retry_count)
                
                rate_info = e.rate_limit_info
                logger.info(
                    f"Rate limit exceeded. "
                    f"Window size: {rate_info.get('window_size')}ms, "
                    f"Max calls: {rate_info.get('max_calls')}, "
                    f"Window start: {rate_info.get('window_start')}. "
                    f"Waiting {delay:.2f} seconds before retry {retry_count + 1}/{self.max_retries}"
                )
                
                time.sleep(delay)
                continue
            except ServerError as e:
                last_exception = e
                # For server errors, use exponential backoff
                delay = self.base_delay * (2 ** retry_count)
                if self.jitter:
                    delay = random.uniform(delay * 0.5, delay * 1.5)
                
                logger.info(
                    f"Server error occurred. Status: {e.status_code}. "
                    f"Waiting {delay:.2f} seconds before retry {retry_count + 1}/{self.max_retries}"
                )
                time.sleep(delay)
                continue
            except TTDError:
                raise
                
        raise last_exception