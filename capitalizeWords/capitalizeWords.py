#!/usr/bin/python -O

import sys
import string


def strictlyCapWords(line):
    '''
    Evidently, there isn't a build-in which retains the formatting of the rest
    of a word when "capitalizing" it. This Function will capitalize the fiirst
    letter of the word of each word in the line passed to it as a list and
    joins it all together in "buf".
    '''

    buf = []
    for i in line:
        buf.append(string.capitalize(i[0]) + i[1:])
    return ' '.join(buf)

if __name__ == "__main__":
    with open(sys.argv[1]) as file:
        for line in file:
            print strictlyCapWords(line.split())
