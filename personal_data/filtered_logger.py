#!/usr/bin/env python3
"""function called filter_datum that returns the log message obfuscated
The function should use a regex to replace occurrences of certain field values.
filter_datum should be less than 5 lines long and use re.sub
toperform the substitution with a single regex"""


from typing import List
import re


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """function called filter_datum that returns the log message obfuscated
The function should use a regex to replace occurrences of certain field values.
filter_datum should be less than 5 lines long and use re.sub
toperform the substitution with a single regex"""
    for i in fields:
        message = re.sub(f'{i}=.*?{separator}',
                         f'{i}={redaction}{separator}', message)
    return message
