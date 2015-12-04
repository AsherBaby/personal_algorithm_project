#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.rstrip().split()
    if not line:
        continue
    key = line[0]
    values = line[1:]
    for value in values:
        print('{0}\t{1}'.format(value, key))
