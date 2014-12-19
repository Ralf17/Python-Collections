#!/usr/bin/env python

def is_prime(x):
    if x == 0 or x == 1 or x < 0:
        return False
    else:
        for n in range(2, x):
             if x % n == 0:
                  return  False
                  break
        else:
             return True
