#!/usr/bin/python

import sys

count = 0

for line in sys.stdin:
    ip = line.strip()

    if ip == "10.99.99.186":
	count += 1

print count

