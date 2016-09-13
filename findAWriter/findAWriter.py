#!/usr/bin/python
import sys

def findEm(line):
    buf = []
    line = line.split('|')
    listKey = line[1].strip().split()
    listValue = list(line[0].strip())
    for i in listKey:
        buf.append(listValue[int(i)-1])
    return ''.join(buf)


if __name__ == '__main__':
    inputFile = sys.argv[1]
    with(open(inputFile)) as file:
        for line in file:
            line = line.strip()
            print findEm(line)
