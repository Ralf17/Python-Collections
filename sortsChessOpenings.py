#!/usr/bin/env python

from operator import itemgetter

data = []

    
with open('input', 'r') as f:
    for line in f:
    	if line.strip():
     	   words = line.split()
           data.append(words)

lst = data 
lst = sorted(lst, key=itemgetter(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30))

numrows = len(lst)
numcols = len(lst[0])

for i in range(0, numrows):
   for j in range(0, numcols):
       print lst[i][j],
   print "\n"
