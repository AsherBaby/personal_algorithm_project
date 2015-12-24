import unittest
from min_max_priority_queue import MinMaxPriorityQueue

class TestMinMaxPriorityQueue(unittest.TestCase):

    def setUp(self):
        self.pq = MinMaxPriorityQueue()
        array = [8, 5, 3, 9, 6, 4, 2, 6]
        for n in array:
            self.pq.add(n)

    def test_of_add(self):
        min_heap = self.pq.min_pq.heap
        for i in range(1, len(min_heap)):
            p = (i - 1) // 2
            self.assertLess(
                min_heap[p], min_heap[i])
        max_heap = self.pq.max_pq.heap
        for i in range(1, len(max_heap)):
            p = (i - 1) // 2
            self.assertGreater(
                max_heap[p], max_heap[i])

    def test_of_pop_min(self):
        sorted_array = []
        while self.pq:
            sorted_array.append(self.pq.pop_min())
        for i in range(1, len(sorted_array)):
            self.assertLessEqual(
                sorted_array[i-1], sorted_array[i])

    def test_of_pop_max(self):
        sorted_array = []
        while self.pq:
            sorted_array.append(self.pq.pop_max())
        for i in range(1, len(sorted_array)):
            self.assertGreaterEqual(
                sorted_array[i-1], sorted_array[i])



if __name__ == '__main__':
    unittest.main()
