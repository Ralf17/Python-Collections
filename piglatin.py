#!/usr/bin/env python

word = raw_input('Enter a word: ').lower()

if len(word) > 0 and word.isalpha():
	word = word[1:] + word[0] + 'ay'
	
print word
