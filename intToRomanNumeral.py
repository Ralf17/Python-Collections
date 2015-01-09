#!/usr/bin/env python

with open('input', 'r') as f:
    data = f.readlines()
    data = [int(i) for i in data]
    del data[0]

    roman_numeral_equivalent = {
        1000 : 'M',
        900 : 'CM',
        500 : "D",
        400 : "CD",
        100 : "C",
        90 : "XC",
        50 : "L",
        40 : "XL",
        10 : "X",
        9 : "IX",
        5 : "V",
        4 : "IV",
        1 : "I"
    }
    
    k = list(roman_numeral_equivalent.keys())
    l = sorted(k, reverse=True)

    for line in data:
        if line >= 1 and line <= 3999:    
          num = line
          roman_numeral = ""
          for key in l:
             if num / key != 0:
                 roman_numeral += roman_numeral_equivalent[key] * (num/key)
                 num = num % key 
          print roman_numeral
