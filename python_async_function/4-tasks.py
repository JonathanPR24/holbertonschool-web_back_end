#!/usr/bin/env python3
"""
Script containing the task_wait_n function.
"""

import asyncio
from typing import List, Coroutine

task_wait_random = __import__('3-tasks').task_wait_random

def task_wait_n(n: int, max_delay: int) -> Coroutine:
    """
    Returns a list of asyncio.Tasks that run the task_wait_random coroutine.

    Args:
        n (int): The number of times to create the task.
        max_delay (int): The maximum delay for task_wait_random.

    Returns:
        Coroutine: A list of tasks to run the task_wait_random coroutine.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return asyncio.gather(*tasks)
