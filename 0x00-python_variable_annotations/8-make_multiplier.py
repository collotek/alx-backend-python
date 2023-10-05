#!/usr/bin/env python3
"""function that returns a function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """return a funtion multiplier"""
    def mut(num: float) -> float:
        """returns result of multiplier * num"""
        return num * multiplier

    return mut
