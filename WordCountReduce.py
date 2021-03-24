#!/usr/bin/env python3

### Imports

import sys
import io

### Main Execution

if __name__ == '__main__':

	table = {}

	# Add UTF-8 Support
	stream = io.TextIOWrapper(sys.stdin.buffer, encoding='iso-8859-1')

	for line in stream:

		# Grab Key Value
		word, count = line.rstrip().split()

		if word not in table:
			table[word] = int(count)

		else:
			table[word] += int(count)

	for key, val in sorted(table.items(), key=lambda item: item[1], reverse=True):
		print(f'{key}\t{val}')
