#!/usr/bin/python

def f(n):
    if n == 0 or n == 1:
        return n
    else:
        return f(n-1)+f(n-2)

import sys
inputFile = sys.argv[1]
with open(inputFile) as file:
    for line in file:
        line = abs(int(line.strip()))
        print f(line)
