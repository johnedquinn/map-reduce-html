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

	# Grab Standard Input
	for line in sys.stdin:

		# Grab URLs
		urls = re.findall('href="([^"]+)"', line)

		# Parse URLs and Print Host Names
		for url in urls:
			parsed_url = urllib.parse.urlparse(url)
			if parsed_url.netloc: print(parsed_url.netloc)
