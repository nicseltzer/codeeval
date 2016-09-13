#!/usr/bin/python

import sys
import re

def calculateIt(line):
    buf = re.compile(r'\-?\d+, \d+')
    print buf.findall(line)

if __name__ == '__main__':
    with open(sys.argv[1]) as file:
        for line in file:
            print calculateIt(line.strip())
