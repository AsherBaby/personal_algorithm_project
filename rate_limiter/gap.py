"""
Rate limiter implemented with gap.

Pros: easy algorithm
Cons: might drop innocent packet
"""
from decimal import Decimal

class RateLimiter:

    def __init__(self, limit):
        self.gap = Decimal('1') / Decimal(limit)
        self.t = Decimal('-1')

    def acquire(self, t):
        if t - self.t >= self.gap:
            self.t = t
            return True
        else:
            return False
