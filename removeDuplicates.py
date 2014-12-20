#!/usr/bin/env python

def remove_duplicates(lst):
    new = []
    for index in range(0, len(lst)):
        if lst.count(lst[index]) == 1 and new.count(lst[index]) == 0:
            new.append(lst[index])
        elif lst.count(lst[index]) > 1 and new.count(lst[index]) == 0:
            new.append(lst[index])        
    return new
