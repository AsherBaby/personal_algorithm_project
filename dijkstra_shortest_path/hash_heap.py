class HashHeap:

    def __init__(self, key=None):
        self.heap = []  # default: min-heap
        self.hash = {}  # hash: node -> pos
        self.key = key  # the same mechanism with key in sort() function

    def __len__(self):
        return len(self.heap)

    def _cmp(self, node1, node2):
        #  Good!
        if not self.key:
            return node1 < node2
        return self.key(node1) < self.key(node2)

    def add(self, node):
        """Add the node"""
        self.heap.append(node)
        self.hash[node] = len(self.heap)-1
        self._siftup(len(self.heap)-1)

    def poll(self):
        """Poll a minimum node"""
        heap = self.heap
        hash = self.hash
        ans = heap[0]
        if len(heap) == 1:
            del hash[heap[0]]
            del heap[0]
        else:
            self._swap(0, len(heap)-1)
            del hash[heap[-1]]
            del heap[-1]
            self._siftdown(0)
        return ans

    def update(self, node):
        """Update the position of node, if key(node) has changed"""
        pos = self.hash[node]
        self._siftup(pos)
        self._siftdown(pos)

    def delete(self, node):
        """Delete the node"""
        heap = self.heap
        hash = self.hash
        pos = hash[node]
        if pos == len(heap) - 1:
            del hash[node]
            del heap[-1]
        else:
            self._swap(pos, len(heap)-1)
            del hash[node]
            del self.heap[-1]
            self._siftup(pos)
            self._siftdown(pos)

    def _swap(self, pos1, pos2):
        # good!
        node1 = self.heap[pos1]
        node2 = self.heap[pos2]
        self.hash[node1] = pos2
        self.hash[node2] = pos1
        self.heap[pos1] = node2
        self.heap[pos2] = node1

    def _siftdown(self, pos):
        left_child = lambda pos: pos*2+1
        right_child = lambda pos: pos*2+2
        heap = self.heap
        while left_child(pos) < len(heap):  # while has at least left child
            l = left_child(pos)
            r = right_child(pos)
            if r >= len(heap) or self._cmp(heap[l], heap[r]):
                # if left child is voted
                if self._cmp(heap[l], heap[pos]):
                    self._swap(l, pos)
                    pos = l
                else:
                    break
            else:
                if self._cmp(heap[r], heap[pos]):  # if violate
                    self._swap(r, pos)
                    pos = r
                else:
                    break

    def _siftup(self, pos):
        parent = lambda pos: (pos-1)//2  # -1//2 == -1
        heap = self.heap
        while parent(pos) >= 0 and self._cmp(heap[pos], heap[parent(pos)]):
            p = parent(pos)
            self._swap(p, pos)
            pos = p
