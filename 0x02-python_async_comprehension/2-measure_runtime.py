#!/usr/bin/env python3
"""a coroutine to measure the execution time"""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measure_runtime - function execute async_com four times
    Arguments:
        nothing
    Returns:
        the total runtime
    """
    t_begin = time.perf_counter()
    t = [async_comprehension() for i in range(4)]
    await asyncio.gather(*t)
    t_end = time.perf_counter()
    return (t_end - t_begin)
