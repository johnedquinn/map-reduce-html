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
			split = line.rstrip().split()
			host  = split[0]
			ref   = split[1]
			table[host].add(ref)
		except:
			continue

	# Print
	for host, refs in table.items():
		print(f'{host}')
		for ref in refs:
			print(f'  {ref}')
