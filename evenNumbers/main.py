#!/usr/bin/python
import sys


def isItEven(n):
    if int(n) % 2:
        return 0
    else:
        return 1


if __name__ == '__main__':
    with open(sys.argv[1]) as file:
        for line in file:
            print isItEven(line.strip())
