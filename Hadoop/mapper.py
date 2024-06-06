#!/usr/bin/env python 

# import sys because we need to read and write data to STDIN and STDOUT 
import sys 

# reading entire line from STDIN (standard input) 
for line in sys.stdin: 
	# to remove leading and trailing whitespace 
	line = line.strip() 
	# split the line into words 
	words = line.split() 
		
	# As we have to only count the words so removing the punctuation marks
	for word in words:
		if word in [",",".","?","!"]:
			pass
		else:
		
		
		# we are looping over the words array and printing the word 
	 	# with the count of 1 to the STDOUT
			print ('%s\t\t\t%s' % (word, 1) )
			
		# write the results to STDOUT (standard output); 
		# what we output here will be the input for the 
		# Reduce step, i.e. the input for reducer.py 
