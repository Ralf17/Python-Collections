#!/usr/bin/env python

with open('input', 'r') as f:
    for year in f:
       if year != "0\n" and year != "0":
          binary = "{0:b}".format(int(year))
          if binary == binary[::-1]:
               print str(int(year)) + " is a binary palindrome year"
          else:
               temp = binary[::-1]    
               for i in range(0, len(binary)):
                  if temp[i] == "0":
                     temp += "0"
                  else:
                     break
               if temp == temp[::-1]:
                  print str(int(year)) + " is a forced binary palindrome year"
               else:
                  print str(int(year)) + " is not a binary palindrome year"
