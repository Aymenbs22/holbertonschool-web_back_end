#!/usr/bin/env python3
"""function sum_list which takes a list input_list of floats
as argument and returns their sum as a float"""


import math
import typing
from typing import List, Set, Dict, Tuple


def sum_list(input_list: List[float]) -> float:
"""function sum_list which takes a list input_list of floats
as argument and returns their sum as a float"""
    return(math.fsum(input_list))
