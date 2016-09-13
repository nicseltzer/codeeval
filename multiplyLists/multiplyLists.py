#!/usr/bin/python -O

import sys

def multiplyLists(inputList):
        buf = inputList.strip().split('|')
        a = buf[0].strip().split(' ')
        b = buf[1].strip().split(' ')
        del buf[0:len(buf)]
        for i in range(len(a)):
                buf.append(int(a[i]) * int(b[i]))
        return ' '.join(map(str, buf))

if __name__ == '__main__':
        with open (sys.argv[1], 'r') as file:
                for line in file:
                        print multiplyLists(line)
