#!/usr/bin/env python3

##
# @name  htmltohosts
# @desc  NA
##

### Imports

import sys
import re
import urllib.parse
import os
import io

### Main Execution

if __name__ == '__main__':

	# Grab File (Hostname) from Environment
	in_file = os.getenv('mapreduce_map_input_file')
	path = urllib.parse.urlparse(in_file).path
	host = os.path.split(path)[1]

	# Add UTF-8 Support
	stream = io.TextIOWrapper(sys.stdin.buffer, encoding='iso-8859-1')

	# Grab Standard Input
	for line in stream:

		# Grab URLs
		urls = re.findall('href="([^"]+)"', line)

		# Parse URLs and Print Host Names
		for url in urls:
			parsed_url = urllib.parse.urlparse(url)
			if parsed_url.netloc: print(f'{host}\t{parsed_url.netloc}')
