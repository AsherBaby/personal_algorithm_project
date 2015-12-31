"""
Rate limiter implemented with bucket.

Pros: rate limit in every second
Cons: not in any second
"""
import math

class RateLimiter:

    def __init__(self, limit):
        self.limit = limit
        self.counter = 0
        self.t = 0

    def acquire(self, t):
        if math.floor(t) != math.floor(self.t):  # next bucket
            self.counter = 0
        if self.counter < self.limit:
            self.counter += 1
            return True
        else:
            return False
