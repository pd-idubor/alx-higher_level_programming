#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = tuple_a
    b = tuple_b

    if len(a) < 2:
        if len(a) == 0:
            a = 0, 0
        else:
            a = a[0], 0
    if len(b) < 2:
        if len(b) == 0:
            b = 0, 0
        else:
            b = b[0], 0
    sum_a = a[0] + b[0]
    sum_b = a[1] + b[1]
    return(sum_a, sum_b)
