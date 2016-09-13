#!/usr/bin/python

import sys
inputFile = sys.argv[1]
sentences = []
buf = []

with open(inputFile) as file:
    numberOfValues = int(file.readline())
    contents = file.readlines()
    for i in contents:
        try:
            i = str(i.strip())
            sentences.append((len(i), i))
        except:
            continue

    buf = [i[1] for i in sorted(sentences, reverse=True)[:numberOfValues]]
    print '\n'.join(buf)