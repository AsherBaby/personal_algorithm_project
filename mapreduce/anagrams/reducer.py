#!/usr/bin/env python

import sys

def main():
    i = sys.stdin.readline().rstrip().split()
    if not i:
        return
    group = [i[1]]
    for j in sys.stdin:
        j = j.rstrip().split()
        if j[0] == i[0]:
            group.append(j[1])
        else:
            if len(group) > 1:
                print(group)
            i = j
            group = [i[1]]
    if len(group) > 1:
        print(group)

main()

