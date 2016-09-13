#!/usr/bin/python
import sys

def findHappiness(n):
    history = set()
    while n <> 1:
        n = sum(int(i) ** 2 for i in str(n))
        if n in history:
            return 0
        history.add(n)
    return 1

if __name__ == "__main__":
    with open(sys.argv[1], 'r') as file:
        for line in file:
            print findHappiness(int(line.strip()))

"""
Huge tip of the hat to: http://rosettacode.org/wiki/Happy_numbers#Python
"""