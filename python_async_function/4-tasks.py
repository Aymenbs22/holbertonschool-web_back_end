#!/usr/bin/env python3
"""code from wait_n and alter it into a new
function task_wait_n. The code is nearly
identical to wait_n except task_wait_random is being called"""


import asyncio
import random
from typing import List, Set, Dict, Tuple, Union, Callable


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """code from wait_n and alter it into a new
function task_wait_n. The code is nearly
identical to wait_n except task_wait_random is being called"""
    wait_randoms = [task_wait_random(max_delay) for i in range(n)]
    Lists = []
    for j in asyncio.as_completed(wait_randoms):
        Lists.append(await j)
    return (Lists)
