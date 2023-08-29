#!/usr/bin/env python3
"""Script that returns values of appropriate type."""

from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Calculate the length of each sequence in an iterable and."""
    return [(i, len(i)) for i in lst]
