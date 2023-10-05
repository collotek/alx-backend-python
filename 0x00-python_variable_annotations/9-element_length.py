#!/usr/bin/env python3
""" type annotation"""
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ takes in an iterable object and returns a
        list of tuples.
    """
    return [(i, len(i)) for i in lst]
