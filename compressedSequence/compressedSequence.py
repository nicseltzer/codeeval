#!/usr/bin/python -O

import sys

def compressSequence(sequence):
    return sequence

if __name__ == '__main__':
    with open(sys.argv[1]) as file:
        for line in file:
            print compressSequence(line.strip())