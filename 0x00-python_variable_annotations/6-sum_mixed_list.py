#!/usr/bin/env python3
"""
Mixed type-annotated function that takes in input_list(int, list)
and returns the sum(float) of the elements
"""
from typing import Union, List


def sum_mixed_list(input_list: List[Union[int, float]]) -> float:
    """
    Takes in list of mixed data types and
    Returns the sum of integers and floats as a float
    """
    return sum(input_list)
