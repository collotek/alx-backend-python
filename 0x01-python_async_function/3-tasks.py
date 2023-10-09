#!/usr/bin/env python3
"""Create new task"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """create new task

    Args:
        max_delay (int): maximum delay time

    Returns:
        object: task object
    """
    task = asyncio.create_task(wait_random(max_delay))

    return task
