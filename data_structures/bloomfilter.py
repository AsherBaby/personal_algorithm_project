"""
Bloomfilter, a data strucutre to quickly check whether an object exists.
However, it has small false positive probability.
"""
from bitarray import bitarray

class Bloomfilter:

    def __init__(self, size):
        self.array = bitarray(size)
        self.array.setall(False)
        self.size = size

    def insert(self, s):
        key = hash(s) % self.size
        self.array[key] = True

    def lookup(self, s):
        key = hash(s) % self.size
        return self.array[key]
