import unittest
from datetime import datetime, timedelta
from visitor_counter import VisitorCounter

class TestVisitorCounter(unittest.TestCase):

    def setUp(self):
        self.counter = VisitorCounter()

    def test_of_same_hour(self):
        self.counter.log(datetime.now()+timedelta(minutes=15))
        self.counter.log(datetime.now()+timedelta(minutes=15))
        self.assertEqual(self.counter.get(), 2)

    def test_of_different_hour(self):
        self.counter.log(datetime.now()+timedelta(minutes=15))
        self.counter.log(datetime.now()+timedelta(hours=1, minutes=15))
        self.assertEqual(self.counter.get(), 1)

if __name__ == '__main__':
    unittest.main()
