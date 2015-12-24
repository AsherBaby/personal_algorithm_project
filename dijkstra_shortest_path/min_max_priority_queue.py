"""
Min max priority queue, get min and max in O(1)
"""
from hash_priority_queue import HashPriorityQueue

class MinMaxPriorityQueue:

    def __init__(self):
        self.min_pq = HashPriorityQueue()
        self.max_pq = HashPriorityQueue(key=lambda x, y: x > y)

    def __len__(self):
        return len(self.min_pq)

    def get_min(self):
        return self.min_pq.top()

    def get_max(self):
        return self.max_pq.top()

    def add(self, key):
        self.min_pq.add(key)
        self.max_pq.add(key)

    def pop_min(self):
        ans = self.min_pq.pop()
        self.max_pq.delete(ans)
        return ans

    def pop_max(self):
        ans = self.max_pq.pop()
        self.min_pq.delete(ans)
        return ans
