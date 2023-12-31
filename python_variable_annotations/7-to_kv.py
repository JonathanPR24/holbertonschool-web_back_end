#!/usr/bin/env python3
"""Function to create a tuple with a string and the square of an int/float."""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Create a tuple with a string and the square of an int/float."""
    return k, v ** 2.0
