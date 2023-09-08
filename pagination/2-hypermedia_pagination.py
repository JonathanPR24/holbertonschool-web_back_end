#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict

class Server:
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """
        Retrieve and cache the dataset, excluding the header.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Create and cache an indexed version of the dataset.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Retrieve a page of data based on the given index and page size.
        """
        result_dataset = []
        index_data = self.indexed_dataset()
        keys_list = list(index_data.keys())

        if index is None or index < 0 or index >= len(keys_list):
            # Handle invalid index or out-of-bounds index
            return {
                'index': None,
                'next_index': None,
                'page_size': 0,
                'data': result_dataset
            }

        for i in range(index, min(index + page_size, len(keys_list))):
            result_dataset.append(index_data[keys_list[i]])

        next_index = min(index + page_size, len(keys_list))

        return {
            'index': index,
            'next_index': next_index,
            'page_size': len(result_dataset),
            'data': result_dataset
            }
