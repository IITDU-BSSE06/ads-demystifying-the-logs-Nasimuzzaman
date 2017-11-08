#!/usr/bin/python

import sys

count = 0
oldKey = None


for line in sys.stdin:
    data1 = line.split("\"")
    data2 = data1[1].split("\t")
    thisKey = data2[0]

    if oldKey and oldKey != thisKey:
	print oldKey, "\t", count
	oldKey = thisKey;
	count = 1

    oldKey = thisKey;
    count += 1

print oldKey, "\t", count
