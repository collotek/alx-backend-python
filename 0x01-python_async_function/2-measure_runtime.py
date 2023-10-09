#!/usr/bin/env python3
"""measure time to execute a function"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measures the total execution time for wait_n(n, max_delay)

    Args:
        n (int): number of times to delay
        max_delay (int): max delay time

    Returns:
        float: average time
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()

    t = (end - start) / n

    return t
