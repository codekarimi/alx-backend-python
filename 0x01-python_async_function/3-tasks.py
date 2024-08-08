#!/usr/bin/env python3
"""
Tasks function
"""
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    function that takes an integer max_delay and returns a asyncio.Task
    """
    return asyncio.create_task(wait_n(max_delay))
