#!/usr/bin/python

import sys

inputFile = sys.argv[1]

with open(inputFile) as file:
    for line in file:
        line = line.strip().split(',')
        line = [int(i) for i in line]
        binary = list(bin(line[0]))
        if binary[len(binary) - line[1]] == binary[len(binary) - line[2]]:
            print "true"
        else:
            print "false"