#!/usr/bin/python

import sys

count = 0
maxCount = 0
filePath = None
oldKey = None

for line in sys.stdin:
    thisKey = line.strip()

    if oldKey and oldKey != thisKey:
	if count > maxCount:
	    maxCount = count;
	    filePath = oldKey;
	oldKey = thisKey;
	count = 1

	
    oldKey = thisKey;
    count += 1

if count > maxCount:
    maxCount = count;
    filePath = oldKey;

print filePath

