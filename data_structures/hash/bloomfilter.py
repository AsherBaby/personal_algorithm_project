"""
Bloom-filter, a data structure to quickly check whether an object exists.
However, it has small false positive probability.
"""
from bitarray import bitarray


class BloomFilter:

    def __init__(self, size):
        self.array = bitarray(size)
        self.array.setall(False)
        self.cap = size

    def insert(self, s):
        key = hash(s) % self.cap
        self.array[key] = True

    def lookup(self, s):
        key = hash(s) % self.cap
        return self.array[key]
