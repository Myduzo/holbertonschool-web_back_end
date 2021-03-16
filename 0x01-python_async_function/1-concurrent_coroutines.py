#!/usr/bin/env python3
"""1. Let's execute multiple coroutines
 at the same time with async
"""
from asyncio import as_completed
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """wait_n should return the list of all
     the delays (float values)."""
    data = [wait_random(max_delay) for i in range(n)]

    wait_list = []
    for i in as_completed(data):
        await_i = await i
        wait_list.append(await_i)
    return wait_list
