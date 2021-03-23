#!/usr/bin/env python3

import sys

if __name__ == '__main__':

	table = {}

	for line in sys.stdin:

		# Grab Key Value
		word, count = line.rstrip().split()

		if word not in table:
			table[word] = int(count)

		else:
			table[word] += int(count)

	for key, val in table.items():
		print(f'{key}\t{val}')
