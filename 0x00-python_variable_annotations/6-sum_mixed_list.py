#!/usr/bin/env python3
from typing import Union, List

Num = Union[int, float]


def sum_mixed_list(mxd_lst: List[Num]) -> float:
    return sum(mxd_lst)
