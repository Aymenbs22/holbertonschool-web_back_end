#!/usr/bin/env python3
import math
import typing
from typing import List, Set, Dict, Tuple, Union, Iterable, Sequence

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
