#!/usr/bin/env python

with open('input', 'r') as f:
    for line in f:
      nums = line.split()
      if len(nums) == 2:
         start = int(nums[0])
         end = int(nums[1]) + 1
         total = 0
         for i in range(start, end):
            if i % 2 == 1:
              total += i
         print total
