"""
Rate limited implemented with a bounded queue

Pros: rate limit in any second
"""
from collections import deque
class RateLimiter:

    def __init__(self, limit):
        self.limit = limit
        self.queue = deque()

    def acquire(self, t):
        if len(self.queue) < self.limit:
            self.queue.append(t)
            return True
        if t - self.queue[0] >= 1:
            self.queue.popleft()
            self.queue.append(t)
            return True
        return False
