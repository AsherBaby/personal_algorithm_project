#!/usr/bin/env python

import bisect
import sys

class Reducer:

    def __init__(self):
        self.top_ten = []

    def is_top_ten(self, vals):
        top_ten = self.top_ten
        for val in vals:
            if len(top_ten) < 10:
                bisect.insort(top_ten, val)
            else:
                if val < top_ten[9]:
                    del top_ten[9]
                    bisect.insort(top_ten, val)

    def cleanup(self):
        print(' '.join([str(n) for n in self.top_ten]))

r = Reducer()
for line in sys.stdin:
    vals = [int(n) for n in line.rstrip().split()]
    r.is_top_ten(vals)
r.cleanup()
