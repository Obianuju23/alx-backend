#!/usr/bin/env python3
"""This is a module contains index_range fuction that takes two integer
args&returns tuple of size 2, xlass server and Implements a method get_page
that take 2 int args page with default value 1&page_size with default value 10
"""


import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Function that returns tuple of two size containing start&end index"""

    start_index = page * page_size - page_size
    end_index = start_index + page_size

    return(start_index, end_index)


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
        """
        A function that takes two integer arguments page with
        default value 1 and page_size with default value 10
        """

        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0

        dataset = self.dataset()
        start_index, end_index = index_range(page, page_size)

        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]
