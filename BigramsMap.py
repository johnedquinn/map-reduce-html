#!/usr/bin/env python3

### Imports

import sys
import io

### Main Execution

if __name__ == '__main__':

	# Add UTF-8 Support
	stream = io.TextIOWrapper(sys.stdin.buffer, encoding='iso-8859-1')

	# Grab
	lastWord = None
	for line in stream:

		word = line.rstrip()
		
		# First Word Found
		if lastWord is None:
			lastWord = word
			continue

		# Print Alphabetically
		if word < lastWord:
			print(f'{word} {lastWord}\t1')
		else:
			print(f'{lastWord} {word}\t1')

		lastWord = word

	sys.exit(0)
