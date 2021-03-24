#!/usr/bin/env python3
"""0. Simple helper function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> tuple:
    """The function should return start index and an end index.
    Page numbers are 1-indexed, i.e. the first page is page 1.
    """
    last_idx = page * page_size
    first_idx = last_idx - page_size
    return (first_idx, last_idx)
