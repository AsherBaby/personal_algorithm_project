#!/usr/bin/env python

import sys

def main():
    i = sys.stdin.readline().rstrip().split()
    if not i:
        return
    doc_list = [i[1]]
    for j in sys.stdin:
        j = j.rstrip().split()
        if j[0] == i[0]:
            doc_list.append(j[1])
        else:
            print('{0} {1}'.format(i[0], doc_list))
            i = j
            doc_list = [i[1]]
    print('{0} {1}'.format(i[0], doc_list))

main()
