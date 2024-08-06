#!/usr/bin/env python3
"""
Type-annotated function that takes in a list of floats
and returns the sum of the list
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Sums up floats in a list of floats and
    returns the sum as a float
    """
    return sum(input_list)
