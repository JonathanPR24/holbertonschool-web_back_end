#!/usr/bin/env python3
"""Script to measure runtime using asyncio.gather"""

import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension
# Import the async_comprehension coroutine


async def measure_runtime() -> float:
    """
    Measure the total runtime of running async_comprehension
    four times in parallel.

    Returns:
        float: Total runtime in seconds.
    """
    start = time.perf_counter()  # Record the starting time

    tasks = [async_comprehension() for _ in range(4)]  # Create a list of tasks
    await asyncio.gather(*tasks)  # Execute tasks in parallel using asyncio.gather

    total_time = time.perf_counter() - start  # Calculate the total runtime

    return total_time
