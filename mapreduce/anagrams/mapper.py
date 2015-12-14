#!/usr/bin/env python

import sys

for line in sys.stdin:
    val = line.strip()
    key = ''.join(sorted(val))
    print('{0}\t{1}'.format(key, val))
