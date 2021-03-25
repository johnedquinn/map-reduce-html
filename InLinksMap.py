#!/usr/bin/env python3

### Imports

import sys
import io
import os.path
import urllib.parse

### Main Execution

if __name__ == '__main__':

	# Add UTF-8 Support
	stream = io.TextIOWrapper(sys.stdin.buffer, encoding='iso-8859-1')

	for line in stream:

		# Parse Stream
		try:
			split = line.rstrip().split()
			host  = split[0]
			ref   = split[1]
		except Exception as ex:
			continue
		
		# Standard Output
		print(f'{ref}\t{host}')

	sys.exit(0)
