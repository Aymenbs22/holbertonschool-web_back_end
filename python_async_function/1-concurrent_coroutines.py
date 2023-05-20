#!/usr/bin/env python3
"""Create a measure_time function with integers n and
max_delay as arguments that measures the total execution
time for wait_n(n, max_delay), and returns
total_time / n. Your function should return a float"""


import asyncio
import random
from typing import List, Set, Dict, Tuple, Union, Callable

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Create a measure_time function with integers n and
max_delay as arguments that measures the total execution
time for wait_n(n, max_delay), and returns
total_time / n. Your function should return a float"""
    wait_randoms = [wait_random(max_delay) for i in range(n)]
    Lists = []
    for j in asyncio.as_completed(wait_randoms):
        Lists.append(await j)
    return (Lists)
