#!/usr/bin/env python

def purify(lst):
    new = []
    for index in range(0, len(lst)):
        if lst[index] % 2 == 0:
            new.append(lst[index]) 
    return new   
