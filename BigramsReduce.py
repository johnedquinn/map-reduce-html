#!/usr/bin/env python3

### Imports

import sys
import io
from collections import defaultdict

### Main Execution

if __name__ == '__main__':

	table = defaultdict(lambda: defaultdict(int))

	# Add UTF-8 Support
	stream = io.TextIOWrapper(sys.stdin.buffer, encoding='iso-8859-1')

	for line in stream:

		# Grab Key Value
		try:
			word1, word2, count = line.rstrip().split()
			table[word1][word2] += int(count)
		except:
			continue

	l = { f'{item[0]}:{d[0]}': d[1] for item in table.items() for d in item[1].items() }

	for key, val in sorted(l.items(), key=lambda item: item[1], reverse=True):
		print(f'{key}\t{val}')
