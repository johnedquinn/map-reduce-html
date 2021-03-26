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

	current = set()
	toVisit = set()
	visited = set()
	hops = []

	toVisit.add('www.nd.edu')
	while len(toVisit):
		current = toVisit.copy()
		hops.append(toVisit)
		toVisit = set()
		while len(current):
			host = current.pop()
			visited.add(host)
			for ref in table[host]:
				if ref not in visited: toVisit.add(ref)
	
	# Print
	for index, item in enumerate(hops):
		print(f'{index} {item}')
