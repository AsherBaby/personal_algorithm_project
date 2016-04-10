import random
import unittest
from hash_heap import HashHeap

class TestHashHeap(unittest.TestCase):

    def test_of_add_and_delete(self):
        pq = HashHeap('min')
        array = random.sample(range(100000), 10000)
        for each in array:
            pq.add(each)
        array.sort()
        for i in range(10000):
            min = pq.top()
            self.assertEqual(min, array[i])
            pq.delete(min)

if __name__ == '__main__':
    unittest.main()
