#!/usr/bin/env python
"""
This code is both mapper and reducer.
"""
import bisect
import sys

class Mapper:

    def __init__(self):
        self.top_ten = []

    def insert(self, val):
        top_ten = self.top_ten
        if len(top_ten) < 10:
            bisect.insort(top_ten, val)
        else:
            if val < top_ten[-1]:
                del top_ten[-1]
                bisect.insort(top_ten, val)
    def send(self):
        for n in self.top_ten:
            print(n)

m = Mapper()
for line in sys.stdin:
    val = int(line.rstrip())
    m.insert(val)
m.send()
