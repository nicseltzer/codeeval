#!/usr/bin/python

import sys
import json


def parseDatJSON(arg):
    addingIsHard = 0
    buf = json.loads(arg)
    menu = buf['menu']
    for x in menu['items']:
        tmpJSONID = x['id']
        tmpJSONLabel = x['label']
        if tmpJSONLabel:
            print addingIsHard
            addingIsHard = addingIsHard + tmpJSONID
    return addingIsHard


if __name__ == "__main__":
    with open(sys.argv[1]) as inputFile:
        for line in inputFile:
            try:
                print parseDatJSON(line.strip())
            except:
                print 
