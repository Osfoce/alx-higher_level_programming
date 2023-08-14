#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
# Ensure both tuples have at least 2 elements
    while len(tuple_a) < 2:
        tuple_a = tuple_a + (0,)
    while len(tuple_b) < 2:
        tuple_b = tuple_b + (0,)
# Take only the first 2 elements of each tuple
    tuple_a = tuple_a[:2]
    tuple_b = tuple_b[:2]
# Add the tuples element-wise
    result = tuple(x + y for x, y in zip(tuple_a, tuple_b))
    return result
