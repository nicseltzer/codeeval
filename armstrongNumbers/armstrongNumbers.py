#!/usr/bin/python
import sys


def determineArmstrongness(line):
    buf = []
    for i in list(line):
        buf.append(int(i) ** len(line))
    if sum(buf) == int(line):
        return True
    else:
        return False

inputFile = sys.argv[1]
with open(inputFile) as file:
    for line in file:
        line = line.strip()
        print determineArmstrongness(line)
