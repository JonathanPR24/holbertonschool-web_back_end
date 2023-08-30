#!/usr/bin/env python3
"""
Script containing the task_wait_random function.
"""
import asyncio
from typing import any
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Coroutine:
    """
    Returns an asyncio.Task that runs the wait_random coroutine.
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
