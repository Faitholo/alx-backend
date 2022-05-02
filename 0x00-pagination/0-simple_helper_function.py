#!/usr/bin/env python3
"""
This module contains a function that takes two integer arguments page and
page_size and returns a tuple of size two containing start and end index"
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """this method takes two args and returns tuple of size two
    containing a start and end index
    """
    start_index = 0
    end_index = 0
    for i in range(page):
        start_index = end
        end_index += page_size

    return (start_index, end_index)
