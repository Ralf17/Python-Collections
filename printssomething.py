#!/usr/bin/env python

def TopOrBottom(character, width):
	return '%s%s%s' % ('+', (character * (width-2)), '+')
	
def Fmt(val1, leftbit, val2, rightbit):
	part2 = '%.2f' % val2
	return '%s%s%s%s' % ('|', val1.ljust(leftbit-2, ' '), part2.rjust(rightbit-2, ' '), ' |')
	
itms = [['Soda', 1.45], ['Candy', 0.75], ['Bread', 1.95], ['Milk', 2.59]]

print TopOrBottom('=', 40)

total = 0
for cntr in range(0, 4):
	print Fmt(itms[cntr][0], 30, itms[cntr][1], 10)
	total += itms[cntr][1]	
print TopOrBottom('-', 40)
print Fmt('Total', 30, total, 10)
print TopOrBottom('=', 40)


