class HashHeap:

    class Node:
        def __init__(self, key, idx):
            self.key = key
            self.idx = idx
            self.num = 1

    def __init__(self, type):
        self.heap = []  # heap: list of Node(key, idx, num)
        self.hash = dict()  # hash: key -> Node(key, idx, num)
        self.size = 0  #!!
        self.type = type

    def cmp(self, idx1, idx2):
        key1 = self.heap[idx1].key
        key2 = self.heap[idx2].key
        return key1 < key2 if self.type == 'min' else key1 > key2

    def __len__(self):
        return self.size

    def swap(self, k1, k2):
        heap = self.heap
        heap[k1], heap[k2] = heap[k2], heap[k1]  # swap
        heap[k1].idx = k1  # update
        heap[k2].idx = k2

    def top(self):
        return self.heap[0].key

    def add(self, key):
        self.size += 1
        heap = self.heap
        hash = self.hash
        if key in hash:
            hash[key].num += 1
        else:
            node = self.Node(key, len(heap))
            heap.append(node)
            hash[key] = node
            self.swim(len(heap)-1)

    def delete(self, key):
        self.size -= 1
        heap = self.heap
        hash = self.hash
        if hash[key].num > 1:
            hash[key].num -= 1
        else:
            idx = hash[key].idx
            self.swap(idx, -1)
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
