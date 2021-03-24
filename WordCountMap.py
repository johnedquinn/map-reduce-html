#!/usr/bin/env python3

### Imports

import sys
import io

### Main Execution

if __name__ == '__main__':

	# Add UTF-8 Support
	stream = io.TextIOWrapper(sys.stdin.buffer, encoding='iso-8859-1')

	for line in stream:
		word = line.rstrip()
		print(f'{word}\t1')
