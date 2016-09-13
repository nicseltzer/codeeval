#!/usr/bin/python

import sys

def rightmostChar(string):
    indexTarget = string[-1]
    return string[0].rfind(indexTarget)

if __name__ == "__main__":
    inputFile = open(sys.argv[1], 'r')
    for line in inputFile:
        if not line.strip():
            continue
        try:
            print rightmostChar(line.strip().split(','))
        except Exception as e:
            print e