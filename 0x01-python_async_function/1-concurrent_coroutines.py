#!/usr/bin/env python3
"""
Concurrent coroutines
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    Call wait_random n times
    Return a list of all the values obtained
    """
    mylist = []
    for _ in range(n):
        mylist.append(wait_random(max_delay))

    return [await x for x in asyncio.as_completed(mylist)]
