#!/usr/bin/env python 

from operator import itemgetter 
import sys 

current_word = None
current_count = 0
word = None
temp_list = []
# read the entire line from STDIN 
for line in sys.stdin: 
	# remove leading and trailing whitespace 
	line = line.strip() 
	# splitting the data on the basis of tab we have provided in mapper.py 
	word, count = line.split('\t', 1) 
	# convert count (currently a string) to int 
	try: 
                temp_list.append(word)
 
	except ValueError: 
		# count was not a number, so we ignore this line 
		continue

	# this IF-switch only works because Hadoop sorts map output 
	# by key (here: word) before it is passed to the reducer 
	if current_word == word.lower(): 
		current_count = count 
	else: 
		if current_word: 
			# write result to STDOUT 
			print( '%s\t%s' % (current_word, current_count) )
		current_count = count 
		current_word = word 

# do not forget to output the last word if needed! 
if current_word == word: 
	print( '%s\t%s' % (current_word, current_count) )

