import unittest
from decimal import Decimal
from gap import RateLimiter

class TestGap(unittest.TestCase):

    def test_of_acquire(self):
        RL = RateLimiter(5)
        packets = [Decimal('0.1'), Decimal('0.3'), Decimal('0.5'),
                   Decimal('0.9'), Decimal('1.0'), Decimal('1.5')]
        results = [RL.acquire(each) for each in packets]
        self.assertEqual(
            results, [True, True, True, True, False, True])

if __name__ == '__main__':
    unittest.main()
