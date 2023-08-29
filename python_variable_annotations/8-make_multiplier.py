#!/usr/bin/env python3
"""This module provides a function to create a multiplier function."""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
"""Create a function that multiplies a float by a given multiplier."""
    def multiplier_function(x: float) -> float:
        return x * multiplier
    return multiplier_function
