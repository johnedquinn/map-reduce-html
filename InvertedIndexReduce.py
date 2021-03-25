#!/usr/bin/env python3

### Imports

import sys
import io
from collections import defaultdict

### Main Execution

if __name__ == '__main__':

	table = defaultdict(set)

	# Add UTF-8 Support
	stream = io.TextIOWrapper(sys.stdin.buffer, encoding='iso-8859-1')

	# Grab Words and Hosts
	for line in stream:
		try:
			word, host = line.rstrip().split()
			table[word].add(host)
		except:
			continue

	# Print
	for word, hosts in table.items():
		print(f'{word}')
		for host in hosts:
			print(f'  {host}')
