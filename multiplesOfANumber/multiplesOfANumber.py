#!/usr/bin/python

import sys
import math

def findMultiples(line):
    # split out the values
    line = line.split(',')
    print line
    x = int(line[0])
    y = int(line[1])
    print x, y
    if y > x:
        return y
    elif y < x:
        buf = math.sqrt(y)
        print buf

inputFile = sys.argv[1]
with open(inputFile) as file:
    for line in file:
        print findMultiples(line.strip())