#!/usr/bin/env python3

##
# @name  htmltowords
# @desc  NA
##

### Imports

import sys
import re
import urllib.parse
import string
import io
import os


### Main Execution

if __name__ == '__main__':

	INCLUDE_HOST = False

	# Parse Command Line
	if len(sys.argv) == 2:
		if sys.argv[1] == '-h':
			INCLUDE_HOST = True

	# Add UTF-8 Support
	stream = io.TextIOWrapper(sys.stdin.buffer, encoding='iso-8859-1')

	# Grab Standard Input
	for line in stream:

		line = line.rstrip()

		# Grab Words Between Tags
		word_groups = re.findall('>([^<]+)|^([^<]+)', line)

		# Grab Group of Words
		for group1, group2 in word_groups:

			# Split into Words
			words = []
			words.extend(group1.split())
			words.extend(group2.split())

			for word in words:

				# Remove Punctuation
				word.translate(str.maketrans('', '', string.punctuation))

				# Make Sure Valid
				word = word.rstrip()
				if word.isnumeric() or not word.isalpha(): continue
				if len(word) < 3: continue
				
				# Print
				if not INCLUDE_HOST:
					print(word.lower())
				else:
					in_file = os.getenv('mapreduce_map_input_file')
					print(f'{in_file}\t{word.lower()}')

	sys.exit(0)
