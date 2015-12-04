#!/usr/bin/env python

import bisect
import sys

class Mapper:

    def __init__(self):
        self.top_ten = []

    def is_top_ten(self, val):
        top_ten = self.top_ten
        if len(top_ten) < 10:
            bisect.insort(top_ten, val)
        else:
            if val < top_ten[9]:
                del top_ten[9]
                bisect.insort(top_ten, val)
    def cleanup(self):
        print(' '.join([str(n) for n in self.top_ten]))

m = Mapper()
for line in sys.stdin:
    val = int(line.rstrip())
    m.is_top_ten(val)
m.cleanup()
