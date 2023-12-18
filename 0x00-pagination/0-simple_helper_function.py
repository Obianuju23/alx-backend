#!/usr/bin/env python3
"""This is a module that takes two integer args&returns tuple of size 2"""


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Function that returns tuple of two size containing start&end index"""

    start_index = page * page_size - page_size
    end_index = start_index + page_size

    return(start_index, end_index)
