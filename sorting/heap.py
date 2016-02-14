"""
Heap:
  public:
    top()
    pop()
    add()
    heapify(arr)
  private:
    _swim()
    _sink()
"""

class Heap:

    def __init__(self, key=lambda x, y: x < y):
        self.heap = []
        self.comp = key

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

    def heapify(self, array):
        # in-place heapify the input array
        tmp = self.heap
        self.heap = array
        for i in range(len(array)//2, -1, -1):
            self._sink(i)
        self.heap = tmp

    def _swim(self, k):
        p = lambda x: (x-1)//2
        while p(k) >= 0 and self.comp(self.heap[k], self.heap[p(k)]):
            self._swap(k, p(k))
            k = p(k)

    def _sink(self, k):
        heap = self.heap
        lc = lambda x: x*2+1
        rc = lambda x: x*2+2
        while lc(k) < len(heap):
            c = lc(k) if (rc(k) >= len(heap) or
                self.comp(heap[lc(k)], heap[rc(k)])) else rc(k)
            if self.comp(heap[c], heap[k]):
                self._swap(c, k)
                k = c
            else:
                break
