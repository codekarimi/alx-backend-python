#!/usr/bin/env python3
"""
Measure the runtime
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the runtime
    Returns a float of the runtime / n
    """
    start = time.time()
    await wait_n(n, max_delay)
    end = time.time()
    total_time = end - start
    return total_time / n
