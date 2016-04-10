#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip().split()
    if not line:
        continue
    value = line[0]
    keys = line[1:]
    for key in keys:
        print('{}\t{}'.format(key, value))
        # A tab-separated key-value pair
