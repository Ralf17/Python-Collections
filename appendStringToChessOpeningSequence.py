#!/usr/bin/env python

from operator import itemgetter

data = []

    
with open('input', 'r') as f:
    for line in f:
    	if line.strip():
     	   words = line.split()
           words.append("1-0")
           for key in words:
              print key,
           print "\n"
