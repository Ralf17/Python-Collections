#!/usr/bin/env python

with open('input', 'r') as f:
    for line in f:
      words = line.split()
      for word in words:
         print word[::-1] ,
      print
