#!/usr/bin/env python

import sys

for line in sys.stdin:
    val = line.rstrip()
    key = ''.join(sorted(val))
    print('{0}\t{1}'.format(key, val))

