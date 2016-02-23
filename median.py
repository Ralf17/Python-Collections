#!/usr/bin/env python

def median(lst):
    if len(lst) % 2 != 0:
        lst = sorted(lst)
        return lst[len(lst)/2]
    else:
        lst = sorted(lst)
        index1 = len(lst)/2
        index2 = len(lst)/2 - 1
        return (lst[index1] + lst[index2]) / 2.0
