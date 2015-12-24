import unittest
from priority_queue import PriorityQueue

class TestPriorityQueue(unittest.TestCase):

    def test_of_heap_sort(self):
        array = [8, 5, 3, 9, 6, 4, 2, 6]
        pq = PriorityQueue()
        for n in array:
            pq.add(n)
        sorted_array = []
        for i in range(len(array)):
            sorted_array.append(pq.pop())
        self.assertEqual(
            sorted_array,[2, 3, 4, 5, 6, 6, 8, 9] )

if __name__ == '__main__':
    unittest.main()
