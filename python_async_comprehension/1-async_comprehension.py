#!/usr/bin/env python3
"""Async comprehension coroutine"""

from typing import List
async_generator = __import__('0-async_generator').async_generator  # Import the async generator coroutine


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using async comprehension over async_generator.
    
    Returns:
        List[float]: A list of 10 random numbers.
    """
    # Use async comprehension to collect random numbers from async_generator
    return [i async for i in async_generator()]
