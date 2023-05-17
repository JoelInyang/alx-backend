#!/usr/bin/env python3
"""index_range is a function that takes two integer arguments
    page and page_size and the results are paginated.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """the Page numbers are 1-indexed, the first page is page 1 and it continues.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
