#!/usr/bin/python

import sys

count = 0
oldKey = None

for line in sys.stdin:
    thisKey = line.strip()

    if oldKey != thisKey:
	oldKey = thisKey;
	count += 1

	
    oldKey = thisKey;

print count

