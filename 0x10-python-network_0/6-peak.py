#!/usr/bin/python3
"""
    Defines a peak-finding function
"""


def find_peak(list_of_integers):
    """Finds peak in a list of unsorted integers"""
    nums = list_of_integers
    length = len(nums)
    if (length == 0):
        return (None)
    if (length == 1):
        return (nums[0])
    if (length == 2):
        if (nums[0] >= nums[1]):
            return (nums[0])
        else:
            return(nums[1])

    m = int(length / 2)
    peak = nums[m]
    if peak > nums[m - 1] and peak > nums[m + 1]:
        return peak
    elif peak < nums[m - 1]:
        return find_peak(nums[:m])
    else:
        return find_peak(nums[m + 1:])
