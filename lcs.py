#!/usr/bin/python -O

import sys

def findLCS(firstString, secondString):
        '''
        Using the backtracking methodology, find the Lowest Common Subsequence for two given strings.
        '''

        firstStringLength = len(firstString)
        secondStringLength = len(secondString)
        buf = []

        grid = [[0 for i in range(len(secondString) + 1)] for j in range(len(firstString) + 1)]

        # breka apart enums and value s
        for a, x in enumerate(firstString):
                for b, y in enumerate(secondString):
                        # if the values x and y are equal at the current enum
                                if x == y:
                                # increment the value in the grid by one for this and future cells
                                grid[a + 1][b + 1] = grid[a][b] + 1
                        # if values are anything else, repeat the largest enum between a and b + 1
                        else:
                                grid[a + 1][b + 1] = max(grid[a + 1][b], grid[a][b + 1])
                        print a, b, x, y


        # secondStringLength is col
        # until we reach the beginning of the strings
        while firstStringLength != 0 and secondStringLength != 0:
                # if a repeated value is found to be equal to the next value, discard and decrement row counter
                if grid[firstStringLength][secondStringLength] == grid[firstStringLength - 1][secondStringLength]:
                        firstStringLength -= 1
                # if a repeated value is found to be equal to the next value, discard and decrement col counter
                elif grid[firstStringLength][secondStringLength] == grid[firstStringLength][secondStringLength - 1]:
                        secondStringLength -= 1
                # everything else is unique, though in reverse order
                else:
                        # append it to the "buf" globally-scoped var
                        buf.append(firstString[firstStringLength - 1])
                        # decrement row and col counters
                        firstStringLength -= 1
                        secondStringLength -= 1

        # push button, recieve reversed output
        return ''.join(buf[::-1])

if __name__ == '__main__':
        with open(sys.argv[1]) as inputFile:
                for line in inputFile:
                        x, y = line.strip().split(';')
                        print findLCS(x, y)
