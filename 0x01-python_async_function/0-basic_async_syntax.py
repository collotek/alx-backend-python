#!/usr/bin/env python3
"""asynchronous concept in python
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """generates random float and wait those seconnds

    Args:
        max_delay (int): max delay value which default to 10.

    Return:
        float: number of seconds delayed
    """
    x = random.uniform(0, max_delay)
    await asyncio.sleep(x)
    return x
