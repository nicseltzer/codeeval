#!/usr/bin/python

import sys

inputFile = sys.argv[1]

with open(inputFile) as file:
    for line in file:
        line = list(line.strip())
        line = [int(i) for i in line]
        print(sum(line))
