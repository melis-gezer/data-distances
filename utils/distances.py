from __future__ import annotations
import math

def manhattan(a, b):
    a = list(a)
    b = list(b)
    if len(a) != len(b):
        raise ValueError("vectors must have the same length")
    return sum(abs(x - y) for x, y in zip(a, b))

def euclidean(a, b):
    a = list(a)
    b = list(b)
    if len(a) != len(b):
        raise ValueError("vectors must have the same length")
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))
