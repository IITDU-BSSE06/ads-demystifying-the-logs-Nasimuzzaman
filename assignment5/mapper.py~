#!/usr/bin/python


import sys

from urlparse import urlparse

for line in sys.stdin:
    data = line.strip().split(" ")
    if len(data) == 10:
	print urlparse(data[6]).path
