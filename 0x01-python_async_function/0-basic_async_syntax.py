#!/usr/bin/env python3
"""0. The basics of async
"""
import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """asynchronous coroutine that takes in an integer
     argumentnamed wait_random that waits for a random delay
      between 0 and max_delay (included and float value) seconds
       and eventually returns it."""
    t = uniform(0, max_delay)
    await asyncio.sleep(t)
    return t
