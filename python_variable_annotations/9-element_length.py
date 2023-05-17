#!/usr/bin/env python3
"""function’s parameters and return values
with the appropriate types"""


import math
import typing
from typing import List, Set, Dict, Tuple, Union, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """function’s parameters and return values
with the appropriate types"""
    return [(i, len(i)) for i in lst]
