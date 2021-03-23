#!/usr/bin/env python3

import sys

if __name__ == '__main__':
	for line in sys.stdin:
		word = line.rstrip()
		print(f'{word}\t1')
