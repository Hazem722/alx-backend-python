#!/usr/bin/env python3
"""an asynchronous coroutine that waits a random delay and eventually returns it"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Returns a random float between 0 and max_delay
    Args:
        max_delay: maximum delay to return
    Returns:
        random float between 0 and max_delay
    """
    r = random.uniform(0, max_delay)
    await asyncio.sleep(r)
    return r
