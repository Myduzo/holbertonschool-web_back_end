#!/usr/bin/env python3
"""2. Hypermedia pagination
"""
import csv
import math
from typing import Tuple, List

index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Implement a method named get_page that takes two integer arguments
         page with default value 1 and page_size with default value 10.
         """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        range = index_range(page, page_size)
        self.dataset()
        return self.__dataset[range[0]: range[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Implement a get_hyper method that takes the same arguments
         (and defaults) as get_page and returns a dictionary containing
          the following key-value pairs.
         """
        getPage = self.get_page(page, page_size)
        allPages = math.ceil(len(self.dataset()) / page_size)
        hyperDict = {
            'page_size': len(getPage),
            'page': page,
            'data': getPage,
            'next_page': page + 1 if page < allPages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': allPages
        }
        return hyperDict
