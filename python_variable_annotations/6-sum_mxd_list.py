#!/usr/bin/env python3
"""mixed list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    A function sum_mixed_list which takes a list mxd_lst
    of integers and floats ad returns their sum as a float.
    """

    return sum(mxd_lst)