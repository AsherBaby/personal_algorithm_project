#!/usr/bin/env python

import sys

def main():
    i = sys.stdin.readline().rstrip().split()
    if not i:
        return
    i = i[0]
    count = 1
    for line in sys.stdin:
        j = line.rstrip().split()[0]
        if j == i:
            count += 1
        else:
            print('{0} {1}'.format(i, count))
            i = j
            count = 1
    print('{0} {1}'.format(i, count))

main()
