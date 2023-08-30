#!/usr/bin/env python3
"""Script that returns the list of all the delays"""
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Returns a list of asyncio. Run the task_wait_random coroutine."""
    delay_list: List[float] = []
    tasks: List[asyncio.Task] = []

    for _ in range(n):
        tasks.append(task_wait_random(max_delay))

    for task in asyncio.as_completed(tasks):
        delay = await task
        delay_list.append(delay)

    return delay_list
