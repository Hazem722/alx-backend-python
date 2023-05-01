#!/usr/bin/env python3
"""an async routine that spawns wait_random n times with a
specified max delay between each call."""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns wait_random n times with a specified max
    delay between each call.
    Args:
        n: number of times to spawn wait_random
        max_delay: maximum delay between each call
    Returns:
        list of delays
    """
    ts = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await t for t in asyncio.as_completed(ts)]
