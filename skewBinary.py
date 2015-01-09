#!/usr/bin/env python

with open('input', 'r') as f:
    for line in f:
      num = line.split()
      skew_binary = num[0]
      temp = skew_binary[::-1]
      value = 0
      cntr = 1
      if skew_binary != "0":
          for c in temp:
             value += int(c)*(2**cntr-1)
             cntr += 1 
          print value
