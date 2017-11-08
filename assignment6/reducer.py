#!/usr/bin/python

import sys

count9 = 0
count10 = 0
count11 = 0


for line in sys.stdin:
    data = line.strip().split(":")

    year = data[0]

    if year == "2009":
	count9 += 1

    if year == "2010":
	count10 += 1

    if year == "2011":
	count11 += 1

print "2009", "\t", count9
print "2010", "\t", count10
print "2011", "\t", count11
