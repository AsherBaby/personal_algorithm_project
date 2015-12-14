#!/usr/bin/env python
import sys

for line in sys.stdin:
    words = line.rstrip().split()
    words = [word.rstrip('.,?!').lower() for word in words]
    for word in words:
        print('{}'.format(word))
