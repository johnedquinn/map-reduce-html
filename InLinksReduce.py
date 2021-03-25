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
			ref   = split[0]
			host  = split[1]
			table[ref].add(host)
		except:
			continue

	# Print
	for ref, hosts in table.items():
		print(f'{ref}')
		for host in hosts:
			print(f'  {host}')
