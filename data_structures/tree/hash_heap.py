"""
Hash heap, a heap data structure that supports O(logN) delete operation.

Hash heap use hash table to map key to index of that key stored in heap array.
"""


class HashHeap:

    class Node:
        def __init__(self, key):
            self.key = key
            self.num = 1

    def __init__(self, type):
        self.heap = []  # heap: list of Node(key, num)
        self.hash = dict()  # hash: key -> idx
        self.type = type

    def __bool__(self):
        # test if hash heap is empty
        return bool(self.heap)

    def cmp(self, k1, k2):
        key1 = self.heap[k1].key
        key2 = self.heap[k2].key
        return key1 < key2 if self.type == 'min' else key1 > key2

    def swap(self, k1, k2):
        heap = self.heap
        hash = self.hash
        heap[k1], heap[k2] = heap[k2], heap[k1]  # swap
        hash[heap[k1].key] = k1
        hash[heap[k2].key] = k2

    def top(self):
        return self.heap[0].key

    def add(self, key):
        heap = self.heap
        hash = self.hash
        if key in hash:
            heap[hash[key]].num += 1
        else:
            node = self.Node(key)
            heap.append(node)
            hash[key] = len(heap)-1
            self.swim(len(heap)-1)

    def delete(self, key):
        heap = self.heap
        hash = self.hash
        idx = hash[key]
        if heap[idx].num > 1:
            heap[idx].num -= 1
        else:
            self.swap(idx, len(heap)-1)
            del hash[key]
            del heap[-1]
            if idx != len(heap):  #!!
                self.swim(idx)
                self.sink(idx)

    def sink(self, k):
        lc = lambda k: k*2+1
        rc = lambda k: k*2+2
        heap = self.heap
        hash = self.hash
        while lc(k) < len(heap):
            c = lc(k) if (
                rc(k) == len(heap) or
                self.cmp(lc(k), rc(k))) else rc(k)
            if self.cmp(c, k):
                self.swap(k, c)
                k = c
            else:
                break

    def swim(self, k):
        p = lambda k: (k-1)//2
        heap = self.heap
        hash = self.hash
        while p(k) >= 0 and self.cmp(k, p(k)):
            self.swap(k, p(k))
            k = p(k)
