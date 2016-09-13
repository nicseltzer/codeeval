#!/usr/bin/python

import sys
import math

def findMultiples(line):
    line = line.split(",")
    x = int(line[0])
    y = int(line[1])
    if y > x:
        return y
    elif y < x:
        buf = math.sqrt(y)
        return buf

if __name__ == '__main__':
    with open(sys.argv[1]) as line:
        for i in line:
            print findMultiples(i.strip())