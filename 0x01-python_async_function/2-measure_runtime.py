#!/usr/bin/env python3
"""A function that measures the total execution time for
another function"""
from time import perf_counter
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures the total execution time of another
    function
    Args:
        n: the number of coroutines
        max_delay: the maximum delay between coroutines
    Returns: an approximate elapsed time
    """
    begin = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    e = perf_counter() - begin
    return e / n
