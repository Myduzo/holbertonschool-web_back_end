#!/usr/bin/env python3
"""6. Complex types - mixed list"""
from typing import Union, List

Num = Union[int, float]


def sum_mixed_list(mxd_lst: List[Num]) -> float:
    """function sum_mixed_list which takes a list mxd_lst of integers
     and floats and returns their sum as a float."""
    return sum(mxd_lst)
