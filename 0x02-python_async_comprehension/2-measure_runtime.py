#!/usr/bin/env python3
"""
Module provides asynchronous function that measures the runtime of
running 4 instances of async_comprehension function from
'1-async_comprehension' module
"""
import asyncio
import time
from importlib import import_module as using

async_comprehension = using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Asynchronous function that measures and returns runtime of
    running 4 instances of async_comprehension function.

    Returns:
        float: The runtime of the async_comprehension function in seconds.
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_time
