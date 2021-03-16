#!/usr/bin/env python3
"""4. Tasks
"""
from asyncio import as_completed
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """he code is nearly identical to wait_n except
     task_wait_random is being called."""
    data = [task_wait_random(max_delay) for i in range(n)]

    wait_list = []
    for i in as_completed(data):
        await_i = await i
        wait_list.append(await_i)
    return wait_list
