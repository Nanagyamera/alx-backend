#!/usr/bin/env python3
"""
Task 1
"""
import csv
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """
    Calculate the start and end indexes for a given page and page size.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start index and the end index (both 0-indexed) for the given page.
    """
    if page < 1 or page_size < 1:
        raise ValueError("Page and page_size must be greater than or equal to 1.")

    start_index = (page - 1) * page_size
    end_index = start_index + page_size - 1

    return start_index, end_index


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get a specific page of the dataset based on the provided pagination parameters.

        Args:
            page (int, optional): The page number (1-indexed). Default is 1.
            page_size (int, optional): The number of items per page. Default is 10.

        Returns:
            List[List]: The list of rows corresponding to the requested page.
        """
        assert isinstance(page, int) and page > 0, "page must be an integer greater than 0."
        assert isinstance(page_size, int) and page_size > 0, "page_size must be an integer greater than 0."

        dataset = self.dataset()
        total_items = len(dataset)
        start_idx, end_idx = index_range(page, page_size)

        if start_idx >= total_items:
            return []  # Return an empty list if the start index is out of range

        return dataset[start_idx:end_idx + 1]
