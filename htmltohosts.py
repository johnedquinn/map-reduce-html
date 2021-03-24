#!/usr/bin/env python3

##
# @name  htmltohosts
# @desc  NA
##

### Imports

import sys
import re
import urllib.parse


### Main Execution

if __name__ == '__main__':

	# Add UTF-8 Support
	stream = io.TextIOWrapper(sys.stdin.buffer, encoding='iso-8859-1')

	# Grab Standard Input
	for line in stream:

		# Grab URLs
		urls = re.findall('href="([^"]+)"', line)

		# Parse URLs and Print Host Names
		for url in urls:
			parsed_url = urllib.parse.urlparse(url)
			if parsed_url.netloc: print(parsed_url.netloc)
