#!/usr/bin/env python3
"""
this module contains a method get_page that takes two integer arguments page
 with default value 1 and page_size with default value 10
"""

import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """this method takes two args and returns tuple of size two containing
    the start and end indices corresponding to the range of indices to return
    in a list for those particular pagination parameters
    Args:
        page(int): page number to return
        page_size(int): number of items per page
    Return: tuple(start, end)
    """
    start = 0
    end = 0
    for i in range(page):
        start = end
        end += page_size

    return (start, end)


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
        """this function takes 2 int args page = 1 and page_size = 10 and
        return appropriate page of the dataset
        Args:
            page(int): requested page (must be positive value > 0)
            page_size(int): number of items per page(must be postive value > 0)
        Return:
            list of list containing required data
        """
        assert type(page) == int and type(page_size) == int and\
            page > 0 and page_size > 0
        data = self.dataset()
        try:
            index = index_range(page, page_size)
            return data[index[0]: index[1]]
        except IndexError:
            return []
