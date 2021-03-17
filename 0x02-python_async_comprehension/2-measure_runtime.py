#!/usr/bin/env python3
"""2. Run time for four parallel comprehensions
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure_runtime coroutine that
     will execute async_comprehension four times
      in parallel using asyncio.gather."""
    start = time.time()
    comp = [async_comprehension() for i in range(4)]
    await asyncio.gather(*comp)
    end = time.time()
    return end - start
