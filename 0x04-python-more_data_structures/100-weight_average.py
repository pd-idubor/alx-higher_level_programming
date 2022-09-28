#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return(0)

    den = 0
    add = 0
    for tup in my_list:
        mul = 1
        for i in tup:
            mul *= i
        add += mul
        den += i
    return(add / den)
