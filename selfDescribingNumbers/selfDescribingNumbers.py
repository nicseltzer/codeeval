#!/usr/bin/python -O

import sys


def describeMeLikeOneOfYourFrenchGirls(line):
    line = list(line)
    for item, qty in enumerate(line):
        counter = line.count(str(item))
        if int(qty) == int(counter):
            continue
        else:
            return 0
    return 1

if __name__ == '__main__':
    with open(sys.argv[1]) as file:
        for line in file:
            print describeMeLikeOneOfYourFrenchGirls(line.strip())
