class PriorityQueue:

    def __init__(self, key=lambda x, y: x < y):
        self.heap = []
        self.before = key

    def __len__(self):
        return len(self.heap)

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def add(self, key):
        self.heap.append(key)
        self._swim(len(self.heap)-1)

    def top(self):
        return self.heap[0] if self.heap else None

    def pop(self):
        if self.heap:
            ans = self.heap[0]
            self._swap(0, len(self.heap)-1)
            del self.heap[-1]
            self._sink(0)
            return ans
        else:
            return None

    def _swim(self, k):
        p = lambda x: (x-1)//2
        while p(k) >= 0 and self.before(self.heap[k], self.heap[p(k)]):
            self._swap(k, p(k))
            k = p(k)

    def _sink(self, k):
        heap = self.heap
        lc = lambda x: x*2+1
        rc = lambda x: x*2+2
        while lc(k) < len(heap):
            c = lc(k) if (rc(k) >= len(heap) or
                self.before(heap[lc(k)], heap[rc(k)])) else rc(k)
            if self.before(heap[c], heap[k]):
                self._swap(c, k)
                k = c
            else:
                break
