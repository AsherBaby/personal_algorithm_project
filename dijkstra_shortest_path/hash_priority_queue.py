"""
Hash priority queue

Hash priority queue provides delete(obj), update(obj) methods in
O(lgn) time. One direct application of hash priority queue is in
Dijkstra algorithm, since it modifies keys of objects that stored in
priority queue. Another application or data structure based on hash
priority queue is MinMaxPriorityQueue.

Ideas during implementation
    1. Sentinel node is popular, however, when store complex object in
    heap, sentinel node could be complex to create.
    2. It is better to keep track of duplicates in hash, since in heap
    we only store objects.
"""
from priority_queue import PriorityQueue

class HashPriorityQueue(PriorityQueue):

    class Node:
        """
        Element in hash
        """
        def __init__(self, idx):
            self.idx = idx
            self.num = 1

    def __init__(self, key=lambda x, y: x < y):
        self.heap = list()
        self.hash = dict()
        self.before = key
        self.size = 0

    def __len__(self):
        return self.size

    def __contains__(self, key):
        return key in self.hash

    def _swap(self, i, j):
        heap = self.heap
        hash = self.hash
        a = heap[i]
        b = heap[j]
        heap[i], heap[j] = heap[j], heap[i]
        hash[a].idx, hash[b].idx = hash[b].idx, hash[a].idx

    def add(self, key):
        self.size += 1
        if key in self.hash:
            self.hash[key].num += 1
        else:
            self.hash[key] = self.Node(len(self.heap))
            PriorityQueue.add(self, key)

    def pop(self):
        heap = self.heap
        hash = self.hash
        if heap:
            self.size -= 1
            ans = heap[0]
            if hash[ans].num > 1:
                hash[ans].num -= 1
            else:
                self._swap(0, len(self.heap)-1)
                del self.hash[ans]
                del self.heap[-1]
                self._sink(0)
            return ans
        else:
            return None

    def delete(self, key):
        heap = self.heap
        hash = self.hash
        if key not in hash:
            return
        self.size -= 1
        if hash[key].num > 1:
            hash[key].num -= 1
            return
        k = hash[key].idx
        if k == len(heap) - 1:
            del hash[key]
            del heap[-1]
        else:
            self._swap(k, len(heap)-1)
            del hash[key]
            del self.heap[-1]
            self._swim(k)
            self._sink(k)

    def update(self, key):
        heap = self.heap
        hash = self.hash
        k = hash[key].idx
        self._swim(k)
        self._sink(k)
