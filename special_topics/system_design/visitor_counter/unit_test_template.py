import unittest
from visitor_counter import VisitorCounterByQueue, VisitorCounterByArray

class TestVisitorCounterByQueue(unittest.TestCase):

    def setUp(self):
        self.counter = VisitorCounterByQueue()

    def test_of_same_hour_get(self):
        self.counter.log_hit(1)
        self.counter.log_hit(1)
        self.counter.log_hit(2)
        ans = self.counter.get_hit(4)
        self.assertEqual(ans, 3)

    def test_of_another_hour_get(self):
        self.counter.log_hit(1)
        self.counter.log_hit(1)
        self.counter.log_hit(2)
        ans = self.counter.get_hit(61)
        self.assertEqual(ans, 1)

class TestVisitorCounterByArray(unittest.TestCase):

    def setUp(self):
        self.counter = VisitorCounterByArray()

    def test_of_same_hour_get(self):
        self.counter.log_hit(1)
        self.counter.log_hit(1)
        self.counter.log_hit(2)
        ans = self.counter.get_hit(4)
        self.assertEqual(ans, 3)

    def test_of_another_hour_get(self):
        self.counter.log_hit(1)
        self.counter.log_hit(1)
        self.counter.log_hit(2)
        ans = self.counter.get_hit(61)
        self.assertEqual(ans, 1)

if __name__ == '__main__':
    unittest.main()
