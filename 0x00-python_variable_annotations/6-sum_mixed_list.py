#!/usr/bin/env python3
"""sum a list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """returns sumed list"""
    return sum(mxd_lst)
