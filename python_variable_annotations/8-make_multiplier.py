#!/usr/bin/env python3
"""function make_multiplier that takes a float multiplier as argument
and returns a function that multiplies a float by multiplier"""


import math
import typing
from typing import List, Set, Dict, Tuple, Union, Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """function make_multiplier that takes a float multiplier as argument
and returns a function that multiplies a float by multiplier"""
    def multiplies(flt):
        return (flt * multiplier)
    return(multiplies)
