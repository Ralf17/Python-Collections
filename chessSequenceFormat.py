#!/usr/bin/env python

from operator import itemgetter

data = []

    
with open('input', 'r') as f:
    for line in f:
    	if line.strip():
     	   words = line.split()
           print "%s%s %s %s%s %s %s%s %s %s%s %s %s%s %s %s%s %s %s%s %s %s%s %s %s%s %s %s%s %s %s%s %s %s%s %s %s%s %s %s%s %s %s%s %s %s"%(words[0],words[1],words[2],words[3],words[4],words[5],words[6],words[7],words[8],words[9],words[10],words[11],words[12],words[13],words[14],words[15],words[16],words[17],words[18],words[19],words[20],words[21],words[22],words[23],words[24],words[25],words[26],words[27],words[28],words[29],words[30],words[31],words[32],words[33],words[34],words[35],words[36],words[37],words[38],words[39],words[40],words[41],words[42],words[43],words[44],words[45])   
           print 
