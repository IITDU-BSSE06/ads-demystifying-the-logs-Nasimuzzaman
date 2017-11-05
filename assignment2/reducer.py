#!/usr/bin/python

import sys

count = 0

for line in sys.stdin:
    filePath = line.strip()

    if filePath == "/assets/js/the-associates.js":
	count += 1

print count
